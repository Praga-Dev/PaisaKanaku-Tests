import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
from utils.driver_factory import get_driver

@pytest.fixture(scope="module")
def setup():
    driver = get_driver()
    yield driver
    driver.quit()
def testExpenseCreation(setup):
    driver = setup
    base_page = BasePage(driver)

    # Navigate to the expense product web page
    driver.get("https://localhost:7048/expense-product")
    # Wait for element to load
    base_page.wait_for_element((By.ID, "expenseDate"))

    # Fill out the expense product form
    base_page.input_text((By.ID, "expenseDate"), "02-02-2020")
    test = Select(driver.find_element(By.ID,'selectMember'))
    test.select_by_index(1)
    testValue= test.first_selected_option

    base_page.select_dropdown_option_by_text((By.ID,"selectProduct"),"New")
    base_page.wait_for_element((By.ID,"name"))
    # Verify the Dropdown is present or not,after click New as Create Product
    if testValue.is_selected()==False:
        assert False
    else:
        assert True
    # Fill out Create Product
    base_page.input_text((By.ID,"name"),'Parthi')
    base_page.input_text((By.ID,"description"),'Having Some Content in the Description')
    base_page.input_text((By.ID,"price"),'120000')
    base_page.select_dropdown_option_by_text((By.ID,"selectProductCategory"),'Medical')
    base_page.select_drop_option_by_index((By.ID,"selectBrand"),0)
    base_page.select_drop_option_by_index((By.ID,"selectTimePeriod"),0)
    base_page.click_element((By.ID,"btnSaveProductSubmit"))
    ProductAmount=base_page.input_text((By.ID,"Amount"))
    # Verify the product amount is present,after create product form submission
    if ProductAmount.is_enabled()==True:
        assert True
    else:
        assert False
    Quantity=base_page.click_element((By.ID,"quantity"))
    # Verify the quantity is present,after create product form submission
    if Quantity.is_enabled() == True:
        assert True
    else:
        assert False
    ExpenseAmount=base_page.click_element((By.ID,"expenseAmount"))
    # Verify the product expense amount is present,after create product form submission
    if ExpenseAmount.is_enabled() == True:
        assert True
    else:
        assert False
    # Expense Creation form submission
    base_page.click_element((By.ID,'btnAddExpenseSubmit'))
    # Verify form submitted pass or fail
    try:
        testData=base_page.get_text((By.XPATH,"//p[normalize-space()='Praga']"))
    except:
        assert False
    if testData == 'Praga':
        assert True



