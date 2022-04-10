from pydantic.main import BaseModel


class Website(BaseModel):
    url: str
