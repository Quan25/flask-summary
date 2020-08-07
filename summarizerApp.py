import sys, os
from typing import List
import time
from nltk import tokenize
srcdir = '/home/quan/Desktop/flask_summary/summarizer'
sys.path.insert(0, os.path.abspath(os.path.join(srcdir)))


from summarizer.lecture_summarizer import SingleModelProcessor

def process_content_sentences(body: str) -> List[str]:
	sentences = tokenize.sent_tokenize(body)
	return [c for c in sentences if len(c) > 75 and not c.lower().startswith('but') and
			not c.lower().startswith('and')
			and not c.lower().__contains__('quiz') and
			not c.lower().startswith('or')]

def createSummary(passage: str, ratio:float):

	text = process_content_sentences(passage)
	if len(text) == 0:
		raise RuntimeError("No viable sentences found. Consider adding larger lectures.")
	sentences = SingleModelProcessor().run_clusters(text, ratio)
	result: str = ' '.join(sentences).strip()

	return result

def textFormatter(originalText):
	processText=""
	formattedText=''
	processText = ''.join([line for line in originalText.splitlines() if line.strip()])
	for each in processText.split('.'):
		if(each != ''):
			if(each[0] == ' '):
				formattedText += each[1:] + '.\n'
			else:
				formattedText += each + '.\n'
	return formattedText
