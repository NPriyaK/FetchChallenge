from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time


def setup_driver():
    # Configure Chrome options to keep the browser open after script execution.
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    # Specify the path to ChromeDriver which should match the system architecture.
    service = Service(
        '/Users/nagapriya/Desktop/chromedriver-mac-arm64/chromedriver')
    return webdriver.Chrome(service=service, options=chrome_options)


def weigh(driver, bars_left, bars_right):
    # Wait until the weighing scales' input fields are visible.
    WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, "input[id^='left'], input[id^='right']")))
    # Input the specified bars into the left and right sides of the scale.
    for side, bars in [("left", bars_left), ("right", bars_right)]:
        for bar in bars:
            input_field = driver.find_element(By.ID, f"{side}_{bar}")
            input_field.clear()
            input_field.send_keys(str(bar))
    # Trigger the weigh action and wait for the result.
    driver.find_element(By.ID, "weigh").click()
    time.sleep(2)  # Pause to ensure the result is displayed.
    result = driver.find_element(
        By.XPATH, "//div[@class='result']/button").text
    # Reset the scales for the next weighing.
    driver.find_element(By.XPATH, "//div/button[text()='Reset']").click()
    return result


def divide_and_conquer(driver, bars):
    # Recursively find the fake bar using a divide and conquer strategy.
    if len(bars) == 1:
        return bars[0]
    third = len(bars) // 3
    group1, group2, group3 = bars[:third], bars[third:2*third], bars[2*third:]
    result = weigh(driver, group1, group2)
    if result is None:
        print("Failed to retrieve the result from weigh function.")
        return None
    # Determine the next group to test based on the weighing result.
    if '<' in result:
        return divide_and_conquer(driver, group1)
    elif '>' in result:
        return divide_and_conquer(driver, group2)
    return divide_and_conquer(driver, group3)


def find_fake_bar_and_weighings(driver, bars):
    # Start the process to identify the fake bar.
    fake_bar = divide_and_conquer(driver, bars)
    if fake_bar is not None:
        # Confirm the identified bar and display an alert message.
        driver.find_element(By.ID, f"coin_{fake_bar}").click()
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert_message = alert.text
        alert.accept()
        print("Alert message:", alert_message)
        print("Fake bar identified as bar number:", fake_bar)
    # Collect and display the number of weighings conducted.
    weighing_results = [result.text for result in driver.find_elements(
        By.XPATH, "//div[@class='game-info']//li")]
    print("Number of Weighings:", len(weighing_results))
    print("List of Weighings:", weighing_results)
    return weighing_results


# Main execution: setup the driver, navigate to the game site, find the fake bar, and close the browser.
driver = setup_driver()
driver.get("http://sdetchallenge.fetch.com/")
weighings = find_fake_bar_and_weighings(driver, list(range(9)))
driver.quit()
