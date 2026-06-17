# helpers/company_list.py

import json

companies = set()

with open(r"C:\Users\Eternity\Dropbox\Projects\New folder\[PUB] India_runs_data_and_ai_challenge\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        candidate = json.loads(line)

        for exp in candidate.get("career_history", []):
            company = exp.get("company")
            if company:
                companies.add(company.strip())

print(f"Unique companies: {len(companies)}")
print("Unique companies list:")

for company in (companies):
    print(f" - {company}")




# Unique companies: 63
# Unique companies list:

# - Accenture
# - TCS
# - Niramai
# - Stark Industries
# - Pied Piper
# - Mphasis
# - Hooli
# - HCL
# - Ola
# - Wayne Enterprises
# - Mindtree
# - Flipkart
# - Unacademy
# - Vedantu
# - Genpact AI
# - PolicyBazaar
# - Freshworks
# - Dunder Mifflin
# - Paytm
# - Apple
# - Aganitha
# - Wysa
# - Nykaa
# - Capgemini
# - Amazon
# - BYJU'S
# - Tech Mahindra
# - Meta
# - Salesforce
# - Dream11
# - Locobuzz
# - Wipro
# - Razorpay
# - InMobi
# - Haptik
# - Meesho
# - Verloop.io
# - Netflix
# - Uber
# - Yellow.ai
# - Observe.AI
# - Sarvam AI
# - Google
# - Mad Street Den
# - Cognizant
# - CRED
# - PharmEasy
# - Saarthi.ai
# - Globex Inc
# - Krutrim
# - Initech
# - Zomato
# - Adobe
# - Swiggy
# - upGrad
# - Glance
# - Microsoft
# - PhonePe
# - Acme Corp
# - Rephrase.ai
# - LinkedIn
# - Infosys
# - Zoho