import requests
import json
from ctfd_req import get_solves
from ctfd_adduser import get_password 
 
def add_userCtfd():
    
    url = "http://34.239.254.174:8000/api/v1/users"
 
    payload = {
        "name": "utente24", #Aggiungere l'username della dashboard
        "password": get_password(),
        "email": "utente24@prova.it", 
        "verified": True,
    }
    headers = {
    'Authorization': 'Token af08dd99ce903fe13b593e1053c5b1f331b4dbfe2669c8d1a538143238e17bbd',
    'Content-Type': 'application/json'
    }  
    
    response = requests.request("POST", url, headers=headers, data = json.dumps(payload))
    print(response.text.encode('utf8'))

    #Primo if per controllare se la richiesta è stata eseguita 
    result = json.loads(response.text)
    print(result['success'])
    if result['success'] == True:
        #Salvare l'id dell'utente
        user_id = result['data']['id']
        print(user_id)
    else :
        print("Utente già inserito")

#get_solves(str(user_id))

add_userCtfd()