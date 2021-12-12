print()
import requests
from bs4 import BeautifulSoup

def main():
   prices = []
   resp = requests.get('http://blog.castman.net/py-scraping-analysis-book/ch2/table/table.html')
   soup = BeautifulSoup(resp.text, 'html.parser')
   rowsa = soup.find('table', 'table')
   rowsb = rowsa.tbody.find_all('tr')
   #print("<執行結果> rowsb=", rowsb) #=====
   #print()

   for row in rowsb:
       price = row.find_all('td')[2].text
       #print("<執行完成> price=", price) #=====
       prices.append(int(price)) 
   print("<執行結果> prices=", prices) #=====

   
if __name__ == '__main__':
   main()


   #print("<執行完成> =" ) #=====
   print()