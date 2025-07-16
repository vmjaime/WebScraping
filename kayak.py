from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

opts = Options()

opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=opts
)

# URL de búsqueda real (Quito → Madrid hoy)
driver.get("https://www.kayak.com.ec/flights/UIO-MAD/2025-07-16")


sleep(3)
precios=driver.find_elements(By.XPATH, '//div[@data-testid="esgW-price"]')
for precio in precios:
    print(precio.text)