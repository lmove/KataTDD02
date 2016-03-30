from unittest import TestCase
from selenium import webdriver

class KataTDD02Test(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_register(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('linkRegistrarse')
        link.click()

        nombre = self.browser.find_element_by_id('nombre')
        nombre.send_keys('Francisco')

        apellidos = self.browser.find_element_by_id('apellidos')
        apellidos.send_keys('Saenz')

        self.browser.implicitly_wait(3)
        self.browser.find_element_by_xpath("//select[@id='idServicio']/option[text()='Pintura']").click()

        aniosExperiencia = self.browser.find_element_by_id('aniosExperiencia')
        aniosExperiencia.send_keys('4')

        telefono = self.browser.find_element_by_id('telefono')
        telefono.send_keys('3111111')

        correoElectronico = self.browser.find_element_by_id('correoElectronico')
        correoElectronico.send_keys('pacho5@buscoayuda.com')

        contrasenia = self.browser.find_element_by_id('contrasenia')
        contrasenia.send_keys('clave1234')

        foto = self.browser.find_element_by_id('foto')
        foto.send_keys('http://es.fakenamegenerator.com/images/sil-male.png')

        botonGuardar = self.browser.find_element_by_id('butGuardar')
        botonGuardar.click()

        self.browser.implicitly_wait(30)
        p = self.browser.find_element_by_xpath("//p[text()='Francisco Saenz']")

        self.assertIn('Francisco Saenz', p.text)


    def test_view_detail(self):
        self.browser.get('http://localhost:8000')
        self.browser.implicitly_wait(30)
        p = self.browser.find_element_by_xpath("//p[text()='Francisco Saenz']")
        p.click()

        nombre = self.browser.find_element_by_id('nombreCompleto')

        self.assertIn('Francisco Saenz', nombre.text)

    def test_sesion(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('linkLogin')
        link.click()

        correoElectronico = self.browser.find_element_by_id('correoElectronico')
        correoElectronico.send_keys('pacho5@buscoayuda.com')

        contrasenia = self.browser.find_element_by_id('contrasenia')
        contrasenia.send_keys('clave1234')

        botonLogin = self.browser.find_element_by_id('butLogin')
        botonLogin.click()

        self.browser.implicitly_wait(10)
        h6 = self.browser.find_element_by_xpath("//h6[text()='Bienvenido']")

        self.assertIn('Bienvenido', h6.text)


    def test_update(self):
        self.browser.get('http://localhost:8000')
        self.browser.find_element_by_id('linkLogin').click()

        correoElectronico = self.browser.find_element_by_id('correoElectronico')
        correoElectronico.send_keys('pacho5@buscoayuda.com')

        contrasenia = self.browser.find_element_by_id('contrasenia')
        contrasenia.send_keys('clave1234')

        botonLogin = self.browser.find_element_by_id('butLogin')
        botonLogin.click()

        self.browser.implicitly_wait(10)
        self.browser.find_element_by_id('linkPerfil').click()

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Sandra')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Perez')

        aniosExperiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        aniosExperiencia.send_keys('6')

        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('322222')

        botonActualizar = self.browser.find_element_by_id('butActualizar')
        botonActualizar.click()

        self.browser.implicitly_wait(10)
        p = self.browser.find_element_by_xpath("//p[text()='Sandra Perez']")

        self.assertIn('Sandra Perez', p.text)