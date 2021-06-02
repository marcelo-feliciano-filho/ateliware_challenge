from django.test import TestCase
from webbrowser import BaseBrowser
# Automatic tests for this awesome project!


class FunctionalTestCases(TestCase):
    """
    Such class makes functional testes for front-end functionalities, for example pressing search repositories button
    """
    def setUp(self):
        self.browser = BaseBrowser()

