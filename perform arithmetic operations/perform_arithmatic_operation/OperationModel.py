from pydantic import BaseModel


class OperationModel(BaseModel):
    lfl_first_number: float
    lfl_second_number: float
    lstr_operation: str
