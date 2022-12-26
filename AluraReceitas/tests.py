
#from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


path = './chromedriver'


class AluraReceitasTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=path)

    def tearDown(self):
        self.browser.quit()

    def test_abre_janela_do_chrome(self):
        paginaIniciall = self.browser.get(self.live_server_url + '/')
        self.browser.find_element(By.CLASS_NAME, 'header__menu__cadastro').click()
        sleep(2)

    def test_clica_em_cadastro(self):
        
        self.browser.find_element(By.CLASS_NAME, 'header__menu__cadastro').click()

    


