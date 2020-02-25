from selenium import webdriver

def before_all(context):
	path = "../chromedriver"

	context.driver = webdriver.Chrome(path
	)

def after_all(context):
	context.driver.quit()
