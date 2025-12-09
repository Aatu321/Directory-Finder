import requests
import sys

def directory_finder(base_url, wordlist):
    print("\n=== Directory Finder (Ethical Web Recon Tool) ===\n")

    try:
        with open(wordlist, "r") as file:
            paths = file.read().splitlines()
    except FileNotFoundError:
        print("Wordlist file not found!")
        return

    if not base_url.startswith("http"):
        base_url = "http://" + base_url

    for path in paths:
        url = f"{base_url}/{path}"

        try:
            r = requests.get(url, timeout=4)

            if r.status_code == 200:
                print(f"[FOUND] {url}  (200 OK)")
            elif r.status_code == 403:
                print(f"[FORBIDDEN] {url}  (403)")
        except:
            pass

    print("\nScan complete!")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python dir_finder.py <url> <wordlist>")
    else:
        directory_finder(sys.argv[1], sys.argv[2])
