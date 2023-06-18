from pages.ecofriendly_page import EcoFriendlyPage


def test_page_title(driver):
    ecofriendly_page = EcoFriendlyPage(driver)
    ecofriendly_page.open()
    assert ecofriendly_page.title.text == "Eco Friendly"


def test_sort_name_descending(driver):
    ecofriendly_page = EcoFriendlyPage(driver)
    ecofriendly_page.open()
    ecofriendly_page.wait_page_loaded()
    ecofriendly_page.sort_by_name()
    ecofriendly_page.wait_page_loaded()
    sorted_items = [item.text for item in ecofriendly_page.find_all_items]
    assert sorted(sorted_items) == sorted_items


def test_sort_name_ascending(driver):
    ecofriendly_page = EcoFriendlyPage(driver)
    ecofriendly_page.open()
    ecofriendly_page.wait_page_loaded()
    ecofriendly_page.sort_by_name()
    ecofriendly_page.sort_ascending_order()
    ecofriendly_page.wait_page_loaded()
    sorted_items = [item.text for item in ecofriendly_page.find_all_items]
    assert sorted(sorted_items, reverse=True) == sorted_items
