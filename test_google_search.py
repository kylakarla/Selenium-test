from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_diuosaoidas():
    # Seadistada Firefoxi veebibrauser
    driver = webdriver.Firefox()

    # Avada Google'i veebileht
    driver.get("https://www.google.com")

    # Oodata, et leht oleks laetud
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    try:
        # Oodata ja leida "Reject All" nupp
        reject_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[text()="Reject all"]'))
        )
        reject_button.click()  # Klõpsata "Reject All" nuppu
        print("Cookie consent rejected.")
    except Exception as e:
        print("Cookie consent button not found or already rejected.")

    # Leida otsingukast
    search_box = driver.find_element(By.NAME, "q")

    # Sisestada otsingupäring ja vajutage Enter
    search_box.send_keys("Selenium Python tutorial")
    search_box.send_keys(Keys.RETURN)

    # Oodata tulemuste laadimist
    time.sleep(2)

    # Näidata esimesi tulemusi 
    search_results = driver.find_elements(By.XPATH, '//h3')
    for result in search_results[:5]:  # Näidata ainult 5 esimest tulemust
        print(result.text)

    # Close
    driver.quit()

if __name__ == "__main__":
    main()
