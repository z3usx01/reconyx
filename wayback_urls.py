# wayback_urls.py
import requests

def fetch_archived_urls(url):
    """Fetch archived URLs from Wayback Machine."""
    api_url = f"https://archive.org/wayback/available?url={url}"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            if 'archived_snapshots' in data and 'closest' in data['archived_snapshots']:
                return data['archived_snapshots']['closest']
        return {'error': 'No archives found'}
    except Exception as e:
        return {'error': str(e)}
