from pydantic import BaseModel, Field, field_validator
from typing import Optional

class Lead(BaseModel):
    name: str
    location: str
    nearest_city: str
    mobile_number: str
    whatsapp_number: str
    land_size: float
    current_farm_status: str
    existing_income: float
    monthly_maintenance_cost: float
    budget: float
    tech_comfort: str
    nature_interest: str

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        value = value.strip()

        if not value:
            raise ValueError("Name cannot be empty.")

        if not value.replace(" ", "").isalpha():
            raise ValueError("Name should contain only letters.")

        return value

    @field_validator("mobile_number")
    @classmethod
    def validate_mobile(cls, value):
        value = value.strip()

        if not value.isdigit():
            raise ValueError("Mobile number should contain only digits.")

        if len(value) != 10:
            raise ValueError("Mobile number must be exactly 10 digits.")

        return value

    @field_validator("nearest_city")
    @classmethod
    def validate_city(cls, value):
        value = value.strip()

        if not value:
            raise ValueError("Nearest city cannot be empty.")

        return value