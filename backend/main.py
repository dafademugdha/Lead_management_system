from backend.models.schemas import Lead
from backend.services.lead_service import create_new_lead


def save_lead(name, mobile, city, land_size, budget):

    lead = Lead(
        name=name,
        mobile_number=mobile,
        nearest_city=city,
        land_size=land_size,
        budget=budget
    )

    return create_new_lead(lead)