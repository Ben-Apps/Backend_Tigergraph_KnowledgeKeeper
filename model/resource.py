from datetime import datetime
from typing import List, Optional
from pydantic.main import BaseModel

class Resource(BaseModel):
    id: Optional[int]
    url: str
    user: Optional[str]
    title: str
    tags: List[str]
    notes: str
    highlights: List[str]
    type: Optional[str]
    domain: Optional[str]
    date: Optional[datetime]
