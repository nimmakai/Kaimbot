import pywikibot as pw # pyright: ignore[reportMissingImports]
import editsettings as es
import re
import datetime

def addtemp(maintext, template):
	if template[:-2] in maintext or template.lower()[:-2] in maintext: return maintext
	i = re.search("\\[\\[[cC]ategory:.*\\]\\]",maintext)
	if not i: return maintext + "\n" + template
	index = i.start()
	return maintext[:index] + "\n" + template + "\n" + maintext[index:]

def isnew(page):
	return (datetime.datetime.now() - page.latest_revision['timestamp']).days < 2
	
def isold(page):
	return (datetime.datetime.now() - page.latest_revision['timestamp']).days > 730

def reftem(page):
	kwords = "{{Reflist {{reflist <references"
	for r in kwords.split(): 
		if r in page.text: return page.text
	page.text=addtemp(page.text,"{{Reflist}}")
	es.put_summary("Reflist","Template","add")
	return page.text

def stubtem(page):
	if len(page.text) >= 1000: return page.text
	for i in re.findall("\\[\\[[cC]ategory:[sS]tub\\]\\]",page.text):
		page.text = page.text.replace(i,"")
		es.put_summary("Stub","Category","remove")
	if page.isRedirectPage(): return page.text
	page.text=addtemp(page.text,"{{Stub}}")
	es.put_summary("Stub","Template","add")
	return page.text

def unreftem(page):
	refens = "<ref {{cit {{Unreferenced {{unreferenced"
	for r in refens.split():
		if r in page.text: return page.text
	page.text = "{{Unreferenced|date="+datetime.datetime.now().strftime("%b %Y")+"}}\n"+page.text
	es.put_summary("Unreferenced","Template","add")
	return page.text

def uncattem(page):
	for i in re.findall("\\[\\[[cC]ategory:.*\\]\\]",page.text): return page.text
	page.text = "{{Uncategorized|date="+datetime.datetime.now().strftime("%b %Y")+"}}\n"+page.text
	es.put_summary("Uncategorized","Template","add")
	return page.text
	
def updatetem(page):
	if not isold(page): return page.text
	page.text = "{{Update|date="+datetime.datetime.now().strftime("%b %Y")+"}}\n"+page.text
	es.put_summary("Update","Template","add")
	return page.text

