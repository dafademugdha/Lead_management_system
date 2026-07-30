from models.schemas import Lead
from services.lead_service import create_new_lead

lead = Lead(
    name="Amit Sharma",
    mobile_number="9999999999",
    nearest_city="Nagpur",
    land_size=10,
    budget=1500000
)


response = create_new_lead(lead)

print(response)