import pywikibot as pw # pyright: ignore[reportMissingImports]
import tfuncs as tf
import editsettings as es

def main():
	site = pw.Site(es.sitecode, "wikipedia")
#	allpages = site.allpages(namespace=0)
	allpages = [pw.page.Page(site, "Kaimbot test page "+str(i)) for i in range(2)]
	allpages.append(pw.page.Page(site, "AliExpress"))
	tems = es.templates.split()
	
	for page in allpages:
		if tf.isnew(page): continue
		pagetext = page.text
		
		if "reflist" in tems: page.text=tf.reftem(page)
		if "stub" in tems: page.text=tf.stubtem(page)
		if "unreferenced" in tems: page.text=tf.unreftem(page)
		if "uncategorized" in tems: page.text=tf.uncattem(page)
		if "update" in tems: page.text=tf.updatetem(page)

		page.save(es.getsummery(),bot=True)
		es.clear_summery()
	

if __name__ == "__main__":
	main()
