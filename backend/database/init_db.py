from database.connection import get_connection


def create_table():

    connection = get_connection()

    if connection is None:
        print("Database connection failed.")
        return

    cursor = connection.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS leads (

        id SERIAL PRIMARY KEY,

        name VARCHAR(100) NOT NULL,

        mobile_number VARCHAR(10) NOT NULL,

        nearest_city VARCHAR(100) NOT NULL,

        land_size FLOAT NOT NULL,

        budget INTEGER NOT NULL

    );
    """

    cursor.execute(create_table_query)

    connection.commit()

    print("Leads table created successfully!")

    cursor.close()
    connection.close()


if __name__ == "__main__":
    create_table()
