#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  # +++your code here+++
  #mchen - favour early returns to get edge cases out of the way and improve readability 
  if len(s) < 3:
    return s
  if s.endswith('ing'):
    return s + 'ly'
  return s + 'ing'

# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  # +++your code here+++
  #mchen - favour early returns to get edge cases out of the way and improve readability
  # used index instead of find to cause error and return early
  try:
    index_not = s.index('not')
    index_bad = s.index('bad')
  except ValueError:
    return s

  if index_bad < index_not:
    return s

  index_end_of_bad = index_bad + len('bad')
  return s[:index_not] + 'good' + s[index_end_of_bad:]

# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  # +++your code here+++
  def get_front_back(s):
    # s_front = s[:len(s)/2 + len(s) % 2]
    # s_back = s[s.find(s_front) + len(s_front):]
    index_split = len(s)/2 + len(s) % 2
    s_front = s[:index_split]
    s_back = s[index_split:]
    return s_front, s_back
  a_front, a_back = get_front_back(a)
  b_front, b_back = get_front_back(b)
  return a_front + b_front + a_back + b_back


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print 'verbing'
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print
  print 'not_bad'
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")
  test(not_bad("not bad, not bad"), "good, not bad")
  test(not_bad("bad"), "bad")

  print
  print 'front_back'
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
