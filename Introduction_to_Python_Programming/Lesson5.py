
# Using Python to get HTML
if True:
    import requests

    # response = requests.get('https://en.wikipedia.org/wiki/Dead_Parrot_sketch')
    response = requests.get('https://en.wikipedia.org/wiki/A.J.W._McNeilly')
    downloaded_html = response.text
    # print('downloaded_html:', downloaded_html)

    from bs4 import BeautifulSoup

    soup = BeautifulSoup(downloaded_html, 'html.parser')
    print('soup.title:', soup.title)            # title 부분을 읽는다.
    print('soup.p:', soup.p)                    # p tag가 달린 첫번째를 찾는다.
    print('soup.p.a:', soup.p.a)                # p tag가 달린 첫번째에서 a tag가 달린 첫번째를 찾는다.
    print('soup.a:', soup.a)                    # a tag가 달린 첫번째를 찾는다.
    print("soup.find_all('a'):", soup.find_all('a'))    # a tag가 달린 모든것을 찾는다.
    # print("soup.:", soup.div(id='image-gallery'))     # 안됌
    # print("soup.find(id='image-gallery'):", soup.find(id='mw-content-text'))    # 주어진 id에 맞는 tag를 찾는다.
    print("soup.find(id='mw-content-text'):", soup.find(id='mw-content_text'))
    print("soup.find(id='mw-content-text').find(class_='mw-parser-output'):", soup.find(id='mw-content-text').find(class_="mw-parser-output"))
    print("soup.find(id='mw-content-text').find(class_='mw-parser-output').p.a.get('href'):", soup.find(id='mw-content-text').find(class_="mw-parser-output").p.a.get('href'))

    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    for element in content_div.find_all("p", recursive=False):
        if element.a:
            first_relative_link = element.find('a', recursive=False).get('href')
            print('first_relative_link:', first_relative_link)
            break


# Quiz: The continue_crawl Function
if False:
    print("\n# Quiz: The continue_crawl Function")

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

    print(continue_crawl(['https://en.wikipedia.org/wiki/Floating_point'],
                       'https://en.wikipedia.org/wiki/Philosophy'))


# Quiz: Add a Link to the Article Chain
# Quiz: Just Wait a Moment!
if False:
    print("\n# Quiz: Add a Link to the Article Chain")
    print("\n# Just Wait a Moment!")
    '''
    Write a line of code that will add the first_link to the end of the list article_chain.
    This line should come after the comment, "add the first link to article chain".
    
    Work out the final step in the while loop - how to make Python wait for two seconds.
    You might need to do some research to find a relevant Python package and/or command to use.
    Add an import statement to the top part if needed, and then a line of code at the bottom of the indented block.
    '''
    def web_crawl():
        article_chain = ['https://en.wikipedia.org/wiki/Floating_point']
        target_url = 'https://en.wikipedia.org/wiki/Philosophy'
        import time

        while continue_crawl(article_chain, target_url):
            # download html of last article in article_chain

            # find the first link in that html
            first_link = find_first_link(article_chain[-1])

            # add the first link to article chain
            article_chain.append(first_link)

            # delay for about two seconds
            # TODO: YOUR CODE HERE!
            time.sleep(2)
