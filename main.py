from environnements.test import *


# Je prepare mon environnement pour tester l'API
# Given
# When ->  J'appel l'API
retourStatus, retourContent = appel('reqres')
# Then -> Je vérifie que l'API renvoi 200
verif_code(200,retourStatus)
# And -> Je vérifie que le contenu correspond
verif_retour_contenu_reqres(retourContent)