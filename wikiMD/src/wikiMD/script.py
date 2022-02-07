import sys
from .wikiMD import transformWikiPage
def run():
    print(transformWikiPage(sys.argv[1]))