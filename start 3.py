from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
import time
import pandas as pd

# Initialize WebDriver
driver = webdriver.Chrome()

# Initialize an empty list to store profile data
all_profiles_data = []

# Step 1: Request multiple search terms from the user
search_terms = input("Enter search terms separated by commas: ").split(",")

try:
    for term in search_terms:
        # Remove any extra whitespace
        term = term.strip()

        # Go to TikTok's search page and search for each term
        driver.get("https://www.tiktok.com/search/user?lang=en")
        time.sleep(3)

        # Step 2: Locate the search bar and enter the search term
        search_bar = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search']")
        search_bar.clear()
        search_bar.send_keys(term)
        search_bar.send_keys(Keys.RETURN)
        time.sleep(5)

        # Step 3: Collect the first 10 usernames (adjust the range if needed)
        username_elements = driver.find_elements(By.CSS_SELECTOR, "p[data-e2e='search-user-unique-id']")[:10]

        # Iterate over username elements and collect data
        profiles_data = []
        for i in range(len(username_elements)):
            profile_data = {"search_term": term}
            try:
                # Re-find the username element if it's stale
                username_elements = driver.find_elements(By.CSS_SELECTOR, "p[data-e2e='search-user-unique-id']")[:10]
                username_element = username_elements[i]

                # Collect username and click to open profile
                profile_data["username"] = username_element.text
                username_element.click()
                time.sleep(3)

                # Followers count
                try:
                    followers_element = driver.find_element(By.CSS_SELECTOR, "strong[data-e2e='followers-count']")
                    profile_data["followers"] = followers_element.text
                except:
                    profile_data["followers"] = "Followers count not found"

                # Likes count
                try:
                    likes_element = driver.find_element(By.CSS_SELECTOR, "strong[data-e2e='likes-count']")
                    profile_data["likes"] = likes_element.text
                except:
                    profile_data["likes"] = "Likes count not found"

                # Bio text
                try:
                    bio_element = driver.find_element(By.CSS_SELECTOR, "h2[data-e2e='user-bio']")
                    profile_data["bio"] = bio_element.text
                except:
                    profile_data["bio"] = "Bio not found"

                # Bio link
                try:
                    bio_link_element = driver.find_element(By.CSS_SELECTOR, "a[data-e2e='user-link']")
                    profile_data["bio_link"] = bio_link_element.get_attribute("href")
                except:
                    profile_data["bio_link"] = "Bio link not found"

                # Append this profile's data to the list for this search term
                profiles_data.append(profile_data)

                # Go back to the search results page
                driver.back()
                time.sleep(3)

            except StaleElementReferenceException:
                print(f"StaleElementReferenceException encountered for element index {i}. Retrying...")

        # Step 4: Add the data for this search term to the all_profiles_data list
        all_profiles_data.extend(profiles_data)

    # Step 5: Convert the list of all profiles data into a DataFrame
    all_profiles_df = pd.DataFrame(all_profiles_data)

    # Step 6: Append the DataFrame to 'tiktok_profiles.csv'
    all_profiles_df.to_csv("tiktok_profiles.csv", mode='a', index=False, header=False)

finally:
    # Close the WebDriver
    driver.quit()
