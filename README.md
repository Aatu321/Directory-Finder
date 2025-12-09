# Directory-Finder
A lightweight Python-based directory brute‑forcing tool for ethical web reconnaissance.  Uses a wordlist to detect hidden directories and endpoints on a target website.
# 🔍 Directory Finder (Web Recon Tool)

A lightweight Python-based **directory brute‑force scanner** used for ethical web reconnaissance.  
This tool helps you discover **hidden directories, admin panels, API endpoints, and sensitive files** on a target website using a wordlist.

Perfect for:
- Bug bounty hunters  
- Security researchers  
- Ethical hackers  
- Web recon learning  

---

## 🚀 Features

- Fast & simple directory brute forcing  
- Custom **URL + wordlist** support  
- Detects:
  - /admin  
  - /login  
  - /uploads  
  - /backup  
  - Hidden folders & files  
- Status code–based discovery  
- No external heavy libraries  
- Clean terminal output  

---

## 📁 Installation

Clone this repository:

```bash
git clone https://github.com/<your-username>/Directory-Finder.git
cd Directory-Finder
python dir_finder.py <url> <wordlist>
python dir_finder.py https://example.com wordlist.txt
=== Directory Finder (Ethical Web Recon Tool) ===

[200] Found: https://example.com/admin
[301] Found: https://example.com/uploads
[403] Forbidden but Exists: https://example.com/private
[404] Not Found: /invalid (skipped)
Directory-Finder/
│── dir_finder.py
│── wordlist.txt
└── README.md
pip install requests

