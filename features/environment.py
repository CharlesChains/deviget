from selenium import webdriver
import os


def before_all(context):
	path = ("../deviget/chromedriver/chromedriver")
	os.chmod(path, 0o755)

	context.driver = webdriver.Chrome(executable_path=os.path.realpath(path))

def after_all(context):
	context.driver.quit()
