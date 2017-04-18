import markovify,sys,json
from ff.fiction import Story
from unidecode import unidecode
input = json.loads(sys.stdin.read())

stories = [Story(id=id) for id in input["ids"]]

text = ""
for story in stories:
	for chapter in story.chapters:
		text+=chapter.text

model = markovify.Text(text)

out = []
for n in xrange(input["num_sentences"]):
	sent = model.make_sentence()
	while not sent:
		sent = model.make_sentence()
	out.append(sent)
print unidecode(" ".join(out))
