from pydantic import BaseModel, Field

class MessegeSchema(BaseModel):
    message: str = Field(...)
    class Config:
        json_schema_extra={
            "message": "Messege",
        }