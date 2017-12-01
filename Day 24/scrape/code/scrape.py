import requests
from bs4 import BeautifulSoup

loc = 'London,+United%20Kingdom'
#change this var for other place if you want to scrap other location

def lookup_be_location(loc):
    base_url = "https://www.yelp.com/search?find_loc="
    current_page = 0
    while current_page < 201:
        print(current_page)
        url= base_url + loc + "&start=" + str(current_page)
        yelp_r = requests.get(url)
        yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')
        file_path = 'yelp2-{loc}.txt'.format(loc=loc)
        businesses = yelp_soup.findAll('div',{'class': 'biz-listing-large'})
        with open(file_path, 'a') as textfile:
            businesses = yelp_soup.findAll('div',{'class': 'biz-listing-large'})
            for biz in businesses:
                title = biz.findAll('a', {'class': 'biz-name'})[0].text
                print(title)
                address = biz.findAll('address')[0].contents
                second_line= ""
                first_line = ""
                try:
                    for item in address:
                        if "br" in str(item):
                            #print(item.getText())
                            second_line += item.getText().strip(" \n\t\r")
                        else:
                            print(item.strip(" \n\t\r"))
                            first_line += item.strip(" \n\t\r")
                    print(first_line)
                    print(second_line)
                except:
                    pass
                print("\n")
                try:
                    phone = biz.findAll('span', {'class': 'biz-phone'})[0].text.strip(" \n\t\r")
                except:
                    phone= None
                print(phone)
                page_line = "{title}\n{address1}\n{address2}\n{phone}\n".format(
                    title = title,
                    address1 = first_line,
                    address2 = second_line,
                    phone = phone
                    )
                textfile.write(page_line)
        current_page +=10

lookup_be_location(loc)
'''
you can also call this function with needed location by passing argument
as a string, like lookup_be_location('Newport+Beach,+CA,+United+States')
'''

'''
Working with Django
obj = SomeModel()
obj.title = title
obj.line_1 = first_line
obj.save()
'''




