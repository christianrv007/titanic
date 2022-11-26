from pydantic import BaseModel

class requestParameters(BaseModel):
    """this class validate the parameters with pydantic"""
    pclass: int
    name: str
    sex: str
    age: str
    sibsp: int
    parch: int
    ticket: str
    fare: str
    cabin: str
    embarked: str
    boat: str
    body: str


class response(BaseModel):
    """this class validate the response with pydantic"""
    prediction: int
    message: str