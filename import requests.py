from bs4 import BeautifulSoup
import requests

# Website URL
URL = 'https://www.google.com/finance/quote/AAPL:NASDAQ'

# Page content from Website URL
page = requests.get(URL)


# Function to remove tags
def remove_tags(html):

    # parse html content
    soup = BeautifulSoup(html, "html.parser")

    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()
        apple=soup.find_all("div", class_="YMlKec fxKbKc")

    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)
soup.find_all("div", class_="YMlKec fxKbKc")


# Print the extracted data
print(remove_tags(page.content))
file=open('note1.txt')
file.write(remove_tags(page.content))
file.close
