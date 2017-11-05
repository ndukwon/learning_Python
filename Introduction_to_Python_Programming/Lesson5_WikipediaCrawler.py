import time
import requests
from bs4 import BeautifulSoup
import urllib

start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"

def continue_crawl(search_history, target_url, max_steps=25):
    '''
    continue_crawl should return True or False

    :param search_history: a list of strings which are the urls of Wikipedia articles. The last item in the list most recently found url.
    :param target_url: a string, the url of the article that the search should stop at if it is found.
    :param max_steps: a int, maximum history size
    :return:
        continue_crawl should return True or False following these rules:
        if the most recent article in the search_history is the target article the search should stop and the function should return False
        If the list is more than 25 urls long, the function should return False
        If the list has a cycle in it, the function should return False
        otherwise the search should continue and the function should return True.
    '''

    if target_url == search_history[-1]:
        print('search_history[-1]:', search_history[-1])
        print('Success: We reached at target_url')
        return False
    elif len(search_history) > max_steps:
        print('Failed: search_history is limited by 25 visits')
        return False
    elif search_history[-1] in search_history[:-1]:
        print('Failed: search_history has cycle links')
        return False
    else:
        return True


def find_first_link(url):
    '''

    :param url:
    :return:
    '''
    response = requests.get(url)
    downloaded_html = response.text
    soup = BeautifulSoup(downloaded_html, 'html.parser')

    the_first_link = None
    paragraphs = soup.find(id='mw-content-text').find(class_='mw-parser-output').find_all('p', recursive=False)
    for p in paragraphs:
        a = p.find('a', recursive=False)
        if a != None:
            the_first_link = a.get('href')
            break

    if the_first_link:
        # Build a full url from the relative article_link url
        the_first_link = urllib.parse.urljoin('https://en.wikipedia.org/', the_first_link)

    return the_first_link

# Main starts
article_chain = [start_url]

while continue_crawl(article_chain, target_url):
    print(article_chain[-1])

    # download html of last article in article_chain
    # find the first link in that html
    first_link = find_first_link(article_chain[-1])

    # add the first link to article chain
    article_chain.append(first_link)

    # delay for about two seconds
    # TODO: YOUR CODE HERE!
    time.sleep(2)
