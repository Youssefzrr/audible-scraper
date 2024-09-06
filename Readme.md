# Audible Book Scraper

This Python script scrapes book information from Audible's search results pages using Selenium WebDriver.

## Features

- Scrapes book titles, authors, and lengths from Audible search results
- Handles multiple pages of results
- Uses headless Chrome browser for faster scraping
- Implements random delays to avoid rate limiting
- Saves results to a CSV file

## Requirements

- Python 3.6+
- Chrome browser
- ChromeDriver

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/audible-scraper.git
   cd audible-scraper
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Ensure you have Chrome and ChromeDriver installed. The ChromeDriver version should match your Chrome version.

## Usage

Run the script with:

```
python audible_scraper.py
```

The script will scrape 25 pages of Audible search results and save the data to `books_data.csv`.

## Note

Web scraping may be against Audible's terms of service. Use this script responsibly and consider using Audible's official API if available.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.