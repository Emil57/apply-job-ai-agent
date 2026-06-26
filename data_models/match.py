from pydantic import BaseModel
from job import Job

class Match(BaseModel):
    job: Job
    score: int
    reasoning: str