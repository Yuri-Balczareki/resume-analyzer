from pydantic import BaseModel 
from typing import List 


class AnalysisSchema(BaseModel): 
    id: str 
    job_id: str 
    resume_id: str 
    name: str 
    skills: List[str]
    education: List[str]
    language: List[str]
    score: float # Given by the LLM model
    