from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from decouple import config

class TestAppContato(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()


    def test_username_indefinido_em_campo_obrigatorio(self):
        driver = self.driver
        driver.get(config('TEST_URL_REGISTRO'))
        assert "Formulário de registro" in driver.find_element_by_css_selector('h2.text-white').text
        user = driver.find_element_by_name("username")
        user.clear()
        user.send_keys(" ")
        nome = driver.find_element_by_name("nome")
        nome.clear()
        nome.send_keys("dionnys nome")
        senha = driver.find_element_by_name("senha")
        senha.clear()
        senha.send_keys(config('TEST_PASSWORD'))
        email = driver.find_element_by_id("id_email")
        email.clear()
        email.send_keys("email@edu.br")
        minibio = driver.find_element_by_name("bio")
        minibio.clear()
        minibio.send_keys("Essa é uma mensagem de bio")
        driver.find_element_by_xpath("/html/body/main/div[2]/form").submit()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "p.invalid-feedback strong")))
        self.assertTrue(driver.find_element(By.CSS_SELECTOR, "p.invalid-feedback strong").text == 'Este campo é obrigatório.')


    def test_nome_obrigatorio(self):
        driver = self.driver
        driver.get(config('TEST_URL_REGISTRO'))
        assert "Formulário de registro" in driver.find_element_by_css_selector('h2.text-white').text
        user = driver.find_element_by_name("username")
        user.clear()
        user.send_keys("dionnysfffiiii")
        nome = driver.find_element_by_name("nome")
        nome.clear()
        senha = driver.find_element_by_name("senha")
        senha.clear()
        senha.send_keys(config('TEST_PASSWORD'))
        email = driver.find_element_by_name("email")
        email.clear()
        email.send_keys("email@edu.br")
        minibio = driver.find_element_by_name("bio")
        minibio.clear()
        minibio.send_keys("Essa é uma mensagem de bio")
        driver.find_element_by_xpath("/html/body/main/div[2]/form").submit()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "p.invalid-feedback strong")))
        self.assertTrue(driver.find_element(By.CSS_SELECTOR, "p.invalid-feedback strong").text == 'Este campo é obrigatório.')


    def test_senha_obrigatoria(self):
        driver = self.driver
        driver.get(config('TEST_URL_REGISTRO'))
        assert "Formulário de registro" in driver.find_element_by_css_selector('h2.text-white').text
        user = driver.find_element_by_name("username")
        user.clear()
        user.send_keys("dionnysfffffhhhh")
        nome = driver.find_element_by_name("nome")
        nome.clear()
        nome.send_keys("dionnys nome")
        senha = driver.find_element_by_name("senha")
        senha.clear()
        email = driver.find_element_by_name("email")
        email.clear()
        email.send_keys("email@edu.br")
        minibio = driver.find_element_by_name("bio")
        minibio.clear()
        minibio.send_keys("Essa é uma mensagem de bio")
        driver.find_element_by_xpath("/html/body/main/div[2]/form").submit()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "p.invalid-feedback strong")))
        self.assertTrue(driver.find_element(By.CSS_SELECTOR, "p.invalid-feedback strong").text == 'Este campo é obrigatório.')


    def test_email_obrigatorio(self):
        driver = self.driver
        driver.get(config('TEST_URL_REGISTRO'))
        assert "Formulário de registro" in driver.find_element_by_css_selector('h2.text-white').text
        user = driver.find_element_by_name("username")
        user.clear()
        user.send_keys("dionnysffffggggg")
        nome = driver.find_element_by_name("nome")
        nome.clear()
        nome.send_keys("dionnys nome")
        senha = driver.find_element_by_name("senha")
        senha.clear()
        senha.send_keys(config('TEST_PASSWORD'))
        email = driver.find_element_by_name("email")
        email.clear()
        minibio = driver.find_element_by_name("bio")
        minibio.clear()
        minibio.send_keys("Essa é uma mensagem de bio")
        driver.find_element_by_xpath("/html/body/main/div[2]/form").submit()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "p.invalid-feedback strong")))
        self.assertTrue(driver.find_element(By.CSS_SELECTOR, "p.invalid-feedback strong").text == 'Este campo é obrigatório.')


    def test_minibio_obrigatorio(self):
        driver = self.driver
        driver.get(config('TEST_URL_REGISTRO'))
        assert "Formulário de registro" in driver.find_element_by_css_selector('h2.text-white').text
        user = driver.find_element_by_name("username")
        user.clear()
        user.send_keys("dionnysfffffeeeee")
        nome = driver.find_element_by_name("nome")
        nome.clear()
        nome.send_keys("dionnys nome")
        senha = driver.find_element_by_name("senha")
        senha.clear()
        senha.send_keys(config('TEST_PASSWORD'))
        email = driver.find_element_by_name("email")
        email.clear()
        email.send_keys("email@edu.br")
        minibio = driver.find_element_by_name("bio")
        minibio.clear()
        minibio.send_keys("Essa é uma mensagem de bio")
        driver.find_element_by_xpath("/html/body/main/div[2]/form").submit()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "p.invalid-feedback strong")))
        self.assertTrue(driver.find_element(By.CSS_SELECTOR, "p.invalid-feedback strong").text == 'Este campo é obrigatório.')


    def test_deve_exibir_email_invalido_gmail(self):
        driver = self.driver
        driver.get(config('TEST_URL_REGISTRO'))
        assert "Formulário de registro" in driver.find_element_by_css_selector('h2.text-white').text
        user = driver.find_element_by_name("username")
        user.clear()
        user.send_keys("dionnysffffffffdddddd")
        nome = driver.find_element_by_name("nome")
        nome.clear()
        nome.send_keys("dionnys nome")
        senha = driver.find_element_by_name("senha")
        senha.clear()
        senha.send_keys(config('TEST_PASSWORD'))
        email = driver.find_element_by_name("email")
        email.clear()
        email.send_keys("email@gmail.br")
        minibio = driver.find_element_by_name("bio")
        minibio.clear()
        minibio.send_keys("Essa é uma mensagem de bio")
        driver.find_element_by_xpath("/html/body/main/div[2]/form").submit()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "p.invalid-feedback strong")))
        self.assertTrue(driver.find_element(By.CSS_SELECTOR, "p.invalid-feedback strong").text == 'Você deve preencher ocm um e-mail válido.')

    def test_deve_exibir_email_invalido_hotmail(self):
        driver = self.driver
        driver.get(config('TEST_URL_REGISTRO'))
        assert "Formulário de registro" in driver.find_element_by_css_selector('h2.text-white').text
        user = driver.find_element_by_name("username")
        user.clear()
        user.send_keys("dionnysffffffffdddddd")
        nome = driver.find_element_by_name("nome")
        nome.clear()
        nome.send_keys("dionnys nome")
        senha = driver.find_element_by_name("senha")
        senha.clear()
        senha.send_keys(config('TEST_PASSWORD'))
        email = driver.find_element_by_name("email")
        email.clear()
        email.send_keys("email@hotmail.br")
        minibio = driver.find_element_by_name("bio")
        minibio.clear()
        minibio.send_keys("Essa é uma mensagem de bio")
        driver.find_element_by_xpath("/html/body/main/div[2]/form").submit()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "p.invalid-feedback strong")))
        self.assertTrue(driver.find_element(By.CSS_SELECTOR, "p.invalid-feedback strong").text == 'Você deve preencher ocm um e-mail válido.')

    def test_deve_exibir_email_outlook(self):
        driver = self.driver
        driver.get(config('TEST_URL_REGISTRO'))
        assert "Formulário de registro" in driver.find_element_by_css_selector('h2.text-white').text
        user = driver.find_element_by_name("username")
        user.clear()
        user.send_keys("dionnysffffffffdddddd")
        nome = driver.find_element_by_name("nome")
        nome.clear()
        nome.send_keys("dionnys nome")
        senha = driver.find_element_by_name("senha")
        senha.clear()
        senha.send_keys(config('TEST_PASSWORD'))
        email = driver.find_element_by_name("email")
        email.clear()
        email.send_keys("email@outlook.br")
        minibio = driver.find_element_by_name("bio")
        minibio.clear()
        minibio.send_keys("Essa é uma mensagem de bio")
        driver.find_element_by_xpath("/html/body/main/div[2]/form").submit()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "p.invalid-feedback strong")))
        self.assertTrue(driver.find_element(By.CSS_SELECTOR, "p.invalid-feedback strong").text == 'Você deve preencher ocm um e-mail válido.')

    def test_deve_exibir_email_live(self):
        driver = self.driver
        driver.get(config('TEST_URL_REGISTRO'))
        assert "Formulário de registro" in driver.find_element_by_css_selector('h2.text-white').text
        user = driver.find_element_by_name("username")
        user.clear()
        user.send_keys("dionnysffffffffdddddd")
        nome = driver.find_element_by_name("nome")
        nome.clear()
        nome.send_keys("dionnys nome")
        senha = driver.find_element_by_name("senha")
        senha.clear()
        senha.send_keys(config('TEST_PASSWORD'))
        email = driver.find_element_by_name("email")
        email.clear()
        email.send_keys("email@live.br")
        minibio = driver.find_element_by_name("bio")
        minibio.clear()
        minibio.send_keys("Essa é uma mensagem de bio")
        driver.find_element_by_xpath("/html/body/main/div[2]/form").submit()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "p.invalid-feedback strong")))
        self.assertTrue(driver.find_element(By.CSS_SELECTOR, "p.invalid-feedback strong").text == 'Você deve preencher ocm um e-mail válido.')

    def test_deve_exibir_email_none(self):
        driver = self.driver
        driver.get(config('TEST_URL_REGISTRO'))
        assert "Formulário de registro" in driver.find_element_by_css_selector('h2.text-white').text
        user = driver.find_element_by_name("username")
        user.clear()
        user.send_keys("dionnysffffffffdddddd")
        nome = driver.find_element_by_name("nome")
        nome.clear()
        nome.send_keys("dionnys nome")
        senha = driver.find_element_by_name("senha")
        senha.clear()
        senha.send_keys(config('TEST_PASSWORD'))
        email = driver.find_element_by_name("email")
        email.clear()
        email.send_keys("email@qualquer.br")
        minibio = driver.find_element_by_name("bio")
        minibio.clear()
        minibio.send_keys("Essa é uma mensagem de bio")
        driver.find_element_by_xpath("/html/body/main/div[2]/form").submit()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "p.invalid-feedback strong")))
        self.assertTrue(driver.find_element(By.CSS_SELECTOR, "p.invalid-feedback strong").text == 'Você deve preencher ocm um e-mail válido.')

    def test_nao_pode_caracter_especial_username(self):
        driver = self.driver
        driver.get(config('TEST_URL_REGISTRO'))
        assert "Formulário de registro" in driver.find_element_by_css_selector('h2.text-white').text
        url_form = driver.current_url
        user = driver.find_element_by_name("username")
        user.clear()
        user.send_keys("dionnysffffff7777#")
        nome = driver.find_element_by_name("nome")
        nome.clear()
        nome.send_keys("dionnys nome")
        senha = driver.find_element_by_name("senha")
        senha.clear()
        senha.send_keys("senha235455")
        email = driver.find_element_by_name("email")
        email.clear()
        email.send_keys("email@edu.br")
        minibio = driver.find_element_by_name("bio")
        minibio.clear()
        minibio.send_keys("Essa é uma mensagem de bio")
        driver.find_element_by_xpath("/html/body/main/div[2]/form").submit()
        WebDriverWait(driver, 5).until(expected_conditions.url_changes(url_form))
        self.assertTrue(driver.find_element(By.CSS_SELECTOR, "h4.alert-heading").text != 'Muito bem!')


    def test_nao_pode_senha_com_menos_de_8_caracteres(self):
        driver = self.driver
        driver.get(config('TEST_URL_REGISTRO'))
        assert "Formulário de registro" in driver.find_element_by_css_selector('h2.text-white').text
        url_form = driver.current_url
        user = driver.find_element_by_name("username")
        user.clear()
        user.send_keys("dionnysfffff6666")
        nome = driver.find_element_by_name("nome")
        nome.clear()
        nome.send_keys("dionnys nome")
        senha = driver.find_element_by_name("senha")
        senha.clear()
        senha.send_keys(config('TEST_PASSWORD'))
        email = driver.find_element_by_name("email")
        email.clear()
        email.send_keys("email@edu.br")
        minibio = driver.find_element_by_name("bio")
        minibio.clear()
        minibio.send_keys("Essa é uma mensagem de bio")
        driver.find_element_by_xpath("/html/body/main/div[2]/form").submit()
        WebDriverWait(driver, 5).until(expected_conditions.url_changes(url_form))
        self.assertTrue(driver.find_element(By.CSS_SELECTOR, "h4.alert-heading").text != 'Muito bem!')

    def test_nao_pode_usuario_repetido(self):
        driver = self.driver
        driver.get(config('TEST_URL_REGISTRO'))
        assert "Formulário de registro" in driver.find_element_by_css_selector('h2.text-white').text
        url_form = driver.current_url
        user = driver.find_element_by_name("username")
        user.clear()
        user.send_keys("dionnysfffff10")
        nome = driver.find_element_by_name("nome")
        nome.clear()
        nome.send_keys("dionnys nome")
        senha = driver.find_element_by_name("senha")
        senha.clear()
        senha.send_keys(config('TEST_PASSWORD'))
        email = driver.find_element_by_name("email")
        email.clear()
        email.send_keys("email@edu.br")
        minibio = driver.find_element_by_name("bio")
        minibio.clear()
        minibio.send_keys("Essa é uma mensagem de bio")
        driver.find_element_by_xpath("/html/body/main/div[2]/form").submit()
        WebDriverWait(driver, 5).until(expected_conditions.url_changes(url_form))
        self.assertTrue(driver.find_element(By.CSS_SELECTOR, "h4.alert-heading").text == 'Muito bem!')
        driver.get(config('TEST_URL_REGISTRO'))
        assert "Formulário de registro" in driver.find_element_by_css_selector('h2.text-white').text
        user = driver.find_element_by_name("username")
        user.clear()
        user.send_keys("dionnysfffff10")
        nome = driver.find_element_by_name("nome")
        nome.clear()
        nome.send_keys("dionnys nome")
        senha = driver.find_element_by_name("senha")
        senha.clear()
        senha.send_keys(config('TEST_PASSWORD'))
        email = driver.find_element_by_name("email")
        email.clear()
        email.send_keys("email@edu.br")
        minibio = driver.find_element_by_name("bio")
        minibio.clear()
        minibio.send_keys("Essa é uma mensagem de bio")
        driver.find_element_by_xpath("/html/body/main/div[2]/form").submit()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div/div/p[2]")))
        self.assertTrue(driver.find_element(By.XPATH, "/html/body/div/div/p[2]").text == ':(')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
