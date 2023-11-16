from typing import Optional, Coroutine

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.models import UserHistoryCreate, ShowUser, BaseResponseModel, \
    VisitedDomains
from db.dals import UserHistoryDAL
from db.session import get_db

user_router = APIRouter()


async def _create_new_history_user(body: UserHistoryCreate, db) -> None:
    """
    Создания истории пользователя
    """
    async with db as session:
        async with session.begin():
            user_dal = UserHistoryDAL(session)
            await user_dal.create_history_user(
                links=body.links
            )


async def _get_history_user(
        from_time: int,
        to_time: int,
        page_num: int,
        page_size: int,
        db
):
    """
    Получение истории пользователя
    """
    async with db as session:
        async with session.begin():
            user_dal = UserHistoryDAL(session)
            return await user_dal.get_history_user(
                from_time=from_time,
                to_time=to_time,
                page_num=page_num,
                page_size=page_size
            )


@user_router.post("/visited_links", response_model=BaseResponseModel)
async def add_user_history(
        body: UserHistoryCreate,
        db: AsyncSession = Depends(get_db)
) -> ShowUser:
    """
    Добавляем историю пользователя
    Args:
        body:список ссылок пользователя [str]
    Returns:
        Возвращает результат запроса
    """
    await _create_new_history_user(body, db)
    return BaseResponseModel(status="ok")


@user_router.get("/visited_domains", response_model=VisitedDomains,
                 status_code=200)
async def visited_domains(
        from_time: Optional[int] = None,
        to_time: Optional[int] = None,
        page_num: Optional[int] = None,
        page_size: Optional[int] = None,
        db: AsyncSession = Depends(get_db)
):
    """
    Получаем уникальные url посещений пользователя
    Args:
        from_time: временной промежуток истории запроса от
        to_time: временной промежуток истории запроса до
    Returns:
        Возвращает уникальные url за это время
    """
    if not page_num or page_num <= 0:
        page_num = 1
    if not page_size or page_size <= 0:
        page_size = 100
    try:
        history_user = await _get_history_user(from_time, to_time, page_num,
                                               page_size, db)
        return VisitedDomains(domains=history_user,
                              status="ok")
    except Exception:
        raise HTTPException(status_code=400, detail="Ошибка в формате данных")
