import requests
import json

payload = {}
headers = {
'Authorization': 'Token af08dd99ce903fe13b593e1053c5b1f331b4dbfe2669c8d1a538143238e17bbd',
'Content-Type': 'application/json'
}

#Funzione GET per tutte le flag risolte da un'utente
def get_solves(user_id):

    url = "http://vpn.projectwork2.cyberhackademy.it:8000/api/v1/users/"+user_id+"/solves"

    response = requests.request("GET", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))

#get_solves(str(2))

#Funzione GET per tutte le flag associate alle challenge
def get_allFlag():
    url = "http://vpn.projectwork2.cyberhackademy.it:8000/api/v1/flags"

    response = requests.request("GET", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))

#Funzione GET per tutte le challenge
def get_challenges():
    url = "http://vpn.projectwork2.cyberhackademy.it:8000/api/v1/challenges"
    
    response = requests.request("GET", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))
    result = json.loads(response.text)

    return result

#get_challenges()