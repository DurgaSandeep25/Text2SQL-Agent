from pydantic import BaseModel, Field
import os

class RequestVerifier(BaseModel):
    is_a_request: str = Field(description="Checks whether the given user request is related to data query")


