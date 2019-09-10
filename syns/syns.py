#!/usr/bin/env python3
# Jan Fecht 2019
"""
Uses the openthesaurus API to access synonyms
Read more about the API at https://www.openthesaurus.de/about/api
"""
import requests
import argparse
import json
import sys

from pprint import pprint


API_URL="https://www.openthesaurus.de/synonyme/search"
VERSION="1.0"

class Search:
    """
    TODO:
        substring
        substringFromResults
        substringMaxResults
        startswith
        supersynsets
        subsynsets
        baseform
    """

    def __init__(self, word, similar=True, max_results=10, verbose=False):
        self.word = word
        self.similar = similar
        self.max_results = max_results
        self.verbose = verbose

    def fetch_results(self):
        values = {
            "format":        "application/json",
            "q":             self.word,
            "similar":       str(self.similar).lower(),
                }
        try:
            r = requests.get(API_URL, params=values)
        except requests.ConnectionError:
            sys.stderr.write("Error fetching results\n")
            return False
        j = json.loads(r.text)
        pprint(j)
        return True

    def print_results(self):
        pass



def main():
    cli = argparse.ArgumentParser(description=__doc__, prog='Syns')
    cli.add_argument('word', metavar='WORD', type=str,
                    help='the word to find synonyms for')
    cli.add_argument('--similar', '-s', action='store_true',
                    help='Include similar words')
    cli.add_argument('--verbose', '-v', action='store_true',
                    help='Show more detailed information about the synonyms')
    cli.add_argument('--results', '-n', type=int, default=10,
                    help='Maximum number of results (defaults to 10)')
    cli.add_argument('--version', action='version', version='%(prog)s \
            {}'.format(VERSION), help="Print current version")
    args = cli.parse_args()

    s = Search(args.word, similar=args.similar, max_results=args.results,
            verbose=args.verbose)
    ok = s.fetch_results()
    if ok:
        s.print_results()

if __name__ == "__main__":
    main()
