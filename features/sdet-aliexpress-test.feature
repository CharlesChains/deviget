Feature: SDET--SG

  Scenario: "As a Customer we want to see if the second Iphone related ad from the second results page from www.aliexpress.com has at least 1 item to be bought."
	Given I access "http://www.aliexpress.com/"
	Given I search for "iphone"
	When I enter the second item in the search results
  	Given  I close the popup
	Then I see there are more than 1 piece available
