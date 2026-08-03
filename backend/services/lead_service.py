from backend.database.crud import create_lead, get_all_leads, search_leads, update_lead, delete_lead

def create_new_lead(lead):

    result = create_lead(lead)

    if result:
        return {
            "status": "success",
            "message": "Lead saved successfully"
        }

    return {
        "status": "error",
        "message": "Failed to save lead"
    }
    
def view_all_leads():
    leads = get_all_leads()

    result = []

    for lead in leads:
        result.append({
        "id": lead[0],
        "name": lead[1],
        "location": lead[2],
        "nearest_city": lead[3],
        "mobile_number": lead[4],
        "whatsapp_number": lead[5],
        "land_size": lead[6],
        "current_farm_status": lead[7],
        "existing_income": lead[8],
        "monthly_maintenance_cost": lead[9],
        "budget": lead[10],
        "tech_comfort": lead[11],
        "nature_interest": lead[12]
        })

    return result

def search_all_leads(name=None, city=None, mobile=None):

    leads = search_leads(name, city, mobile)

    result = []

    for lead in leads:
        result.append({
        "id": lead[0],
        "name": lead[1],
        "location": lead[2],
        "nearest_city": lead[3],
        "mobile_number": lead[4],
        "whatsapp_number": lead[5],
        "land_size": lead[6],
        "current_farm_status": lead[7],
        "existing_income": lead[8],
        "monthly_maintenance_cost": lead[9],
        "budget": lead[10],
        "tech_comfort": lead[11],
        "nature_interest": lead[12]
        })

    return result

def edit_lead(lead_id, lead):

    updated = update_lead(lead_id, lead)

    if updated:
        return {
            "status": "success",
            "message": "Lead updated successfully"
        }

    return {
        "status": "error",
        "message": "Lead not found"
    }
    
def remove_lead(lead_id):

    deleted = delete_lead(lead_id)

    if deleted:
        return {
            "status": "success",
            "message": "Lead deleted successfully"
        }

    return {
        "status": "error",
        "message": "Lead not found"
    }