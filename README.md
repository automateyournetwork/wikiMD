# wikiMD
A Python Package that transforms any Wikipedia Page into a markmap friendly Markdown file

## How To 
Provide a valid Wikipedia Page Title to the function

```python

>>> print(wikiMD("Computer"))
# Computer
## [URL](https://en.wikipedia.org/wiki/Computer) - https://en.wikipedia.org/wiki/Computer
## Catagories
### All articles needing additional references
### All articles with unsourced statements
### Articles containing video clips
### Articles needing additional references from July 2012

>>> computerWiki = wikiMD("Computer")
>>> with open(f"Computer.md", "w") as fh:
>>>     fh.write(computerWiki)             
>>>     fh.close()


>>> python -m wikiMD Computer

>>> wikiMD Computer

```