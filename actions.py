from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def action(driver, id, action, requestType, text=""):
    try:
        # Using WebDriverWait to wait for the element to load 
        element = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.ID, id))
        )

        # React differently for every action type
        if action == "text":
            # doing CTRL + A command for selecting all text in input element and replace it with determined text
            actions = ActionChains(driver)
            actions.move_to_element_with_offset(element, 0, 0).click().perform()
            actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
            element.send_keys(text)
        elif action == "getStatus":
            print("Loading ... ")
            time.sleep(3)
            return element.text
        elif action == "getText":
            print(f"{element.text}\n")
        elif action == "click":
            element.click()
        elif action == "select":
            requestTypeDic = {
                1: "POST",
                2: "GET",
                3: "PUT",
                4: "DELETE",
            }
            # select the select element in web using selenium package
            Select(element).select_by_value(requestTypeDic.get(int(requestType)))
        else:
            print(f'Masukkan action yang benar')
    except Exception as e:
        print(f'Terjadi Kesalahan: {str(e)}')
