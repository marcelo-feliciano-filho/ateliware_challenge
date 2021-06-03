from django.test import TestCase
from selenium import webdriver
# Automatic tests for this awesome project!


class FunctionalTestCases(TestCase):
    """
    Such class makes functional testes for front-end functionalities, for example pressing search repositories button
    """
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_home_page(self):
        """
        This test homepage oppening process
        """
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Encontrar Repositórios Destaques em: CSS, HTML, Python, JS, Flutter', self.browser.page_source)

    def test_search_btn(self):
        """
        This test is responsible by emulating a single language repository search by User
        """
        pass


class UnitTestCases(TestCase):
    """
    UnitTestCases tests back-end functionalities to assure front-end operations, for exemple:
    Database tests;

    """

    def test_home_template(self):
        """
        Makes a test to validate template
        """
        pass

    def test_database(self):
        """
        Tests database connection by selecting all values from a table
        """
        pass

    def test_git_api_init(self):
        """
        This test will open GitHub API and test random requisition
        """
        pass
