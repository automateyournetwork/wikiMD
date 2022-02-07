from pathlib import Path
import wikipedia
import logging
import json
from jinja2 import Environment, FileSystemLoader

template_dir = Path(__file__).parent
env = Environment(loader=FileSystemLoader(template_dir))
wiki_template = env.get_template('wiki.j2')

def tranformWikiPage(page):
    try:
        rawPage = wikipedia.page(page)
        wikiTitle = rawPage.title
        wikiURL = rawPage.url
        wikiContent = json.dumps(rawPage.content)
        wikiLinks = rawPage.links
        wikiSummary = rawPage.summary
        wikiCategory = rawPage.categories
        wikiReferences = rawPage.references
        wikiImages = rawPage.images

        parsed_output = wiki_template.render(
        title = wikiTitle,
        summary = wikiSummary,
        category = wikiCategory,
        refs = wikiReferences,
        URL = wikiURL,
        content = wikiContent,
        links = wikiLinks,
        images = wikiImages
        )
        return (parsed_output)
    except Exception as e:
        logging.exception(e)