import requests
from bs4 import BeautifulSoup
import csv

def get_book_details(book):
    title = book.find('a', class_='bookTitle').text.strip()
    author = book.find('span', itemprop='author').text.strip()
    rating = book.find('span', class_='minirating').text.strip()  
    return title, author, rating

url = 'https://www.goodreads.com/list/show/2994.Couldn_t_Put_The_Book_Down_'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    with open('book_list.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title', 'Author', 'Rating'])
        
        books = soup.find_all('tr', itemtype='http://schema.org/Book')
        for book in books:
            title, author, rating = get_book_details(book)
            writer.writerow([title, author, rating])
    
    print('CSV file created.')
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
