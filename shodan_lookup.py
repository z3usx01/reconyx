# shodan_lookup.py
import requests
import os

def perform_shodan_lookup(ip):
    """Perform Shodan lookup for an IP address."""
    api_key = os.environ.get('SHODAN_API_KEY')
    if not api_key:
        return {'error': 'SHODAN_API_KEY environment variable not set'}
        
    url = f"https://api.shodan.io/shodan/host/{ip}?key={api_key}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return {'error': 'Shodan API error'}
    except Exception as e:
        return {'error': str(e)}
