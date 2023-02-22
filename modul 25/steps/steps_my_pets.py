from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StepsMyPets:
    def get_pets_from_pet_table(self, selenium):
        WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.XPATH, "//tbody/tr")))
        my_pets = selenium.find_elements(By.XPATH, '//tbody/tr')
        return len(my_pets)

    def get_amount_of_pets_from_stats(self, selenium):
        user_statistics = selenium.find_element(By.XPATH, "//div[@class='.col-sm-4 left']")
        user_statistics_text = user_statistics.text
        user_statistics_list = user_statistics_text.split("\n")
        return int(user_statistics_list[1].split()[-1])

    def split_pets_data(self, selenium):
        selenium.implicitly_wait(10)
        all_pets_data_elements = selenium.find_elements(By.CSS_SELECTOR, "tbody>tr>td:not(.smart_cell)")
        all_pets_data_elements_text = []
        for element in all_pets_data_elements:
            all_pets_data_elements_text.append(element.text)
        all_pets_data_elements_split = [all_pets_data_elements_text[x:x + 3] for x in range(0, len(all_pets_data_elements_text), 3)]
        return all_pets_data_elements_split

    def get_unique_pets(self, selenium):
        unique_list = []
        for i in self.split_pets_data(selenium):
            item_exist = False
            for j in unique_list:
                if i == j:
                    item_exist = True
                    break
            if not item_exist:
                unique_list.append(i)
        return unique_list

    def get_pets_images_elements(self, selenium):
        selenium.implicitly_wait(10)
        return selenium.find_elements(By.XPATH, '//tbody/tr/th/img[contains(@src,"data")]')

    def get_pets_names(self, selenium):
        selenium.implicitly_wait(10)
        all_pets_names = selenium.find_elements(By.CSS_SELECTOR, "td:nth-of-type(1)")
        print(type(all_pets_names))
        all_pets_names_text = []
        for element in all_pets_names:
            all_pets_names_text.append(element.text)
        return all_pets_names_text