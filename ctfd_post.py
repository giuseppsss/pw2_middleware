import requests
import json
from ctfd_req import *
from ctfd_adduser import get_password 

URL_CTFD = "http://ctfd.projectwork2.cyberhackademy.it"

#Funzione per aggiungere un utente su CTFD
def add_userCtfd():
    
    url = ""+URL_CTFD+":8000/api/v1/users"
 
    payload = {
        "name": "utente24", #Aggiungere l'username della dashboard
        "password": get_password(),
        "email": "utente24@prova.it",
        "verified": True,
    }
    headers = {
    'Authorization': 'Token d901c4c649f2438eced8f185e5e784eeec813e793a4fefa7bea33551688dbe50',
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
                return challenge['id']
    return False

#check_challenges("PrimaCh","Challenge1")

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
    url = ""+URL_CTFD+":8000/api/v1/flags"

    payload = {
        "challenge_id": challenge_id,
        "type": "static",  #Tipo di flag
        "content": flag_content, #Questa è la flag da aggiungere
    }

    headers = {
    'Authorization': 'Token d901c4c649f2438eced8f185e5e784eeec813e793a4fefa7bea33551688dbe50',
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
    url = ""+URL_CTFD+":8000/api/v1/challenges"
    
    payload = {
        "name": name_challenge, #Aggiungere il nome della challenge
        "description": "Inserisci qui la flag", #Aggiungere la descrizione della challenge
        "value": value_challenge, #Aggiungere il valore della challenge 
        "category": category_challenge, #Aggiungere la categoria
        "type": "standard",
        "state": "Visible",  #Modificare in "Hidden" nel caso si vogli aggiungere una challenge non visibile
    }

    headers = {
    'Authorization': 'Token d901c4c649f2438eced8f185e5e784eeec813e793a4fefa7bea33551688dbe50',
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

#Funzione per patchare una flag
def patch_flag(flag_patched, name_challenge, category_challenge):
    
    challenge_id=check_challenges(name_challenge,category_challenge)

    flag_id = get_idFlag(challenge_id)
    print(flag_id)

    url = ""+URL_CTFD+":8000/api/v1/flags/"+str(flag_id)+""
    

    payload = {
        "challenge_id": challenge_id,
        "type": "static",
        "content": flag_patched,
    }

    headers = {
        'Authorization': 'Token d901c4c649f2438eced8f185e5e784eeec813e793a4fefa7bea33551688dbe50',
        'Content-Type': 'application/json'
    }

    #Richiesta PATCH per modificare la flag
    response = requests.request("PATCH", url, headers=headers, data = json.dumps(payload))
    print(response.text.encode('utf8'))
    #IF per verificare se è stata modificata
    result = json.loads(response.text)
    if result['success'] == True:
        return True
    else: return False
    

#patch_flag("ciao2","ProvaCh","Challenge1")

def patch_challenge(challenge_id, patch_nameCh, patch_value, patch_categoryCh):
    
    url = ""+URL_CTFD+":8000/api/v1/challenges/"+str(challenge_id)+""
    

    payload = {

        "name": patch_nameCh,
        "value": patch_value,
        "category": patch_categoryCh,
    }

    headers = {
        'Authorization': 'Token d901c4c649f2438eced8f185e5e784eeec813e793a4fefa7bea33551688dbe50',
        'Content-Type': 'application/json'
    }

    response = requests.request("PATCH", url, headers=headers, data = json.dumps(payload))
    print(response.text.encode('utf8'))
    result = json.loads(response.text)
    if result['success'] == True:
        return True
    else: return False

#patch_challenge(2, "SecondaCh", 12, "Challenge1")

#Funzione per aggiungere gli hint
def add_hints(challenge_id, hint_content, cost_hint):
    
    url = ""+URL_CTFD+":8000/api/v1/hints"

    payload = {

        "type": "standard",
        "challenge_id": challenge_id,
        "content": hint_content,
        "cost": cost_hint,
    }

    headers = {
        'Authorization': 'Token d901c4c649f2438eced8f185e5e784eeec813e793a4fefa7bea33551688dbe50',
        'Content-Type': 'application/json'
    }

    #If per verificare se esistente
    if check_challengeHint(challenge_id,hint_content, cost_hint) == False:
        response = requests.request("POST", url, headers=headers, data = json.dumps(payload))
        #print(response.text.encode('utf8'))
        result = json.loads(response.text)
        if result['success'] == True:
            hint_id = result['data']['id']
            return True
        else: return False

#add_hints(1,"Questa è la seconda hint", 4)

def patch_hint(hint_patched, cost_patched, name_challenge, category_challenge):
    
    challenge_id=check_challenges(name_challenge,category_challenge)

    hint_id = get_idFlag(challenge_id)
    print(hint_id)

    url = ""+URL_CTFD+":8000/api/v1/hints/"+str(hint_id)+""
    
    payload = {
        "challenge_id": challenge_id,
        "cost": cost_patched,
        "type": "static",
        "content": hint_patched,
    }

    headers = {
        'Authorization': 'Token d901c4c649f2438eced8f185e5e784eeec813e793a4fefa7bea33551688dbe50',
        'Content-Type': 'application/json'
    }

    #Richiesta PATCH per modificare la flag
    response = requests.request("PATCH", url, headers=headers, data = json.dumps(payload))
    #print(response.text.encode('utf8'))
    #IF per verificare se è stata modificata
    result = json.loads(response.text)
    if result['success'] == True:
        return True
    else: return False

#patch_hint("Questa è la prima hint", 3, "PrimaChal", "Challenge1")
#add_challenge("SesttimoChallenge",16,"challenge3")