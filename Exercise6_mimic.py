#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys


def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it.
  Where first key word is ''
  """
  with open(filename, 'rU') as f:
    text = f.read().split()
    mimics = {'': [text[0]]}
    for index, word in enumerate(text):
      try:
        next_word = text[index+1]
      except IndexError:
        break
      if word not in mimics:
        mimics[word] = [next_word]
      else:
        mimics[word].append(next_word)
  return mimics

def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words.
  Where it defaults back to key word '' when it hits a word not in mimic_dict
  """
  output = []
  linebreak_count =  1

  for i in range(200):
    if len(mimic_dict.get(word, [])):
      word = random.choice(mimic_dict[word])
    else:
      word = random.choice(mimic_dict[''])
    output.append(' ')
    output.append(word)

    if len(''.join(output)) >= linebreak_count * 70:
      output.append('\n')
      linebreak_count += 1

  print ''.join(output)


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print 'usage: ./mimic.py file-to-read'
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
