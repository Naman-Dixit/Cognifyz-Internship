import streamlit as st
from Scrape import scrape_website

st.title("Web Scraper")
url=st.text_input("Enter a Website URL: ")
if st.button("Scrape site"):
    st.write(f"Scraping {url}...")
    # Here you would add your web scraping code using libraries like BeautifulSoup or Scrapy
    st.write("Web scraping completed!") 
    result = scrape_website(url)
    print(result)
 