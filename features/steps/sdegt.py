from behave import *
from ../elements import *

@given('I access "http://www.aliexpress.com/"')
def step_impl(context):
	context.driver.get("http://www.aliexpress.com/")

@given('I search for "iphone"")
def step_imp(context):
	get_element(context.elements, search_field).send_keys("iphone")
	#TODO: Change given to include the search action
	get_element(context.elements.Search_button).click()

@when('I enter the second item in the search results")
def step_imp(context):
	get_elements(context.elements, results_list)[1].click()
	context.driver.switch_to.window(window_handles[1])

@then('I see there are more than 1 piece available')
def step_imp(context):
	quantity_found = get_element(context.elements.product_quantity).split(" ")[0]
	assert(int(quantity_found > 1, "The quantity of items to be bought is less than 1 ({})".format(quantity_found)


"""  Scenario: "As a Customer we want to see if the second Iphone related ad from the second results page from www.aliexpress.com has at least 1 item to be bought."
	Given I access "http://www.aliexpress.com/"
	Given I enter "Iphone" into the search field
	When I enter the second item in the search results
	Then I see there are more than 1 piece available"""
