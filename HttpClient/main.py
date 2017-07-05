"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    (News) get_news <source>   
    (News) (-i | --interactive)
    (News) (-h | --help)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.

"""

import sys
import cmd
from docopt import docopt, DocoptExit
import json
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class NewsFeed(cmd.Cmd):
    intro = 'Welcome to THE NEWS APP!' \
            + ' (type help for a list of commands.)'
    prompt = 'News At Your Finger Tips\n'

    file = None

    @docopt_cmd
    def do_get_news(self, arg):
        """Usage: get_news <source>"""
        source = arg['<source>']
        self.fetch_news(source)

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('******Good Bye!******')
        exit()

    def fetch_news(self, source):
        """
        Http Client to interact with NASA's public APi

        Args:
            source: News Source
        """
        api_key = '51ffb1a860b7437cbd213e7e16c1c5c7'

        print('Fetching News from ' + source + '.................\n')
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


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    NewsFeed().cmdloop()
print(opt)
