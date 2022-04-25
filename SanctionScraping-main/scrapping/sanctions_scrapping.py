from bs4 import BeautifulSoup
import csv
import requests
from config import sanctions, HEADER
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
    TABLE sanctions
        Source
        Name
        Address
        Sanction Type
        Other Name
        Country
        Eligibility Period
        Grounds
'''


def insert_to_database(record):
    try:
        data = {"Source": record[0], "Name": record[1], "Address": record[2], "Sanction Type": record[3],
                "Other Name": record[4], "Country": record[5], "Eligibility Period": record[6], "Grounds": record[7]}
        returned_id = sanctions.insert_one(data)
        print(returned_id)
    except Exception as e:
        print("Failed to insert into MySQL table {}".format(e))


def list_all_sanctions_dilisense_AsiaDevelopmentBank():
    url = "http://lnadbg4.adb.org/oga0009p.nsf/sancALL1P?OpenView&count=999"
    response = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(response.text, "html.parser")
    container = soup.find(id="viewcontainer")
    if container is not None:
        table = container.find('table')
        if table is not None:
            all_rows = table.find_all('tr')
            count = 0
            for row in all_rows:
                all_data = row.find_all('td')
                index = 0
                record = list()
                for td in all_data:
                    index += 1
                    if index == 1:
                        continue
                    record.append(td.text)
                    count += 1

                if len(record) == 7:
                    record[5] = record[5].strip()
                    if len(record[5]) != 0:
                        temp = record[5].split('|')
                        if len(temp) == 2:
                            _from = temp[0]
                            _to = temp[1]
                            val = ["Dilisense/Asia Development Bank", record[0], record[1], record[2],
                                   record[3], record[4], f'{_from} to {_to}', record[6]]
                            insert_to_database(val)
                record.clear()
            print(f"{count} records has been scraped")
        else:
            raise Exception("Missing id:viewcontainer in the given source")


def list_all_sanctions_dilisense_TheWorldBank():
    url = "https://www.worldbank.org/en/projects-operations/procurement/debarred-firms"
    driver = webdriver.Firefox()
    driver.get(url)
    try:
        element = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, "k-debarred-firms")))
        try:
            element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.ID, "k-grid-content k-auto-scrollable")))
        except:
            pass
        print("Wait for k-debarred-firms done!")
        page = driver.page_source
        soup = BeautifulSoup(page, 'html.parser')
        container = soup.find(id="k-debarred-firms")
        if container is not None:
            tables = container.find_all('table')
            if len(tables) == 2:
                table = tables[1]
                if table is not None:
                    all_rows = table.find_all('tr')
                    count = 0
                    for row in all_rows:
                        all_data = row.find_all('td')
                        record = list()
                        td_index = 0
                        for td in all_data:
                            td_index += 1
                            if td_index != 2:
                                record.append(td.text)
                        if len(record) == 6:
                            count += 1
                            val = ["Dilisense/The World Bank", record[0], record[1], '', '', record[2],
                                   f'{record[3]} to {record[4]}', record[5]]
                            insert_to_database(val)
                    print(f"{count} records has been scraped")
                else:
                    print('Required table is None')
            else:
                print('Expected table format not exists!')
        else:
            print('expected table container not found. try again')
    finally:
        driver.quit()


def list_all_sanctions_Sanction_Intelligence_com_UK_HM_Treasury():
    url = "https://ofsistorage.blob.core.windows.net/publishlive/ConList.csv"
    with requests.get(url, stream=True) as r:
        lines = (line.decode('ISO-8859-1') for line in r.iter_lines())
        line_count = 0
        scraped = 0
        for row in csv.reader(lines):
            try:
                if line_count <= 1:
                    line_count += 1
                else:
                    line_count += 1
                    firstName = row[1]
                    address = ''
                    otherNames = []
                    for i in range(2, 5):
                        tempStr = row[i]
                        if len(tempStr.strip()) > 0:
                            otherNames.append(tempStr)
                    otherName = ','.join(otherNames)
                    country = row[10]
                    grounds = row[22]
                    _from = row[26]
                    _to = row[27]
                    val = ['Sanction Intelligence.com/UK HM Treasury', firstName, address, '', otherName, country,
                           f'{_from} to {_to}', grounds]
                    scraped += 1
                    insert_to_database(val)
            except:
                print('Ignored Row. Since it did not followed the excepted row format')

        print(f'Processed {line_count - 1} lines.')


def test_with_bs4(url):
    response = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(response.text, "html.parser")
    file = open("test.html", "w+")
    file.write(str(soup))
    file.close()


if __name__ == "__main__":
    pass
    # list_all_sanctions_dilisense_AsiaDevelopmentBank()
    # list_all_sanctions_Sanction_Intelligence_com_UK_HM_Treasury()
    # list_all_sanctions_dilisense_TheWorldBank()
    # test_with_bs4('https://www.worldbank.org/en/projects-operations/procurement/debarred-firms')
