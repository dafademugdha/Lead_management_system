from backend.database.crud import create_lead

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