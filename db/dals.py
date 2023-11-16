from datetime import datetime
from typing import Optional, Any

from sqlalchemy import select, distinct
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import UserHistory



class UserHistoryDAL:
    """
    Уровень доступа к данным для управления информацией о пользователе
    """

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_history_user(
            self,
            links: list[str]
    ) -> UserHistory:
        """
        Добавляем историю пользователя.
        Args:
        links: Список ссылок пользователя.
        Returns:
        Список ссылок пользователя которые добавились в БД.
        """
        new_history_user = UserHistory(
            link=links
        )
        for link in links:
            self.db_session.add(UserHistory(link=link))
        await self.db_session.flush()
        return new_history_user

    async def get_history_user(
            self,
            from_time: Optional[int],
            to_time: Optional[int],
            page_num: int,
            page_size: int
    ) -> Any:
        """
        Получаем историю пользователя с учетом фильтров и пагинации.
        Args:
        from_time:  Время начала интервала (в формате Unix timestamp).
        to_time: Время окончания интервала (в формате Unix timestamp).
        page: Номер страницы.
        page_size: Размер страницы.
        Returns:
        Список записей истории пользователя.
        """
        stmt = select(distinct(UserHistory.link))

        # обработка фильтров
        if from_time:
            from_datetime = datetime.fromtimestamp(from_time)
            stmt = stmt.where(UserHistory.time_visited >= from_datetime)

        if to_time:
            to_datetime = datetime.fromtimestamp(to_time)
            stmt = stmt.where(UserHistory.time_visited <= to_datetime)
        # настройки пагинация
        offset = (page_num - 1) * page_size
        stmt = stmt.offset(offset).limit(page_size)

        result = await self.db_session.execute(stmt)
        history_user = result.scalars().all()
        return history_user
