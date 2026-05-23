import pandas as pd
import mysql.connector

# Load dataset
df = pd.read_csv("data/Mall_Customers.csv")

# Rename columns
df.columns = [
    "customer_id",
    "gender",
    "age",
    "annual_income",
    "spending_score"
]

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ashu@0313",
    database="customer_segmentation"
)

cursor = connection.cursor()

# Insert data into table
for _, row in df.iterrows():
    sql_query = """
    INSERT INTO customers
    (customer_id, gender, age, annual_income, spending_score)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        int(row["customer_id"]),
        row["gender"],
        int(row["age"]),
        int(row["annual_income"]),
        int(row["spending_score"])
    )

    cursor.execute(sql_query, values)

# Commit changes
connection.commit()

print("Data inserted successfully!")

# Close connection
cursor.close()
connection.close()