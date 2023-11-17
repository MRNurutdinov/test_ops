from fastapi import HTTPException
from pydantic import BaseModel, validator

"""
БЛОК С МОДЕЛЯМИ API
"""


class TunedModel(BaseModel):
    class Config:
        """Сообщает pydantic преобразовать даже не dict obj в json"""

        orm_mode = True


class ShowUser(TunedModel):
    domains: list[str]


class UserHistoryCreate(BaseModel):
    links: list

    @validator('links')
    def validate_links(cls, links):
        if len(links) == 0:
            raise HTTPException(status_code=400, detail="Пустой список")
        if (
                not isinstance(links, list)
                or not all(isinstance(link, str) for link in links)
        ):
            raise HTTPException(status_code=400, detail="Некорректный формат данных. Ожидается список строк.")
        return links


class LinksPost(BaseModel):
    links: list[str]


class ShowHistoryUser(TunedModel):
    links: list[str]


class BaseResponseModel(BaseModel):
    status: str


class VisitedDomains(BaseResponseModel):
    domains: list[str]
