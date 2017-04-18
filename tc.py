def titlecase(s):
	words = s.split()
	tcd = []
	for word in words:
		if word in ('of','on','in','an','a','the','and'):
			tcd.append(word)
		else:
			tcd.append(word.capitalize())
	return ' '.join(tcd)
