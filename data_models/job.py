from pydantic import BaseModel


class Job(BaseModel):
    title: str
    company: str
    description: str
    url: str
    location: str
    source: str