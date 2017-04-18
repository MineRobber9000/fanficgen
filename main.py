import ficgen,pagegen,uuid,json

# Tweak these for different results
c_ids = [12425824,12372218]	# list of ids (value required)
c_num_sentences = 0		# number of sentences per paragraph (0 = use default (currently 10))

# Don't change anything below this line.
name = str(uuid.uuid1())

fic = {}
if c_num_sentences >= 1:
	fic = ficgen.doGenerate(c_ids,c_num_sentences)
else:
	fic = ficgen.doGenerate(c_ids)
page = pagegen.makePage(fic)
with open("www/"+fic['title'].lower().replace(" ","_")+"_"+name[:8]+".html","w") as f:
	f.write(page)
json.dump(fic,open(name+".json","w"))
print "New fanfic at www/"+fic['title'].lower().replace(" ","_")+"_"+name[:8]+".html"
