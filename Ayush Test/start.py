import requests

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
        print("Webhook sent please check!")
        print("Response:", response.json())
    except requests.exceptions.RequestException as e:
        print("Error sending webhook:", e)

# Call on startup
if __name__ == "__main__":
    send_startup_webhook()




#"accessToken": "some_token_here",
#  "webhook": "https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON"