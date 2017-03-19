#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
  # +++your code here+++
  # for i, num in enumerate(nums):
  #   next = i + 1
  #   while next < len(nums):
  #     if num == nums[next]:
  #       nums[next] = 'to_remove'
  #       next += 1
  #     else:
  #       break
  # return [num for num in nums if num != 'to_remove']
  no_adj = []
  for i in nums:
    if len(no_adj) == 0 or i != no_adj[-1]:
      no_adj.append(i)
  return no_adj


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
  # +++your code here+++
  # the fastest sorts are O(n log(n)) which is slower than linear
  # https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt
  
  #method0 - bad
  #list1.extend(list2) return sorted(list1)

  #method1 - bad
  # index_counter = 0
  # for i in list1:
  #   try:
  #     while True:
  #       if i < list2[index_counter]:
  #         list2.insert(index_counter, i)
  #         break
  #       else:
  #         index_counter += 1
  #   except IndexError:
  #     #nothing to compare in list1, every i is now bigger than previous
  #     list2.append(i)
  # return list2

  #method google
  # while len(list1) and len(list2):
  # if list1[-1] > list2[-1]:
  #   result.append(list1.pop())
  # else:
  #   result.append(list2.pop()) 
  # result.extend(list1)  
  # result.extend(list2)
  # reversed(result)

  merged_list = []
  index1_count = 0
  index2_count = 0
  while True:
    try:
      if list1[index1_count] <= list2[index2_count]:
        merged_list.append(list1[index1_count])
        index1_count += 1
      #get in the habit of seeing if you can use "else"
      else:
        merged_list.append(list2[index2_count])
        index2_count += 1
    except IndexError:
      if index1_count == len(list1):
        merged_list.extend(list2[index2_count:])
      else:
        merged_list.extend(list1[index1_count:])
      break
  return merged_list

#Below note is from google against unknown solution
# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Calls the above functions with interesting inputs.
def main():
  print 'remove_adjacent'
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  print
  print 'linear_merge'
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()
