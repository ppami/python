import sys
path = sys.argv[1]

file = open(path)
text = file.read().lower()
file.close()

intp = '''!"#%&\()*+,./:;<=>?@[\\]^_{|}~'''
for sign in text:
	if sign in intp:
		text = text.replace(sign, "")
words = text.split()

p = open("p.txt")
positive = p.read().split()
p.close()

n = open("n.txt")
negative = n.read().split()
n.close()

nots = open("negation.txt")
negation = nots.read().split()
nots.close()

sentiment = 0
beforenotpos = ""
beforenotneg = ""

for number, word in enumerate(words):
	if word in positive:
		beforenotpos += words[number - 1]
		if beforenotpos in negation:
			sentiment -= 2
		else:
			sentiment += 1
	elif word in negative:
		beforenotneg += words[number - 1]
		if beforenotneg in negation:
			sentiment += 2
		else:
			sentiment -= 1

if sentiment > 0:
	print(text)
	print("Positive sentence.")
elif sentiment < 0 :
	print(text)
	print("Negative sentence.")
else:
	print(text)
	print("Neutral sentence.")
