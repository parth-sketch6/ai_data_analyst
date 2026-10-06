from data_loader import load_data
from query_engine import register_dataframe, execute_query


df = load_data("data/students.csv")

connection = register_dataframe(df, "students")


query = """
SELECT
    Department,
    COUNT(*) AS student_count,
    AVG(GPA) AS average_gpa
FROM students
GROUP BY Department
ORDER BY average_gpa DESC
"""


result = execute_query(connection, query)

if result["success"]:
    print(result["data"])
else:
    print("Query failed:")
    print(result["error"])