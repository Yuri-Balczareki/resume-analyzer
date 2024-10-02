from pydantic import BaseModel 


class ResumeSchema(BaseModel): 
    id: str 
    job_id: str 
    content: str 
    opnion: str # Given by the LLM model 
    file_path: str 