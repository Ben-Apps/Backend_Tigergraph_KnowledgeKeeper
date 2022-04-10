from typing import List

from pydantic.main import BaseModel

## Date --> addDat
class Resource(BaseModel):
    url: str
    title: str
    tags: List[str]
    learningDiary: str
    highlights: List[str]
