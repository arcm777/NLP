from atlassian import Confluence
import os
from dotenv import load_dotenv

load_dotenv()

confluence = Confluence(
    url=os.getenv("CONFLUENCE_BASE_URL"),
    username=os.getenv("CONFLUENCE_USERNAME"),
    password=os.getenv("CONFLUENCE_API_TOKEN")
)

def fetch_confluence_pages(space_key):
    pages = confluence.get_all_pages_from_space(space=space_key, limit=1000, status='current')
    docs = []
    for page in pages:
        content = confluence.get_page_by_id(page['id'], expand='body.storage')['body']['storage']['value']
        title = page['title']
        clean_text = clean_html(content)
        docs.append({"title": title, "content": clean_text})
    return docs

def clean_html(html):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(separator="\n")