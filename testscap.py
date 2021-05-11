#!python
from bs4 import BeautifulSoup
# import bs4

'''
easy_install beautifulsoup4
pip install beautifulsoup4
'''
with open('index.html','r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    # print(soup)
    course_cards = soup.find_all('div',class_='card')

    for course in course_cards:
        # print(course)
        course_name = course.h5.text
        course_price = course.a

        print(course_name)
        print(course_price)