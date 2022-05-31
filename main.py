from environnements.test import *
import HtmlTestRunner, unittest


class maclasse(unittest.TestCase):
    @classmethod


    def test_API_reqres(self):
        # Je prepare mon environnement pour tester l'API
        # Given
        # When ->  J'appel l'API
        retourStatus, retourContent = appel('reqres')
        # Then -> Je vérifie que l'API renvoi 200
        verif_code(200,retourStatus)
        # And -> Je vérifie que le contenu correspond
        verif_retour_contenu_reqres(retourContent)

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'), )