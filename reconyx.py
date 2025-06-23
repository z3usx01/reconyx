import argparse
from tech_detect import detect_technologies
from wayback_urls import fetch_archived_urls
from shodan_lookup import perform_shodan_lookup

def main():
    parser = argparse.ArgumentParser(description='Reconyx - OSINT Tool')
    parser.add_argument('target', help='Target URL or IP address')
    
    args = parser.parse_args()
    target = args.target
    
    print(f"\n[+] Starting Reconyx scan for: {target}\n")
    
    # Technology detection
    print("[+] Detecting technologies...")
    tech_data = detect_technologies(target)
    print("\n[++] Technology Detection Results:")
    print(json.dumps(tech_data, indent=2))
    
    # Wayback Machine lookup
    print("\n[+] Fetching archived URLs...")
    archive_urls = fetch_archived_urls(target)
    print("\n[++] Archive URLs Results:")
    print(json.dumps(archive_urls, indent=2))
    
    # Shodan lookup if target is an IP
    import ipaddress
    try:
        ipaddress.ip_address(target)
        print("\n[+] Performing Shodan lookup...")
        shodan_data = perform_shodan_lookup(target)
        print("\n[++] Shodan Results:")
        print(json.dumps(shodan_data, indent=2))
    except ValueError:
        print("\n[+] Target is not an IP address, skipping Shodan lookup")

if __name__ == "__main__":
    main()
