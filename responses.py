import requests



def get_response(message: str) -> str:
    p_message = message.lower()

    r = requests.get("https://api.kanye.rest")
    data = r.json()

    if p_message == '!kanye':
        return data["quote"]
    

    