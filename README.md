Scrapey is a web scraping application built with Python, Streamlit, and Selenium. It allows users to easily extract HTML content from any website by simply entering the URL. The application uses Selenium for automated browsing and supports headless scraping.

Features
Easy-to-Use Interface: Simple UI powered by Streamlit to input the website URL and scrape content.
Automated Web Scraping: Uses Selenium to automate browsing and extract website content.
Headless Scraping: Runs Chrome in headless mode for efficient scraping without a visible browser window.
Error Handling: Captures errors and provides feedback in the application.
Requirements
To run Scrapey, you'll need the following:

Python 3.7+
Google Chrome
ChromeDriver (matching your Chrome version)
Python Libraries
Install the required Python libraries by running:

bash
Copy code
pip install -r requirements.txt
The requirements.txt file should include:

Copy code
streamlit
selenium
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/athrv1837/Scrapey.git
cd Scrapey
Download ChromeDriver:

Make sure you have Google Chrome installed.
Download ChromeDriver that matches your Chrome version.
Place the chromedriver.exe (for Windows) or chromedriver (for macOS/Linux) in the project directory.
Run the application:

bash
Copy code
streamlit run app.py
Usage
Enter the website URL you want to scrape in the text box.
Click the "Scrape Site" button.
The application will display a preview of the scraped HTML content.
Example Code
Here is a basic example of the scraping function used in Scrapey:

python
Copy code
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def scrape_website(website):
    chrome_driver_path = "./chromedriver.exe"  # Ensure correct path or use absolute path
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    
    try:
        driver.get(website)
        html = driver.page_source
        return html
    finally:
        driver.quit()
Troubleshooting
ChromeDriver not found: Make sure the ChromeDriver is in the project directory and matches your Chrome version.
Connection errors: If a website has a CAPTCHA or blocks scraping, you may need to use a proxy or CAPTCHA-solving service.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contributing
Feel free to contribute to Scrapey! Please submit a pull request or open an issue to discuss any changes.
