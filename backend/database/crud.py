from database.connection import get_connection


def create_lead(lead):

    connection = get_connection()

    if connection is None:
        return False


    cursor = connection.cursor()


    lead_data = lead.model_dump()


    query = """
    INSERT INTO leads
    (name, mobile_number, nearest_city, land_size, budget)
    VALUES (%s, %s, %s, %s, %s);
    """


    cursor.execute(
        query,
        (
            lead_data["name"],
            lead_data["mobile_number"],
            lead_data["nearest_city"],
            lead_data["land_size"],
            lead_data["budget"]
        )
    )


    connection.commit()


    cursor.close()
    connection.close()


    return True