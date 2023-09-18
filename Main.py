import openpyxl
from bs4 import BeautifulSoup
import requests
import openpyxl
from openpyxl import load_workbook
url = "https://weather.com/weather/tenday/l/Mahoning+Township+PA?canonicalCityId=1035939183d80a97a7b0ef4df08ca60d53c49d87aba371d0a87bb12576133236"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

temp_elements = soup.find_all('span', class_ = 'DetailsSummary--lowTempValue--2tesQ',)
dates = soup.find_all('h3', class_ = 'DetailsSummary--daypartName--kbngc',)

temperatures = [element.get_text() for element in temp_elements]
text_dates = [element.get_text() for element in dates]

try:
    workbook = load_workbook('snow_excel.xlsx')
    sheet = workbook.active
except FileNotFoundError:
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    sheet['A1'] = 'Dates'
    sheet['B1'] = 'temperature'

next_row = sheet.max_row + 2

for row, (item1, item2) in enumerate(zip(text_dates, temperatures), start= next_row):
    sheet[f'A{row}'] = item1
    sheet[f'B{row}'] = item2

workbook.save('snow_excel.xlsx')

workbook = openpyxl.load_workbook('snow_excel.xlsx') 

sheet = workbook['Sheet']  

for row in sheet.iter_rows(min_row=1, max_row=sheet.max_row, min_col=1, max_col=sheet.max_column):
    for cell in row:
        print(cell.value, end='\t')
    print() 

workbook.close()
