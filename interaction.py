from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import threading

# Keep browser open after program finished
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

def money_checker():
        while True:
            cookies = int(driver.find_element(by=By.ID, value="money").text.replace(",", ""))
            all_items_string = ["Cursor", 'Grandma', 'Factory', 'Mine', 'Shipment', 'Alchemy', 'Portal', 'Time']
            items = driver.find_elements(By.CSS_SELECTOR, value="#store b")
            new_items=[]
            for item in items:
                try:
                    new_items.append(int(item.text.split('-')[1].replace(",", "")))
                except:
                    break
            for num in range(len(new_items)):
                if new_items[num] <= cookies <= new_items[num+1] and num!=len(new_items)-1:
                    driver.find_element(by=By.ID, value=f"buy{all_items_string[num]}").click()
                if num==len(new_items)-1 and cookies>=new_items[num]:
                    driver.find_element(by=By.ID, value=f"buy{all_items_string[num]}").click()
            time.sleep(15)

def click():
    while True:
        driver.find_element(By.CSS_SELECTOR, value="#middle #cookie").click()

click_thread = threading.Thread(target=click)
money_checker_thread = threading.Thread(target=money_checker)


money_checker_thread.start()
click_thread.start()




# driver.find_element(By.NAME, value="fName").send_keys("Revanth")
# driver.find_element(By.NAME, value="lName").send_keys("Neelakantham")
# driver.find_element(By.NAME, value="email").send_keys("reva.neelakantham@gmail.com")
# driver.find_element(By.CSS_SELECTOR, value=".form-signin .btn-primary").click()




