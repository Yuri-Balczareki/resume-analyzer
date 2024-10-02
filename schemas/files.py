from pydantic import BaseModel 


class FilesSchema(BaseModel):
    file_id: str 
    job_id: str 