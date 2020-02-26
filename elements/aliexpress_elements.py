from selenium.webdriver.common.by import By


results_list = (By.CSS_SELECTOR, 'a[class="item-title"]')
product_quantity = (By.CSS_SELECTOR, 'div[class="product-quantity-tip"]')
search_button = (By.CSS_SELECTOR, 'input[type="submit"]')
search_field = (By.ID, 'search-cate')
popup = (By.CSS_SELECTOR, 'div[class*="closeable"]')
popup_cross = (By.CSS_SELECTOR, 'a[role="button"]')
second_page = (By.CSS_SELECTOR, 'button[aria-label*="Page 2"]')