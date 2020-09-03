import requests


payload = {}
headers = {
'Authorization': 'Token af08dd99ce903fe13b593e1053c5b1f331b4dbfe2669c8d1a538143238e17bbd',
'Content-Type': 'application/json'
}

def get_solves(user_id):

    url = "http://34.239.254.174:8000/api/v1/users/"+user_id+"/solves"

    response = requests.request("GET", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))