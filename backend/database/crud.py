from backend.database.connection import get_connection
from backend.models.schemas import Lead


def create_lead(lead):

    connection = get_connection()

    if connection is None:
        return False

    cursor = connection.cursor()

    lead_data = lead.model_dump()

    query = """
    INSERT INTO leads
    (
        name,
        location,
        nearest_city,
        mobile_number,
        whatsapp_number,
        land_size,
        current_farm_status,
        existing_income,
        monthly_maintenance_cost,
        budget,
        tech_comfort,
        nature_interest
    )
    VALUES
    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

    cursor.execute(
        query,
        (
            lead_data["name"],
            lead_data["location"],
            lead_data["nearest_city"],
            lead_data["mobile_number"],
            lead_data["whatsapp_number"],
            lead_data["land_size"],
            lead_data["current_farm_status"],
            lead_data["existing_income"],
            lead_data["monthly_maintenance_cost"],
            lead_data["budget"],
            lead_data["tech_comfort"],
            lead_data["nature_interest"]
        )
    )

    connection.commit()

    cursor.close()
    connection.close()

    return True

def get_all_leads(): 
    conn = get_connection() 
    cursor = conn.cursor() 
    cursor.execute("""
    SELECT
        id,
        name,
        location,
        nearest_city,
        mobile_number,
        whatsapp_number,
        land_size,
        current_farm_status,
        existing_income,
        monthly_maintenance_cost,
        budget,
        tech_comfort,
        nature_interest
        FROM leads
        ORDER BY id;
    """) 
    leads = cursor.fetchall() 
    cursor.close() 
    conn.close() 
    return leads

def search_leads(
    name=None,
    location=None,
    city=None,
    mobile=None,
    whatsapp=None,
    current_farm_status=None,
    tech_comfort=None,
    nature_interest=None
):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT
    id,
    name,
    location,
    nearest_city,
    mobile_number,
    whatsapp_number,
    land_size,
    current_farm_status,
    existing_income,
    monthly_maintenance_cost,
    budget,
    tech_comfort,
    nature_interest
    FROM leads
    WHERE 1=1
    """

    values = []

    if name:
        query += " AND name ILIKE %s"
        values.append(f"%{name}%")

    if city:
        query += " AND nearest_city ILIKE %s"
        values.append(f"%{city}%")

    if mobile:
        query += " AND mobile_number = %s"
        values.append(mobile)
        
    if location:
        query += " AND location ILIKE %s"
        values.append(f"%{location}%")

    if whatsapp:
        query += " AND whatsapp_number = %s"
        values.append(whatsapp)

    if current_farm_status:
        query += " AND current_farm_status ILIKE %s"
        values.append(f"%{current_farm_status}%")

    if tech_comfort:
        query += " AND tech_comfort ILIKE %s"
        values.append(f"%{tech_comfort}%")

    if nature_interest:
        query += " AND nature_interest ILIKE %s"
        values.append(f"%{nature_interest}%")

    query += " ORDER BY id;"

    cursor.execute(query, values)

    leads = cursor.fetchall()

    cursor.close()
    conn.close()

    return leads

def update_lead(lead_id, lead):

    conn = get_connection()

    if conn is None:
        return False

    cursor = conn.cursor()

    query = """
    UPDATE leads
    SET
        name = %s,
        location = %s,
        nearest_city = %s,
        mobile_number = %s,
        whatsapp_number = %s,
        land_size = %s,
        current_farm_status = %s,
        existing_income = %s,
        monthly_maintenance_cost = %s,
        budget = %s,
        tech_comfort = %s,
        nature_interest = %s
    WHERE id = %s;
    """

    cursor.execute(
        query,
        (
            lead.name,
            lead.location,
            lead.nearest_city,
            lead.mobile_number,
            lead.whatsapp_number,
            lead.land_size,
            lead.current_farm_status,
            lead.existing_income,
            lead.monthly_maintenance_cost,
            lead.budget,
            lead.tech_comfort,
            lead.nature_interest,
            lead_id
        )
    )

    conn.commit()

    updated = cursor.rowcount

    cursor.close()
    conn.close()

    return updated

def delete_lead(lead_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM leads
        WHERE id = %s
        """,
        (lead_id,)
    )

    conn.commit()

    deleted = cursor.rowcount

    cursor.close()
    conn.close()

    return deleted