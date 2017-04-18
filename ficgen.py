import libffnmarkov as fm
import ff.fiction as ff
from tc import titlecase
import random

def mixUp(s):
	words = s.split()
	words = [list(w) for w in words]
	for word in words:
		random.shuffle(word)
	words = [''.join(w) for w in words]
	random.shuffle(words)
	words = [w for w in words if random.randint(1,3) != 1]
	return ' '.join(words)

def makeTitle(ids):
	stories = [ff.Story(id=id) for id in ids]
	titles = [st.title for st in stories]
	return titlecase(mixUp(" and ".join(titles)))

def doGenerate(ids,num_sentences=10):
	title = makeTitle(ids)
	contents = fm.getOutput(ids,num_sentences)
	while random.choice(["GO","STOP","STOP"]) == "GO":
		contents += "\n\n"+fm.getOutput(ids,num_sentences)
	return {'title':title,'contents':contents}
