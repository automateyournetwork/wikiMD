import sys
from .wikiMD import transformWikiPage
if __name__ == "__main__":
    print(transformWikiPage(sys.argv[1]))
