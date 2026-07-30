from pydantic import BaseModel, Field, field_validator

class Lead(BaseModel):
    name: str = Field(..., min_length=2)
    mobile_number: str
    nearest_city: str
    land_size: float = Field(..., gt=0)
    budget: int = Field(..., gt=0)

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