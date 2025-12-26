

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
