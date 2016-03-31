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
        self.browser.find_element_by_id('linkLogin').click()

        correoElectronico = self.browser.find_element_by_id('correoElectronico')
        correoElectronico.send_keys('pacho5@buscoayuda.com')

        contrasenia = self.browser.find_element_by_id('contrasenia')
        contrasenia.send_keys('clave1234')

        self.browser.find_element_by_id('butLogin').click()

        self.browser.implicitly_wait(5)
        try:
            h6 = self.browser.find_element_by_xpath("//h6[text()='Bienvenido']")
        except:
            h6 = self.browser.find_element_by_xpath("//h6[text()='Bienvenido']")

        self.assertIn('Bienvenido', h6.text)

    def test_update(self):
        self.browser.get('http://localhost:8000')
        self.browser.find_element_by_id('linkLogin').click()

        correoElectronico = self.browser.find_element_by_id('correoElectronico')
        correoElectronico.send_keys('pacho5@buscoayuda.com')

        contrasenia = self.browser.find_element_by_id('contrasenia')
        contrasenia.send_keys('clave1234')

        self.browser.find_element_by_id('butLogin').click()

        self.browser.implicitly_wait(15)
        try:
            self.browser.find_element_by_id('linkPerfil').click()
        except:
            self.browser.find_element_by_id('linkPerfil').click()

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.clear()
        nombre.send_keys('Sandra')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.clear()
        apellidos.send_keys('Perez')

        aniosExperiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        aniosExperiencia.clear()
        aniosExperiencia.send_keys('6')

        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.clear()
        telefono.send_keys('322222')

        self.browser.find_element_by_xpath("//input[@value='Actualizar']").click()

        self.browser.implicitly_wait(5)
        p = self.browser.find_element_by_xpath("//p[text()='Sandra Perez']")

        self.assertIn('Sandra Perez', p.text)

    def test_comentarios(self):
        self.browser.get('http://localhost:8000')
        self.browser.find_element_by_xpath("//p[text()='Francisco Saenz']").click()

        self.browser.implicitly_wait(5)
        self.browser.find_element_by_id('butComentario').click()

        correoElectronico = self.browser.find_element_by_id('correoElectronico')
        correoElectronico.send_keys('test@test.com')

        comentario = self.browser.find_element_by_id('comentario')
        comentario.clear()
        comentario.send_keys('Esto es una prueba de comentario.')

        self.browser.find_element_by_id('butComentarioAgregar').click()

        self.browser.implicitly_wait(5)
        b = self.browser.find_element_by_xpath("//b[text()='test@test.com:']")

        self.assertIn('test@test.com:', b.text)


    def test_busqueda(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('linkRegistrarse')
        link.click()

        nombre = self.browser.find_element_by_id('nombre')
        nombre.send_keys('Kata')

        apellidos = self.browser.find_element_by_id('apellidos')
        apellidos.send_keys('TDD02')

        self.browser.implicitly_wait(3)
        self.browser.find_element_by_xpath("//select[@id='idServicio']/option[text()='PINTURA']").click()

        aniosExperiencia = self.browser.find_element_by_id('aniosExperiencia')
        aniosExperiencia.send_keys('3')

        telefono = self.browser.find_element_by_id('telefono')
        telefono.send_keys('3333333')

        correoElectronico = self.browser.find_element_by_id('correoElectronico')
        correoElectronico.send_keys('kata@buscoayuda.com')

        contrasenia = self.browser.find_element_by_id('contrasenia')
        contrasenia.send_keys('clave1234')

        foto = self.browser.find_element_by_id('foto')
        foto.send_keys('http://es.fakenamegenerator.com/images/sil-male.png')

        botonGuardar = self.browser.find_element_by_id('butGuardar')
        botonGuardar.click()

        self.browser.implicitly_wait(5)

        self.browser.find_element_by_xpath("//select[@id='idFiltro']/option[text()='PRUEBAS']").click()
        p = self.browser.find_element_by_xpath("//p[text()='Kata TDD02']")

        self.assertIn('', p.text)

