from test.base_test import login_to_my_pets_page

def test_25_5_1(selenium, login_to_my_pets_page):
    steps_my_pets = login_to_my_pets_page

    # 1. проверяем наличие всех питомцев на странице со списком питомцев
    len_my_pets = steps_my_pets.get_pets_from_pet_table(selenium)
    my_pets_amount_from_user_statistics = steps_my_pets.get_amount_of_pets_from_stats(selenium)
    assert len_my_pets == my_pets_amount_from_user_statistics

    # 2. Хотя бы у половины питомцев есть фото.
    pets_images = steps_my_pets.get_pets_images_elements(selenium)
    len_images = len(pets_images)
    assert len_images >= round(len_my_pets/2)

    # 3. проверяем, что у всех питомцев есть имя, возраст и порода.
    all_pets_data_elements_split = steps_my_pets.split_pets_data(selenium)
    for element in all_pets_data_elements_split:
        assert len(element) == 3

    # 4. проверяем, что у всех питомцев разные имена.
    all_pets_names_text = steps_my_pets.get_pets_names(selenium)
    assert len(all_pets_names_text) == len(set(all_pets_names_text)), "Имена не уникальны"

    # 5. проверяем, что в списке нет повторяющихся питомцев
    unique_list = steps_my_pets.get_unique_pets(selenium)
    assert all_pets_data_elements_split == unique_list, "В списке есть повторяющиеся питомцы"