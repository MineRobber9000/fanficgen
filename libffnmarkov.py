import markovify
from ff.fiction import Story
from unidecode import unidecode

def getOutput(ids,num_sentences=5):
	stories = [Story(id=id) for id in ids]
	text = ""
	for story in stories:
		for chapter in story.chapters:
			text+=chapter.text
	model = markovify.Text(text)
	out = []
	for n in xrange(num_sentences):
		sent = model.make_sentence()
		while not sent:
			sent = model.make_sentence()
		out.append(sent)
	return unidecode(" ".join(out))
