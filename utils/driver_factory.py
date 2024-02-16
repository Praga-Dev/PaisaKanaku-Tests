from selenium import webdriver

def get_driver():
    options = webdriver.ChromeOptions()
	
	#this is optional to have, 
    options.add_argument("--headless")  # Headless mode for running tests without opening browser window
    
    driver = webdriver.Chrome(options=options)
    return driver