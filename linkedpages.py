import pywikibot
from pywikibot import pagegenerators
from pywikibot import site
import json, urllib

### primary function
def do(article_names, language):
	print("\n")
	language_dictionary = generate_language_dict()
	storelinks = {}
	language_code = language_dictionary[language]
	site = pywikibot.getSite(language_code)

	for article_name in article_names:
		storelinks[article_name] = getlinks(site, article_name)

	for ogpage, backlink_generator in storelinks.items():
		print(ogpage.title())
		linked_to_count = 0
		for backlink in backlink_generator:
			linked_to_count += 1
			print(backlink.title(withNamespace=False, withSection=False))
		print(str(linked_to_count) + " articles link to " + ogpage.title() + "\n\n")

### returns num number of links that link to the original article (in this case the original article is set to the first
### article that appears in the generated set of articles)
def getlinks(site, pageName):
	page = pywikibot.Page(site, pageName)
	return site.pagebacklinks(page, followRedirects=True, filterRedirects=True, namespaces=None, content=False)
	#return page.backlinks()
def generate_language_dict():
    with open("list_of_wiki_languages.txt", "r") as file:
        lines = file.read().split(",")
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
            lines[i] = lines[i].strip("\'")
        dictionary = {lines[i+1]:lines[i] for i in range(0, len(lines), 2)}
    return dictionary

do(["Pear", "Grape"], "English")
#outputs the article title, list of articles that link to that article, and 
# number of articles that link to that article for each article in list provided
# as first parameter

#questions:
#gen is an iterable object but not an array, how do i just get the first one, or like
#the most popular page from gen
#
#1. Get the most popular article once you get user input on the topic of interest (for now just choose some random article)
#2. Store some arbitrary number of articles that link to the original article
#3. Output those articles (I guess in terms of order of popularity?)