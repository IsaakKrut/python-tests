import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://isaakkrut.ca")
        self.assertIn("Isaak Krut", driver.title)
        heading = driver.find_element(By.ID, "heading")
        self.assertEqual("Isaak Krut", heading.text)

        form_name = driver.find_element(By.ID, "name")
        form_email = driver.find_element(By.ID, "email")
        form_message = driver.find_element(By.ID, "message")
        form_name.send_keys("Python Selenium Name")
        form_email.send_keys("python_selenium@example.com")
        form_message.send_keys("Message from Python Selenium")

        submit_button = driver.find_element(By.ID, "sendMessage")
        driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        time.sleep(1)
        submit_button.click()

        confirmation = driver.find_element(By.ID, "messageSent")
        self.assertEqual("Message is sent. Expect a reply soon!", confirmation.text)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
