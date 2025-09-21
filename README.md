🗞️ Web Scraper for Fars News Agency
A Python-based web scraper that extracts news articles from various categories of Fars News Agency (Farsnews.ir) using Selenium.

📋 Features
Multi-Category Support: Scrapes news from 4 main categories:

📰 Political News (/politics)

👥 Social News (/social)

💰 Economic News (/economy)

🌍 World News (/world)

Comprehensive Data Extraction:

News headlines and titles

Article summaries and preview text

Direct links to full articles

News images and thumbnails

Category classification

Source identification

Smart Scrolling: Automated scroll functionality to load and capture all available articles
Adjustable Scroll Settings: Easily modify scroll parameters to get more articles:

python
scroll_steps = 20    # Increase for more scrolling
scroll_pause = 3.0   # Increase for slower loading
scroll_position = 500  # Increase for larger scroll jumps

🛠️ Technical Details
Prerequisites
Python 3.7+

Chrome Browser

ChromeDriver (automatically managed by Selenium)

Dependencies
bash
pip install selenium
Usage
python
# Run the scraper
python farsnews_scraper.py

# Output will be saved to: all_fars_news.json
Output Format
The scraper generates a JSON file with the following structure:

json
[
  {
    "id": 1,
    "title": "News Headline",
    "summary": "News summary text...",
    "link": "https://farsnews.ir/full-article-url",
    "image_url": "https://cdn.farsnews.ir/news-image.jpg",
    "category": "سیاسی",
    "source": "فارس نیوز"
  }
]
⚙️ How It Works
Initialization: Launches Chrome browser and navigates to Fars News categories

Popup Handling: Automatically closes any subscription popups

Content Loading: Uses smart scrolling to load all available articles

Data Extraction: Parses HTML to extract news content using CSS selectors

Data Storage: Saves structured data to JSON format

🔧 Customization
You can easily modify the script to:

Add more news categories

Adjust scrolling parameters

Change output format (CSV, database, etc.)

Add error handling and logging

Implement rate limiting

⚠️ Important Notes
This tool is for educational purposes only

Respect website's robots.txt and terms of service

Consider adding delays between requests to avoid overloading servers

Check website structure regularly as it may change

📄 License
This project is intended for educational use. Please ensure compliance with applicable laws and website terms of service.

🤝 Contributing
Feel free to fork this project and submit pull requests for improvements and bug fixes.

Note: Always use web scraping tools responsibly and ethically.

