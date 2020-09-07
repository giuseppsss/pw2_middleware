import requests
import json
from ctfd_req import *
from ctfd_adduser import get_password 


#Funzione per aggiungere un utente su CTFD
def add_userCtfd():
    
    url = "http://vpn.projectwork2.cyberhackademy.it:8000/api/v1/users"
 
    payload = {
        "name": "utente24", #Aggiungere l'username della dashboard
        "password": get_password(),
        "email": "utente24@prova.it", 
        "verified": True,
    }
    headers = {
    'Authorization': 'Token 8b01a36e2edca539b7d6c258d0b8211a4197784ffef2722fbc24b38c2f7cd2ae',
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
        #print(user_id)
    else :
        print("Utente già inserito")

#get_solves(str(user_id))
#add_userCtfd()

#Funzione per controllare se la challenge esiste
def check_challenges(name_challenge, category_challenge):

    result=get_challenges()
    if result['success'] == True:
        for challenge in result['data']: 
            if challenge['name'] == name_challenge and challenge['category'] == category_challenge:
                return True
    return False

check_challenges("PrimaCh","Challenge1")

#Funzione per verificare se la flag già esiste
def check_flag(challenge_id, flag_content):
    
    result=get_allFlag()
    if result['success'] == True:
        for challenge in result['data']: 
           if challenge['challenge_id'] == challenge_id and challenge['content'] == flag_content:
                return True
    return False

#Funzione per aggiungere una flag
def add_flag(challenge_id, flag_content):
    url = "http://vpn.projectwork2.cyberhackademy.it:8000/api/v1/flags"

    payload = {
        "challenge_id": challenge_id,
        "type": "static",  #Tipo di flag
        "content": flag_content, #Questa è la flag da aggiungere
    }

    headers = {
    'Authorization': 'Token 8b01a36e2edca539b7d6c258d0b8211a4197784ffef2722fbc24b38c2f7cd2ae',
    'Content-Type': 'application/json'
    }  

    if check_flag(challenge_id, flag_content) == False:
        response = requests.request("POST", url, headers=headers, data = json.dumps(payload))
        #print(response.text.encode('utf8'))
        return True
    else: return False

#add_flag(1,"ciao1")

#Funzione per aggiungere una nuova challenge 
def add_challenge(name_challenge, value_challenge, category_challenge): 
    url = "http://vpn.projectwork2.cyberhackademy.it:8000/api/v1/challenges"
    
    payload = {
        "name": name_challenge, #Aggiungere il nome della challenge
        "description": "Inserisci qui la flag", #Aggiungere la descrizione della challenge
        "value": value_challenge, #Aggiungere il valore della challenge 
        "category": category_challenge, #Aggiungere la categoria
        "type": "standard",
        "state": "Visible", 
    }

    headers = {
    'Authorization': 'Token 8b01a36e2edca539b7d6c258d0b8211a4197784ffef2722fbc24b38c2f7cd2ae',
    'Content-Type': 'application/json'
    }  
    
    if check_challenges(name_challenge, category_challenge) == False:
        response = requests.request("POST", url, headers=headers, data = json.dumps(payload))
        print(response.text.encode('utf8'))
        result = json.loads(response.text)
        #print(result['success'])
        if result['success'] == True:
        #Salvare l'id della challenge
            challenge_id = result['data']['id']
            add_flag(challenge_id, "ciao5") 
    else: print("Challenge già esistente")

#add_challenge("SesttimoChallenge",16,"challenge3")