
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
        #self.browser.quit()
        pass



    def test_cria_um_novo_usuario_e_entra_no_login(self):

        # Acessando a página
        self.browser.get(self.live_server_url + '/')
        navbarCadastro = self.browser.find_element(By.XPATH, '//div[@class="classynav"]/ul/li/a[text()="Cadastro"]').text
        self.assertEqual('CADASTRO', navbarCadastro)

        # Acessando o cadastro
        self.browser.find_element(By.XPATH, '//div[@class="classynav"]/ul/li/a[text()="Cadastro"]').click()

        # Formulario do Cadastro
        self.browser.find_element(By.XPATH, '//input[@type="text" ][@class="form-control"][@name="nome"]').send_keys('Nome Teste')
        self.browser.find_element(By.XPATH, '//input[@type="email" ][@class="form-control"][@name="email"]').send_keys('teste@testes.com.br')
        self.browser.find_element(By.XPATH, '//input[@type="password" ][@class="form-control"][@name="password"]').send_keys('senhaDoTeste12345')
        self.browser.find_element(By.XPATH, '//input[@type="password" ][@class="form-control"][@name="password2"]').send_keys('senhaDoTeste12345')

        # Criando a conta em si
        self.browser.find_element(By.XPATH, '//button[@class="btn btn-success" ][@type="submit"]').click()


        # Formulario do Login
        self.browser.find_element(By.XPATH, '//input[@type="text" ][@class="form-control"][@name="email"]').send_keys('teste@testes.com.br')
        self.browser.find_element(By.XPATH, '//input[@type="password" ][@class="form-control"][@name="senha"]').send_keys('senhaDoTeste12345')

        # Entrando em sua conta
        self.browser.find_element(By.XPATH, '//button[@class="btn btn-success" ][@type="submit"]').click()

        status = 'y'
        
        print('\n\n')
        while status == 'y':
            status = str(input('Continue? '))


    def test_usuario_entrando_na_sua_conta(self):
        # Acessando a página
        self.browser.get(self.live_server_url + '/')
        navbarCadastro = self.browser.find_element(By.XPATH, '//div[@class="classynav"]/ul/li/a[text()="Login"]').text
        self.assertEqual('LOGIN', navbarCadastro)

        # Acessando o login
        self.browser.find_element(By.XPATH, '//div[@class="classynav"]/ul/li/a[text()="Login"]').click()
        
        
        # Formulario do Login
        self.browser.find_element(By.XPATH, '//input[@type="text" ][@class="form-control"][@name="email"]').send_keys('teste@testes.com.br')
        self.browser.find_element(By.XPATH, '//input[@type="password" ][@class="form-control"][@name="senha"]').send_keys('senhaDoTeste12345')

        # Entrando em sua conta
        self.browser.find_element(By.XPATH, '//button[@class="btn btn-success" ][@type="submit"]').click()

        status = 'y'
        
        print('\n\n')
        while status == 'y':
            status = str(input('Continue? '))


    


