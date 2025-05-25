import requests
api_url = 'https://api.api-ninjas.com/v1/quotes'
headers = {"X-Api-Key": "7PK5rcZC+g1tgG+JAd8AHA==yB8EN2L74Qqa9KsH"}

def get_quote():
    response = requests.get(api_url, headers=headers)
    if response.status_code == requests.codes.ok:
        return response.json()[0]
    else:
        return "error"

print(get_quote())