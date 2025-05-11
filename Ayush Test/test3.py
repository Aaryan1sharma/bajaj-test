import requests


sql_query = """SELECT s.salary AS SALARY, e.first_name || ' ' || e.last_name AS NAME, 
strftime('%Y', 'now') - strftime('%Y', e.date_of_birth) AS AGE, 
d.department_name AS DEPARTMENT_NAME FROM salaries s 
JOIN employees e ON s.employee_id = e.employee_id 
JOIN departments d ON e.department_id = d.department_id 
WHERE strftime('%d', s.transaction_date) != '01' 
ORDER BY s.salary DESC LIMIT 1;"""

def send_startup_webhook():
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

        access_token = data.get("accessToken")
        webhook_url = data.get("webhook")

        if not access_token or not webhook_url:

            return

        print("Webhook generated successfully!")
        print("accessToken:", access_token)
        print("webhook:", webhook_url)

        # Now send the final SQL query to the webhook
        submit_final_query(access_token, webhook_url)

    except requests.exceptions.RequestException as e:
        print(" Error ", e)

def submit_final_query(access_token, webhook_url):
    headers = {
        "Authorization": access_token,
        "Content-Type": "application/json"
    }

    body = {
        "finalQuery": sql_query
    }

    try:
        response = requests.post(webhook_url, headers=headers, json=body)
        response.raise_for_status()
        print(" Final query submitted ")
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)
    except requests.exceptions.RequestException as e:
        print(" Error ", e)


if _name_ == "_main_":
    send_startup_webhook()