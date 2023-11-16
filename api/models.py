from pydantic import BaseModel

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
    links: list[str]


class LinksPost(BaseModel):
    links: list[str]


class ShowHistoryUser(TunedModel):
    links: list[str]


class BaseResponseModel(BaseModel):
    status: str


class VisitedDomains(BaseResponseModel):
    domains: list[str]
