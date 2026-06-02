# 🌐 Ultimate Data Aggregator (BBC News Scraper)

A modern, fast, and lightweight web application built using **FastAPI** that dynamically scrapes live breaking headlines from **BBC News** using **BeautifulSoup4** and displays them in a premium, responsive dark-themed dashboard.

---

## 🚀 Features
* **Live Web Scraping:** Fetching real-time global and tech headlines directly from BBC News.
* **Premium UI:** Clean, responsive, and modern card layout built using Bootstrap 5.
* **Smart URL Routing:** Automatically fixes relative URLs to absolute links for seamless browsing.
* **Robust Error Handling:** Includes fallback mechanisms so the app never crashes even if the source website is down.

---

## 🛠️ Tech Stack
* **Backend:** Python, FastAPI, Uvicorn (ASGI Server)
* **Scraping Engine:** BeautifulSoup4, Requests
* **Frontend/Templating:** Jinja2, HTML5, Bootstrap 5

---

## 📂 Project Structure
```text
API_FETCHING/
│
├── templates/              # HTML Templates Directory
│   └── dashboard.html      # Frontend UI layout
├── app.py                  # Main FastAPI Application & Scraper Logic
├── requirements.txt        # Project Dependencies & Libraries
