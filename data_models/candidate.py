from pydantic import BaseModel

class Candidate(BaseModel):
    name: str
    email: str
    skills: list[str]
    years_experience: int
    preferred_locations: list[str]
    preferred_titles: list[str]