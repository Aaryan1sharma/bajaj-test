import requests


def send_initial_request():
    url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
    payload = {
        "name": "Aaryan Sharma",
        "regNo": "0827CS221005",
        "email": "aaryansharma220190@acropoli.in"
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        print("Initial Request Successful!")
        return data['webhook'], data['accessToken']
    except Exception as e:
        print("Failed to send initial request:", e)
        return None, None


def get_question_url(reg_no):
    last_digit = int(reg_no[-1])
    if last_digit % 2 == 0:
        return "https://drive.google.com/file/d/1PO1ZvmDqAZJv77XRYsVben11Wp2HVb/view?usp=sharing"
    else:
        return "https://drive.google.com/file/d/1q8F8g0EpyNzd5BWk-voe5CKbsxoskJWY/view?usp=sharing"


def submit_solution(webhook_url, token, final_sql_query):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    payload = {
        "query": final_sql_query
    }
    try:
        response = requests.post(webhook_url, json=payload, headers=headers)
        response.raise_for_status()
        print(" Success")
        print("Response:", response.json())
    except Exception as e:
        print("Failed", e)


def main():
    
    webhook_url, access_token = send_initial_request()

    if not webhook_url or not access_token:
        print("Terminating due to missing webhook/token.")
        return

    import sqlite3

    def main():
        
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()

        
        cursor.executescript("""
        CREATE TABLE employees (
            employee_id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            date_of_birth TEXT,
            department_id INTEGER
        );

        CREATE TABLE departments (
            department_id INTEGER PRIMARY KEY,
            department_name TEXT
        );

        CREATE TABLE salaries (
            id INTEGER PRIMARY KEY,
            employee_id INTEGER,
            salary INTEGER,
            transaction_date TEXT,
            FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
        );
        """)

        
        cursor.executescript("""
        INSERT INTO departments VALUES 
        (1, 'Engineering'), 
        (2, 'HR'), 
        (3, 'Sales');

        INSERT INTO employees VALUES 
        (101, 'John', 'Doe', '1990-05-10', 1),
        (102, 'Jane', 'Smith', '1985-07-15', 2),
        (103, 'Alice', 'Brown', '1992-03-22', 3);

        INSERT INTO salaries VALUES 
        (1, 101, 50000, '2023-08-15'),
        (2, 101, 70000, '2023-09-01'),  -- on 1st day, should be excluded
        (3, 102, 60000, '2023-08-10'),
        (4, 103, 65000, '2023-09-05');
        """)

        
        cursor.execute("""
        SELECT 
            s.salary AS SALARY,
            e.first_name || ' ' || e.last_name AS NAME,
            strftime('%Y', 'now') - strftime('%Y', e.date_of_birth) AS AGE,
            d.department_name AS DEPARTMENT_NAME
        FROM 
            salaries s
        JOIN 
            employees e ON s.employee_id = e.employee_id
        JOIN 
            departments d ON e.department_id = d.department_id
        WHERE 
            strftime('%d', s.transaction_date) != '01'
        ORDER BY 
            s.salary DESC
        LIMIT 1;
        """)

        
        result = cursor.fetchone()
        if result:
            print(f"SALARY: {result[0]}")
            print(f"NAME: {result[1]}")
            print(f"AGE: {result[2]}")
            print(f"DEPARTMENT_NAME: {result[3]}")
        else:
            print("No valid records found.")

        conn.close()

    if __name__ == "__main__":
        main()


    reg_no = "0827cs221005"
    question_url = get_question_url(reg_no)



    final_sql_query = """
    SELECT * FROM table_name WHERE condition = true;
    """


    submit_solution(webhook_url, access_token, final_sql_query)


if __name__ == "__main__":
    main()
