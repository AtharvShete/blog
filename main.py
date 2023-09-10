from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Function to perform the blog search on CFI
def search_cfi_blog(search_query, tag_filter, club_filter):
    # Initialize the web driver (Change the path to your webdriver)
    driver = webdriver.Chrome()

    # Navigate to the CFI website
    driver.minimize_window()
    driver.get("https://cfi.iitm.ac.in/blog")

    try:
        # Locate the search input field and enter the search query
        search_input = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "search")))
        search_input.clear()
        search_input.send_keys(search_query)
        search_input.send_keys(Keys.RETURN)
        search_input.send_keys(Keys.ESCAPE)
        search_input.send_keys(Keys.ESCAPE)

        # Wait for search results to load
        time.sleep(2)

        # Apply tag filter (if specified)
        if tag_filter:
            tag_filter_element = driver.find_element(By.XPATH, "//input[@id='tag-filter']")
            tag_filter_element.send_keys(tag_filter)
            tag_filter_element.send_keys(Keys.ARROW_DOWN)
            tag_filter_element.send_keys(Keys.RETURN)
            tag_filter_element.send_keys(Keys.ESCAPE)
            tag_filter_element.send_keys(Keys.ESCAPE)
            
            time.sleep(2)

        # Apply club filter (if specified)
        if club_filter:
            club_filter_element = driver.find_element(By.XPATH, "//input[@id='club-filter']")
            club_filter_element.send_keys(club_filter)
            club_filter_element.send_keys(Keys.ARROW_DOWN)
            club_filter_element.send_keys(Keys.RETURN)
            club_filter_element.send_keys(Keys.ESCAPE)
            club_filter_element.send_keys(Keys.ESCAPE)
            time.sleep(2)

        # Find and click on the first search result (best match)
        search_result = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiCard-root css-5vr80q'])[1]")))
        search_result.click()

        # Print the title and URL of the blog
        blog_title = driver.find_element(By.CSS_SELECTOR, ".MuiTypography-root.MuiTypography-h3.css-r6km21").text
        blog_url = driver.current_url
        print("Blog Title:", blog_title)
        print("Blog URL:", blog_url)

    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        # Close the web driver
        driver.quit()

# Input from the user
search_query = input("Enter the blog search query: ")
tag_filter = input("Enter the tag filter (or leave blank): ")
club_filter = input("Enter the club filter (or leave blank): ")

# Call the function to search and open the best match blog
search_cfi_blog(search_query, tag_filter, club_filter)
