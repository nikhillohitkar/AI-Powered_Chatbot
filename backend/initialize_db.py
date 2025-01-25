import mysql.connector

# Database connection configuration
db_config = {
    'user': 'your_user',  # Replace with your MySQL username
    'password': 'your_password',  # Replace with your MySQL password
    'host': 'localhost',  # Use 'localhost' if running MySQL locally
    'database': 'your_database'  # The name of your database
}

# SQL query to create the tables
create_tables_query = """
CREATE TABLE IF NOT EXISTS suppliers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    contact_info TEXT
);

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2),
    supplier_id INT,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
);
"""

# Function to create the tables
def initialize_database():
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Execute the create tables query
        cursor.execute(create_tables_query)
        print("Tables created successfully!")

        # Commit the changes
        connection.commit()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    initialize_database()
