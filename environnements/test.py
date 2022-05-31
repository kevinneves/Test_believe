import requests

def appel(API):
    if API == 'reqres':
        req = requests.get('https://reqres.in/api/users/2')
    return req.status_code, req.content

def verif_code(retour_attendu,retour_eu):
    if retour_attendu != retour_eu:
        raise AssertionError(f"Erreur de l'API car elle renvoi {retour_eu} au lieu de {retour_attendu}")

def verif_retour_contenu_reqres(retour):
    if str(retour) != 'b\'{"data":{"id":2,"email":"janet.weaver@reqres.in","first_name":"Janet","last_name":"Weaver","avatar":"https://reqres.in/img/faces/2-image.jpg"},"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}\'':
        print(str(retour))
        raise AssertionError(retour)
    else:
        print('TEST OK')