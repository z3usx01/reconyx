# Reconyx - OSINT Tool

Reconyx is a modular CLI-based OSINT tool that performs website reconnaissance and intelligence gathering.

## Features

- Technology detection (similar to Wappalyzer)
- Wayback Machine archive URL fetching
- Shodan IP analysis
- Modular architecture
- Easy installation and usage

## Installation

```bash
git clone https://github.com/yourusername/reconyx.git
cd reconyx
pip install -r requirements.txt
```

## Usage

Basic scan:
```bash
python reconyx.py https://example.com
```

IP scanning (requires SHODAN_API_KEY environment variable):
```bash
export SHODAN_API_KEY=your_api_key
python reconyx.py 192.168.1.1
```

## Environment Variables

| Variable | Description |
| --- | --- |
| SHODAN_API_KEY | Required for Shodan lookups |

## Modules

Each module handles specific OSINT functionality:

* **tech_detect.py**: Analyzes website technologies
* **wayback_urls.py**: Fetches archived URLs
* **shodan_lookup.py**: Performs IP analysis

## Contributing

Contributions are welcome! Please submit pull requests with clear descriptions of changes.
