import requests
import json

payload = {}
headers = {
'Authorization': 'Token 8b01a36e2edca539b7d6c258d0b8211a4197784ffef2722fbc24b38c2f7cd2ae',
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
    result = json.loads(response.text)

    return result

#get_allFlag()

#Funzione GET per tutte le challenge
def get_challenges():
    url = "http://vpn.projectwork2.cyberhackademy.it:8000/api/v1/challenges"
    
    response = requests.request("GET", url, headers=headers, data = payload)
    #print(response.text.encode('utf8'))
    result = json.loads(response.text)

    return result

#get_challenges()

#Funzione per la Scoreboard dei top 10 utenti
def get_scoreboard():
    url = "http://vpn.projectwork2.cyberhackademy.it:8000/api/v1/scoreboard"

    response = requests.request("GET", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))
    result = json.loads(response.text)

#get_scoreboard()


#Forse è quasi inutile
def get_award(user_id):
    url = "http://vpn.projectwork2.cyberhackademy.it:8000/api/v1/users​/"+user_id+"/awards"

    response = requests.request("GET", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))
    result = json.loads(response.text)

#Funzione per prendere l'id delle flag nelle challenge
def get_idFlag(challenge_id):
    url = "http://vpn.projectwork2.cyberhackademy.it:8000/api/v1/challenges/"+str(challenge_id)+"/flags"

    response = requests.request("GET", url, headers=headers, data = payload)
    #print(response.text.encode('utf8'))
    result = json.loads(response.text)
    if result['success'] == True:
        #Dichiaro un array per salvare più flag
        #flag_id=[]
        for flag in result['data']:
           #flag_id.append(flag['id'])
           flag_id = flag['id']           
           return flag_id
    else: return False

#get_award()