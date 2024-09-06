import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pandas as pd
import time
import random

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def setup_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)
    chrome_options.add_argument('--headless')
    return webdriver.Chrome(options=chrome_options)


def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))


def scrape_page(driver, url):
    try:
        driver.get(url)
        wait_for_element(driver, By.CLASS_NAME, 'adbl-impression-container')

        titles = driver.find_elements(By.CSS_SELECTOR, '.adbl-impression-container li h3.bc-heading')
        authors = driver.find_elements(By.CSS_SELECTOR, '.adbl-impression-container li.bc-list-item.authorLabel')
        lengths = driver.find_elements(By.CSS_SELECTOR, '.adbl-impression-container li.bc-list-item.runtimeLabel')

        return [
            [title.text for title in titles],
            [author.text.replace('By: ', '') for author in authors],
            [length.text.replace('Length: ', '') for length in lengths]
        ]
    except (TimeoutException, NoSuchElementException) as e:
        logger.error(f"Error scraping page {url}: {str(e)}")
        return [[], [], []]


def main():
    driver = setup_driver()
    base_url = 'https://www.audible.com/search'
    list_titles, authors_list, list_length = [], [], []

    try:
        for page in range(1, 26):
            logger.info(f"Scraping page {page}")
            url = f"{base_url}?page={page}"
            titles, authors, lengths = scrape_page(driver, url)

            list_titles.extend(titles)
            authors_list.extend(authors)
            list_length.extend(lengths)

            time.sleep(random.uniform(1.5, 3.5))

    except Exception as e:
        logger.error(f"An unexpected error occurred: {str(e)}")
    finally:
        driver.quit()

    if list_titles and len(list_titles) == len(authors_list) == len(list_length):
        books = pd.DataFrame({
            'title': list_titles,
            'author': authors_list,
            'length': list_length
        })
        books.to_csv('books_data.csv', index=False)
        logger.info(f"Successfully scraped {len(books)} books. Data saved to books_data.csv")
    else:
        logger.error("No data collected or lists have different lengths. Unable to create CSV.")


if __name__ == "__main__":
    main()
