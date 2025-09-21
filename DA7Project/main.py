from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
import json


def scrape_category(category_url, category_name):
    driver = Chrome()
    driver.get(category_url)
    time.sleep(5)

    try:
        close_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='بستن']")
        close_button.click()
        time.sleep(2)
    except:
        pass

    all_news = []
    scroll_steps = 12
    scroll_pause = 2.5

    for step in range(scroll_steps):
        scroll_position = (step + 1) * 400
        driver.execute_script(f"window.scrollTo(0, {scroll_position});")
        time.sleep(scroll_pause)

        news_blocks = driver.find_elements(By.CSS_SELECTOR, "blockquote.n-4df7w3")

        for block in news_blocks:
            try:
                title_element = block.find_element(By.CSS_SELECTOR, "h3.n-0neaww.prosed")
                title = title_element.text.strip()

                if title and title not in [news['title'] for news in all_news]:
                    summary_element = block.find_element(By.CSS_SELECTOR, "span.n-y64nk4.prosed")
                    summary = summary_element.text.strip()

                    link_element = block.find_element(By.CSS_SELECTOR, "a.n-h3v2f0")
                    link = link_element.get_attribute("href")

                    try:
                        img_element = block.find_element(By.CSS_SELECTOR, "img[src*='width=600']")
                        image_url = img_element.get_attribute("src")
                    except:
                        image_url = "بدون عکس"

                    all_news.append({
                        "title": title,
                        "summary": summary,
                        "link": link,
                        "image_url": image_url,
                        "category": category_name
                    })
            except:
                continue

    driver.close()
    return all_news


categories = [
    {"url": "https://farsnews.ir/politics/posts", "name": "سیاسی"},
    {"url": "https://farsnews.ir/social/posts", "name": "اجتماعی"},
    {"url": "https://farsnews.ir/Economy/posts", "name": "اقتصادی"},
    {"url": "https://farsnews.ir/world/posts", "name": "جهان"}
]

all_news_data = []

for category in categories:
    try:
        news = scrape_category(category["url"], category["name"])
        all_news_data.extend(news)
    except:
        pass

news_with_ids = []
for i, news in enumerate(all_news_data):
    news_with_ids.append({
        "id": i + 1,
        "title": news["title"],
        "summary": news["summary"],
        "link": news["link"],
        "image_url": news["image_url"],
        "category": news["category"],
        "source": "فارس نیوز"
    })

with open("all_fars_news.json", "w", encoding="utf-8") as f:
    json.dump(news_with_ids, f, ensure_ascii=False, indent=2)