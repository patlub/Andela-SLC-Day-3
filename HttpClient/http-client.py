import json
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

"""Http Client to interact with NASA's public APi"""


def fetch_news(source):
    """
    Args:
        source: News Source
    """
    api_key = '51ffb1a860b7437cbd213e7e16c1c5c7'

    print('Get News from Top News Channels Around the world')

    print('Fetching News.................\n')
    req_url = 'https://newsapi.org/v1/articles?source=' + source + '&apiKey=' + api_key
    req = Request(req_url)
    try:
        response = urlopen(req)

    # Returns error from server
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)

    # Returns error if server is unreachable
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)

    # json parse the response to print only the relevant information
    else:
        json_obj = json.load(response)
        print('Source:' + json_obj['source'] + '\n')
        for article in json_obj['articles']:
            print('Author: ' + article['author'] + '\n')
            print('Title: ' + article['title'] + '\n')
            print('Article: ' + article['description'] + '\n')

            print('=========================================')
