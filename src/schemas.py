from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field, EmailStr, ConfigDict


class ContactModel(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    email: EmailStr | None
    phone: str = Field(max_length=15, pattern=r"^\+?\d{10,15}$")
    birthday: date | None


class ContactResponse(ContactModel):
    id: int
    created_at: Optional[datetime] | None
    updated_at: Optional[datetime] | None
    model_config = ConfigDict(from_attributes=True)


class HealthCheckResponse(BaseModel):
    message: str
