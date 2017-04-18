template = """<html>
<head>
<title>Markov's Fanfic - {title}</title>
<link rel="stylesheet" href="../style.css">
</head>
<body>
<h1>{title}</h1>
<p>{contents}</p>
<a href='index.html'>Back to homepage</a>
</body>
</html>
"""

def makePage(genfic):
	return template.format(title=genfic['title'],contents=genfic['contents'].replace("\n\n","</p><p>"))

