import requests
import json

payload = {}
headers = {
'Authorization': 'Token d901c4c649f2438eced8f185e5e784eeec813e793a4fefa7bea33551688dbe50',
'Content-Type': 'application/json'
}

URL_CTFD = "http://ctfd.projectwork2.cyberhackademy.it"

#Funzione GET per il numero di flag risolte da un'utente
def get_userSolves(user_id):
    
    url = ""+URL_CTFD+":8000/api/v1/users/"+str(user_id)+"/solves"

    response = requests.request("GET", url, headers=headers, data = payload)
    #print(response.text.encode('utf8'))
    result = json.loads(response.text)
    
    correct=0

    if result['success'] == True:
        for challenge_id in result['data']:
            correct+=1    
    return correct

#Funzione GET per tutte le flag associate alle challenge
def get_allFlag():
    url = ""+URL_CTFD+":8000/api/v1/flags"

    response = requests.request("GET", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))
    result = json.loads(response.text)

    return result

#Funzione GET per tutte le challenge
def get_challenges():
    url = ""+URL_CTFD+":8000/api/v1/challenges"
    
    response = requests.request("GET", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))
    result = json.loads(response.text)

    return result

#Funzione per la Scoreboard dei top 10 utenti
def get_scoreboard():
    url = ""+URL_CTFD+":8000/api/v1/scoreboard"

    response = requests.request("GET", url, headers=headers, data = payload)
    #print(response.text.encode('utf8'))
    result = json.loads(response.text)
    return result


#Forse è quasi inutile perchè non funziona
def get_award(user_id):
    url = ""+URL_CTFD+":8000/api/v1/users​/"+str(user_id)+"/awards"

    response = requests.request("GET", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))
    #result = json.loads(response.text)


#Funzione per prendere l'id delle flag nelle challenge
def get_idFlag(challenge_id):
    url = ""+URL_CTFD+":8000/api/v1/challenges/"+str(challenge_id)+"/flags"

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

#Funzione GET tutte le hint
def get_hints():
    url = ""+URL_CTFD+":8000/api/v1/hints"

    response = requests.request("GET", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))
    #result = json.loads(response.text)

#Funzione per vedere se la Hint esiste
def check_challengeHint(challenge_id, hint_content, cost_hint):
    url = ""+URL_CTFD+":8000/api/v1/challenges/"+str(challenge_id)+"/hints"
    
    response = requests.request("GET", url, headers=headers, data = payload)
    #print(response.text.encode('utf8'))
    result= json.loads(response.text)

    if result['success'] == True:
        for hint in result['data']: 
            if hint['content'] == hint_content and hint['cost'] == cost_hint:
                #print("La hint già esiste\n")
                return True
    #print("Puoi aggiungere la hint")
    return False

#Funzione per prenderesi l'id dell'Hint
def get_idHint(challenge_id):
    url = ""+URL_CTFD+":8000/api/v1/challenges/"+str(challenge_id)+"/hints"

    response = requests.request("GET", url, headers=headers, data = payload)
    #print(response.text.encode('utf8'))
    result = json.loads(response.text)
    if result['success'] == True:
        #Dichiaro un array per salvare più flag
        #flag_id=[]
        for hint in result['data']:
           #flag_id.append(flag['id'])
           hint_id = hint['id']           
           return hint_id
    else: return False

#Funzione GET per tutte le flag risolte da un'utente
def get_solves(user_id):
    
    url = ""+URL_CTFD+":8000/api/v1/users/"+str(user_id)+"/solves" 
 
    response = requests.request("GET", url, headers=headers, data = payload) 
    #print(response.text.encode('utf8')) 
    result = json.loads(response.text) 
    return result

#Funzione GET per il punteggio di ogni utente ma escludendo gli Hint acquistati
def get_score(user_id):
    score_user = 0

    result = get_userSolves(user_id)
    if result['success'] == True:
        for challenge in result['data']:
            score_user += int(challenge['challenge']['value'])
        #print(score_user)
    return score_user

#Funzione GET per il punteggio di ogni utente considerando gli Hint acquistati
def get_userScore(user_id):
    result=get_scoreboard()
    score_user = 0
    if result['success'] == True:
        for user in result['data']:
            if user['account_id'] == user_id:
                score_user += int(user['score'])
    return score_user
