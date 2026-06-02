from fastapi import FastAPI, Request 
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests
from bs4 import BeautifulSoup

app = FastAPI()
templates = Jinja2Templates(directory="templates")

dharitri_URL = "https://www.dharitri.com/"

def scrap_news():
    news = [] 
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(dharitri_URL, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        headlines = soup.find_all('p') or soup.find_all('h3')
        
        for element in headlines[:21]: 
            title = element.text.strip()
            
            a_tag = element.find_parent('a') or element.find('a') or element.find_next_sibling('a')
            
            if a_tag and a_tag.has_attr('href') and len(title) > 10:
                link = a_tag['href']
                
                if link.startswith('/'):
                    link = dharitri_URL + link
                    
                if not any(item['title'] == title for item in news):
                    news.append({'title': title, 'link': link})
                    
    except Exception as e:
        print(f"Error occurred during scraping: {e}")
    
    return news

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request): 
    fetched_news = scrap_news()

    return templates.TemplateResponse("dashboard.html", {
            "request": request,
            "news_data": fetched_news, 
        })
