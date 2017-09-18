import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('word', help='fetch meaning of given word', type=str)
args = parser.parse_args()

word = args.word
print(word)
with open('word_meanings.txt', 'r') as fileobj:
	meaning_text = re.search(r'{}:(.+)'.format(word), fileobj.read()).group()
	type_of_speech, meanings = meaning_text.strip('{}').split(':')
	print('({})'.format(type_of_speech))
	meanings = meanings.strip('[] ').split(',')
	for counter, meaning in enumarate(meanings, 1):
		print('{}. {}'.format(counter, meaning))


	

