from bs4 import BeautifulSoup
import requests
import json
from os import path

UCSD_COURSE_CATALOG_BASE_URL = 'http://www.ucsd.edu/catalog/'
UCSD_COURSE_CATALOG_MAIN_PAGE_URL = 'http://www.ucsd.edu/catalog/front/courses.html'

response = requests.get(UCSD_COURSE_CATALOG_MAIN_PAGE_URL)

soup = BeautifulSoup(response.text, 'html.parser')

a_tags = soup.findAll('a', string='courses')
partial_urls = map(lambda a: a['href'][3:], a_tags)

courses = []
seen = set()

pk = 1
for partial_url in partial_urls:
    response = requests.get(UCSD_COURSE_CATALOG_BASE_URL + partial_url)

    soup = BeautifulSoup(response.text, 'html.parser')

    p_tags = soup.find_all('p', class_='course-name')


    for p_tag in p_tags:
        text = ' '.join(p_tag.text.replace('\n', '').replace('\t', '').split())
        split1 = text.split('.')

        if len(split1) is not 2:
            continue

        split2 = split1[0].split(' ')

        if len(split2) is not 2:
            continue

        department = split2[0]
        number = split2[1] 
        verbose_name = split1[1].strip()

        if (department, number) in seen:
            continue

        seen.add((department, number))


        course_fields = {
            'department': department,
            'number': number,
            'verbose_name': verbose_name
        }

        course = {
            'model': 'courses.course',
            'pk': pk,
            'fields': course_fields
        }

        courses.append(course)
        pk += 1
    
with open(path.join(path.dirname(path.dirname(path.abspath(__file__))), 'data/ucsd_courses.json'), 'w+') as courses_file:
    json.dump(courses, courses_file)


