from PyDictionary import PyDictionary

INPUT_FILE = 'words_alpha.txt'
OUTPUT_FILE = 'word_meanings.txt'

def fetch_meaning(word):
	"""Fetches the meaning of the word and returns it."""

	dictionary = PyDictionary()
	try:
		return dictionary.meaning(word)
	except Exception:
		pass


def write_meanings_to_file(infile, opfile):
	"""Reads words from input file and write their meaning in output file."""

	opfileobj = open(opfile, 'w+')
	opfileobj.truncate()
	with open(infile, 'r') as infileobj:
		for word in infileobj.readlines():
			print('Current word: {}'.format(word))
			word_meaning = fetch_meaning(word)
			print('Meaning: {}'.format(word_meaning))
			if word_meaning == None:
				continue
			opfileobj.write('{}:{}\n'.format(word.strip('\n'), word_meaning))
	opfileobj.close()


if __name__ == '__main__':
	write_meanings_to_file(INPUT_FILE, OUTPUT_FILE)