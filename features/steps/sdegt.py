from behave import *
from elements import aliexpress_elements as elements
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_element(context, by):
	return context.find_element(*by)
def get_elements(context,by):
	return context.find_elements(*by)

@given('I access "http://www.aliexpress.com/"')
def step_impl(context):
	context.driver.get("http://www.aliexpress.com/")

@given('I search for "iphone"')
def step_imp(context):
	get_element(context.driver, elements.search_field).send_keys("iphone")
	get_element(context.driver, elements.search_button).click()

@given("I wait for two seconds")
def step_imp(context):
	import time
	time.sleep(2)

@given('I close the popup')
def step_imp(context):
	from selenium.webdriver.common.keys import Keys
	import time
	time.sleep(5)
	context.driver.find_element_by_css_selector('body').send_keys(Keys.ESCAPE)

@when('I enter the second item in the search results')
def step_imp(context):
	get_elements(context.driver, elements.results_list)[1].click()
	context.driver.switch_to.window(context.driver.window_handles[1])

@then('I see there are more than 1 piece available')
def step_imp(context):
	quantity_found = get_element(context.driver, elements.product_quantity).text.split(" ")[0]
	assert(int(quantity_found) > 1)


@given("I go to the 2nd page")
def step_impl(context):
	context.driver.execute_script("window.scrollTo(0,  document.body.scrollHeight)")
	WebDriverWait(context.driver, 10).until(
		EC.presence_of_element_located((elements.second_page))
	).click()

"""  Scenario: "As a Customer we want to see if the second Iphone related ad from the second results page from www.aliexpress.com has at least 1 item to be bought."
	Given I access "http://www.aliexpress.com/"
	Given I enter "Iphone" into the search field
	When I enter the second item in the search results
	Then I see there are more than 1 piece available"""

