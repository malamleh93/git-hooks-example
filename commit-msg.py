#!/usr/bin/env python

import sys

COMMIT_MESSAGE_TITLE_MAX_LENGTH = 50
COMMIT_MESSAGE_TITLE_MIN_LENGTH = 15
COMMIT_MESSAGE_TITLE_MIN_NUMBER_OF_WORDS = 3
COMMIT_MESSAGE_DESCRIPTION_LENGTH = 72

def check_format_rules(lineno, line):
	real_lineno = lineno + 1
	if lineno == 0:
		if len(line) > COMMIT_MESSAGE_TITLE_MAX_LENGTH:
			return "Error %d: First line should be less than %d characters in length." % (real_lineno, COMMIT_MESSAGE_TITLE_MAX_LENGTH)
		if len(line) < COMMIT_MESSAGE_TITLE_MIN_LENGTH:
			return "Error %d: First line should be greater than %d characters in length." % (real_lineno, COMMIT_MESSAGE_TITLE_MIN_LENGTH)
		if len(line.split(" ")) < COMMIT_MESSAGE_TITLE_MIN_NUMBER_OF_WORDS:
			return "Error %d: The number of words in the first line should be greater than %d words." % (real_lineno, COMMIT_MESSAGE_TITLE_MIN_NUMBER_OF_WORDS)

		if(line[0].isupper() == False):
			return "Error %d: First letter in the first line should be uppercase." 
	if lineno == 1:
		if line:
			return "Error %d: Second line should be empty." % (real_lineno)
	
	if not line.startswith('#'):
		if len(line) > COMMIT_MESSAGE_DESCRIPTION_LENGTH:
			return "Error %d: No line should be over %d characters long." % (real_lineno, COMMIT_MESSAGE_DESCRIPTION_LENGTH)
	return False

def main(message_file):
	commit_msg = list()
	errors = list()

	with open(message_file) as commit_fd:
		for lineno, line in enumerate(commit_fd):
			stripped_line = line.strip()
			commit_msg.append(line)
			e = check_format_rules(lineno, stripped_line)
			if e:
				errors.append(e)
	
	if errors:
		#with open(message_file, 'w') as commit_fd:
		print('%s' % '# GIT COMMIT MESSAGE FORMAT ERRORS:')
		for error in errors:
			print('# %s' % (error,))

		sys.exit(1)



if __name__ == "__main__":
	main(sys.argv[1])