# tech_detect.py
import requests
from bs4 import BeautifulSoup
import json

def detect_technologies(url):
    """Detect technologies used by analyzing website headers and content."""
    try:
        response = requests.get(url, timeout=10)
        
        # Analyze headers
        headers = {}
        for header, value in response.headers.items():
            if any(keyword in header.lower() for keyword in ['server', 'powered-by']):
                headers[header] = value
        
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find meta tags and scripts
        meta_tags = [tag['content'] for tag in soup.find_all(attrs={'content': True})]
        script_tags = [tag['src'] for tag in soup.find_all('script', src=True)]
        
        return {
            'headers': headers,
            'meta_tags': meta_tags,
            'scripts': script_tags
        }
    except Exception as e:
        return {'error': str(e)}
