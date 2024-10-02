from pydantic import BaseModel 


class JobSchema(BaseModel):
    id: str 
    name: str 
    main_activities: str 
    prerequisites: str 
    differentials: str 
    