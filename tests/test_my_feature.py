import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.driver_factory import get_driver

@pytest.fixture(scope="module")
def setup():
    driver = get_driver()
    yield driver
    driver.quit()

def test_expense_creation(setup):
    driver = setup
    base_page = BasePage(driver)
    
    # Navigate to the web page
    driver.get("https://localhost:7048/expense-grocery")
    
    # Wait for elements to load
    base_page.wait_for_element((By.ID, "expenseDate"))
    base_page.wait_for_element((By.ID, "selectMember"))
    base_page.wait_for_element((By.ID, "selectGrocery"))
    
    # Fill out the expense form
    base_page.input_text((By.ID, "expenseDate"), "2024-02-12")
    base_page.select_dropdown_option_by_text((By.ID, "selectMember"), "Chithra")
    base_page.select_dropdown_option_by_text((By.ID, "selectGrocery"), "Apple - Fruits")
    base_page.input_text((By.ID, "quantity"), "2")
    base_page.input_text((By.ID, "expenseAmount"), "10.50")
    base_page.input_text((By.ID, "expenseDescription"), "Bought apples")
    
    # Submit the expense form
    base_page.click_element((By.ID, "btnAddExpenseSubmit"))
    
    # Wait for success message
    base_page.wait_for_element((By.CLASS_NAME, "toast-success"))
    
    # Assert that the expense was created successfully
    assert "Expense created successfully" in base_page.get_text((By.CLASS_NAME, "toast-body"))

def test_navigation_to_setup_page(setup):
    driver = setup
    base_page = BasePage(driver)

    # Navigate to the Setup page
    driver.get("https://localhost:7048/expense-grocery")
    base_page.click_element((By.LINK_TEXT, "Setup"))

    # Verify that the Setup page is loaded
    assert "Setup" in driver.title

    # Assert the presence of elements on the Setup page
    assert base_page.is_element_present((By.LINK_TEXT, "Brand"))
    assert base_page.is_element_present((By.LINK_TEXT, "Member"))
    assert base_page.is_element_present((By.LINK_TEXT, "Bill Type"))

def test_clear_button_functionality(setup):
    driver = setup
    base_page = BasePage(driver)

    # Navigate to the Expense page
    driver.get("https://localhost:7048/expense-grocery")

    # Fill out some fields
    base_page.input_text((By.ID, "expenseDate"), "2024-02-12")
    base_page.select_dropdown_option_by_text((By.ID, "selectMember"), "Chithra")
    base_page.select_dropdown_option_by_text((By.ID, "selectGrocery"), "Apple - Fruits")
    base_page.input_text((By.ID, "quantity"), "2")
    base_page.input_text((By.ID, "expenseAmount"), "10.50")
    base_page.input_text((By.ID, "expenseDescription"), "Bought apples")

    # Click the Clear button
    base_page.click_element((By.XPATH, "//button[text()='Clear']"))

    # Verify that the fields are cleared
    assert base_page.get_text((By.ID, "expenseDate")) == ""
    assert base_page.get_text((By.ID, "quantity")) == ""
    assert base_page.get_text((By.ID, "expenseAmount")) == ""
    assert base_page.get_text((By.ID, "expenseDescription")) == ""