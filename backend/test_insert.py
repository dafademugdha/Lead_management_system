from models.schemas import Lead
from database.crud import create_lead


lead = Lead(
    name="Rahul Patil",
    mobile_number="9876543210",
    nearest_city="Pune",
    land_size=5.5,
    budget=800000
)


result = create_lead(lead)


print(result)