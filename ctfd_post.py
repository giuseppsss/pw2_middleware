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
#add_userCtfd()

#Funzione per convertire le stringhe in liste
def split_str(s):
    return list(s)

#Funzione per controllare se la challenge esiste
def check_challenges(name_challenge, category_challenge):
 #Da errore di tipo sul secondo if. Da risolvere se si vuole implementare nella funzione add_challenge

    #Provavo a convertire in lista le variabili, ma da sempre errore
    #name_challenge = split_str(name)
    #category_challenge = split_str(category)
    #print(name_challenge,category_challenge)

    result=get_challenges()
    if result['success'] == True:
        if result['data']['name'] == name_challenge and result['data']['category'] == category_challenge:
            print("La challenge già esiste")
        else: print("La challenge si può aggiungere")


#check_challenges("PrimaCh","Challenge1")

#Funzione per aggiungere una flag
def add_flag(challenge_id, flag_content):
    url = "http://vpn.projectwork2.cyberhackademy.it:8000/api/v1/flags"

    payload = {
        "challenge_id": challenge_id,
        "type": "static",  #Tipo di flag
        "content": flag_content, #Questa è la flag da aggiungere
    }

    headers = {
    'Authorization': 'Token af08dd99ce903fe13b593e1053c5b1f331b4dbfe2669c8d1a538143238e17bbd',
    'Content-Type': 'application/json'
    }  
    response = requests.request("POST", url, headers=headers, data = json.dumps(payload))
    print(response.text.encode('utf8'))

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
    'Authorization': 'Token af08dd99ce903fe13b593e1053c5b1f331b4dbfe2669c8d1a538143238e17bbd',
    'Content-Type': 'application/json'
    }  
    
    #check_challenges(name_challenge, category_challenge)
    response = requests.request("POST", url, headers=headers, data = json.dumps(payload))
    print(response.text.encode('utf8'))

    #If per vedere se la challenge è stata aggiunta
    result = json.loads(response.text)
    print(result['success'])
    if result['success'] == True:
        #Salvare l'id della challenge
        challenge_id = result['data']['id']
        add_flag(challenge_id, "ciao5") 
    #else commentato perchè non viene mai eseguito, anche se già c'è una challenge con lo stesso 
    # nome, nella categoria e con la stessa flag viene aggiunta un'altra challenge con l'id successivo
    #else : print("Challenge non aggiunta")
    #SOLUZIONE:if prima di fare la POST per la challenge in cui si richiama check_challenges e si vede 
    #          se quella challenge esiste già


#add_challenge()