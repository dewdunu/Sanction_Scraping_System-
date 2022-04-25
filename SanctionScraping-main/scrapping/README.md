## Sanction Scraping Scripts

### Sanctions Table Columns
- Source
- Name
- Address
- Sanction Type
- Other Name
- Country
- Eligibility Period
- Grounds

### Listed scraped sources
- Dilisense/Asia Development Bank
- Dilisense/The World Bank
- Sanction Intelligence.com/UK HM Treasury

### Used libraries
- BeautifulSoup 
- Requests 
- Pymongo
- Selenium

### Install Firefox Selenium Driver
- Download firefox selenium driver from [click here](https://github.com/mozilla/geckodriver/releases)
- Instructions
  - Download from 0.30.0 version 
  - Extract the downloaded zip
  - If your OS is Windows, just install .exe file
  - If your OS is Linux or Mac, move the driver to the following locations
    - /usr/bin or /usr/local/bin.
  

### Install required libraries
    pip install -r requirements.txt

### Run main script
    python sanctions_scrapping.py