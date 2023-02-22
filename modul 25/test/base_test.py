import pytest

from selenium.webdriver.common.by import By

from steps.steps_my_pets import StepsMyPets


@pytest.fixture
def login_to_my_pets_page(selenium):
    selenium.implicitly_wait(10)
    selenium.get("https://petfriends.skillfactory.ru/")
    btn_newuser = selenium.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]")
    btn_newuser.click()
    btn_exist_acc = selenium.find_element(By.LINK_TEXT, u"У меня уже есть аккаунт")
    btn_exist_acc.click()
    field_email = selenium.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys("reudacriluzo-2903@yopmail.com")

    field_pass = selenium.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys("tSR3pB3StcXTa")

    selenium.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    selenium.find_element(By.CSS_SELECTOR, 'html>body>nav>div>ul >li>a').click()
    return StepsMyPets()