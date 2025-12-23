#1. Guarantees valid JSON

#2. Acts as contract between agents

#3. Enables automatic retries when output is invalid
# from pydantic import BaseModel, Field

# class UserProfile(BaseModel):
#     name: str = Field(description="Full name")
#     age: int = Field(description="Age in years")
#     email: str = Field(description="Email address")
#     country: str = Field(description="Country name")

# for dynamic Clumn Schema and then number of rows
from pydantic import BaseModel
from typing import List, Optional

class ColumnSchema(BaseModel):
    name: str
    type: str
    description: Optional[str] = None
    values: Optional[List[str]] = None

class DatasetSchema(BaseModel):
    dataset_type: str
    columns: List[ColumnSchema]
