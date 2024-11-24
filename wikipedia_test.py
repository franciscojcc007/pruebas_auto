import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import HtmlTestRunner


# Crear carpeta para capturas de pantalla si no existe
os.makedirs("screenshots", exist_ok=True)

class TestWikipedia(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver_path = r"C:\Users\francisco javier\OneDrive\Escritorio\edgedriver_win64\msedgedriver.exe"
        service = Service(driver_path)
        cls.driver = webdriver.Edge(service=service)
        cls.driver.maximize_window()
        
# **abrir la página principal de wikipedia correctamente**
    def test_01_home_page(self):
        self.driver.get("https://www.wikipedia.org/")
        self.driver.save_screenshot("screenshots/home_page.png")
        self.assertIn("Wikipedia", self.driver.title, "La página principal no contiene 'Wikipedia' en el título.")
      
 # **Realizar una búsqueda en inglés**
    def test_02_search_english(self):
      self.driver.get("https://www.wikipedia.org/")
      search_box = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "searchInput"))
      )
      search_box.send_keys("Selenium (software)")
      search_box.send_keys(Keys.RETURN)
      WebDriverWait(self.driver, 10).until(
        EC.title_contains("Selenium")
      )
      self.assertIn("Selenium", self.driver.title, "La página de búsqueda en inglés no contiene el título esperado.")
      self.driver.save_screenshot("screenshots/search_english.png")

 # **Cambiar idioma a español y realizar búsqueda**
    def test_03_search_spanish(self):
        self.driver.get("https://www.wikipedia.org/")
        search_box = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "search"))
        )
        search_box.send_keys("Selenium (software)")
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)
        self.assertIn("Selenium", self.driver.title, "La página de búsqueda en español no contiene el título esperado.")
        self.driver.save_screenshot("screenshots/search_spanish.png")

 # ** Navegar a la página inicial desde el idioma español usado el logo de la misma**
    def test_04_navigate_home_spanish(self):
        self.driver.find_element(By.CLASS_NAME, "mw-logo").click()
        time.sleep(2)
        self.assertIn("Wikipedia, la enciclopedia libre", self.driver.page_source, "No se redirigió correctamente a la página inicial en español.")
        self.driver.save_screenshot("screenshots/home_page_spanish.png")
        
  # **Validar navegación en la barra oriental de Wikipedia**
    def test_05_navigate_discussion(self):
        self.driver.get("https://es.wikipedia.org/")
        discusion_link = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Discusión"))
        )
        discusion_link.click()
        self.assertIn("discusión", self.driver.title, "La página no se redirigió a la sección 'Discusión'.")
        self.driver.save_screenshot("screenshots/discusion_section.png")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

# Generación del reporte HTML 
if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="reportes",
            report_title="Reporte de Pruebas Automatizadas - Wikipedia",
            descriptions="Resultados de las pruebas realizadas en la página de Wikipedia.",
        )
    )



