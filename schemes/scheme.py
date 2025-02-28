from datetime import date

from pydantic import BaseModel, field_validator, model_validator, Field


class User(BaseModel):
    login: str = Field(default="auto")
    password: str = Field(default="auto")
    role: int = Field(default=1)

class AuthUser(BaseModel):
    login: str = Field(default="auto")
    password: str = Field(default="auto")

class Role(BaseModel):
    name: str = Field(default="auto")
    level: int = Field(default=1)

class ResponseRole(BaseModel):
    id: int = Field(default=1)
    name: str = Field(default="auto")
    level: int = Field(default=1)


class Student(BaseModel):
    id: int
    name: str 
    b_date: date
    
    @field_validator("name", mode="before")
    def balidate_name(cls, v):
        if isinstance(v, str):
            return v
        elif isinstance(v, int):
            return str(v)
        else:
            raise ValueError("name must be str or int")


    @model_validator(mode="after")
    def validate_age(self):
        
        today = date.today()
        
        age = today.year - self.b_date.year - (
            (today.month, today.day) < (self.b_date.month, self.b_date.day)
        ) 
        
        if age < 18:
            raise ValueError("user must be over 18")
        elif age > 118:
            raise ValueError("user must be under 18")
        else:
            return self
        
    @model_validator(mode="after")
    def validate_name(self):
        if self.name.strip() == "":
            self.name = f"User_{self.id}"
        else:
            self
    
    
    
if __name__ == "__main__":
    petr = Student(
        id=1,
        name="Petr",
        b_date=date(year=2004, month=5, day=6)
    )
    
    # print(petr)
    # print(type(petr.model_dump()))
    # print(type(petr.model_dump_json()))
    
    
    oleg_dict = {
        "id": 2,
        "name":  "",
        "b_date": "2002-01-01"
    }
    
    oleg = Student(**oleg_dict)
    
    print(oleg.model_dump())