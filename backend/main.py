from fastapi import FastAPI, Query, HTTPException
from backend.models.schemas import Lead
from backend.services.lead_service import create_new_lead, view_all_leads, search_all_leads, edit_lead, remove_lead

app = FastAPI(
    title="Lead Management System",
    version="1.0"
)

@app.get("/leads")
def get_leads():
    return view_all_leads()


@app.post("/leads")
def save_lead(lead: Lead):
    return create_new_lead(lead)

@app.get("/leads/search")
def search(
    name: str = None,
    location: str = None,
    city: str = None,
    mobile: str = None,
    whatsapp: str = None,
    current_farm_status: str = None,
    tech_comfort: str = None,
    nature_interest: str = None,
):
    return search_all_leads(
        name=name,
        location=location,
        city=city,
        mobile=mobile,
        whatsapp=whatsapp,
        current_farm_status=current_farm_status,
        tech_comfort=tech_comfort,
        nature_interest=nature_interest
    )

@app.put("/leads/{lead_id}")
def update_existing_lead(lead_id: int, lead: Lead):
    return edit_lead(lead_id, lead)

@app.delete("/leads/{lead_id}")
def delete_existing_lead(lead_id: int):
    return remove_lead(lead_id)