# Unfollowers Web App  

A full-stack web application that identifies Instagram accounts you follow who don’t follow you back. Built with **Flask, Python, JavaScript, HTML/CSS, and BeautifulSoup**.  

---

## Features  
- Upload Instagram **Followers** and **Followings** HTML export files.  
- Parse data using **BeautifulSoup** and cleanly extract usernames.  
- Identify **unfollowers** with efficient set operations.  
- Display results dynamically through **JSON API responses**.  
- Responsive front-end with **file upload form** and async `fetch` calls.  

---

## Tech Stack  
- **Backend**: Python, Flask, BeautifulSoup  
- **Frontend**: HTML, CSS, JavaScript  
- **Data Handling**: JSON APIs

---

## How It Works  
1. Export your **Followers** and **Following** lists from Instagram as HTML.  
2. Upload both files through the app interface.  
3. The backend parses usernames and compares sets.  
4. A dynamic preview of **unfollowers** is displayed.  

---

## Run Locally  

Clone the project:  
```bash
git clone https://github.com/your-username/unfollowers-app.git
cd unfollowers-app
```

Install dependencies:  
```bash
pip install flask beautifulsoup4 lxml
```

Run the server:  
```bash
python server.py
```

Open in your browser:  
```
http://127.0.0.1:5000/
```
