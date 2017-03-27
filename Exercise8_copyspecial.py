#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import subprocess


"""Copy Special exercise
"""
# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(directory):
  '''returns a list of the absolute paths of the special files in the given
  directory
  '''
  special_paths = []
  filenames = os.listdir(directory)
  _dir = os.path.realpath(directory)
  #                   __word__
  special_path_re = r'__\w+__'
  for filename in filenames:
    special_path_re_match = re.search(special_path_re, filename)
    if special_path_re_match:
      special_paths.append(os.path.join(_dir, filename))
  return special_paths


def copy_to(paths, todir):
  '''given a list of paths, copies those files into the given directory'''
  for path in paths:
    try:
      os.mkdir(todir)
    except OSError:
      shutil.copy(path, todir)


def zip_to(paths, zippath):
  '''given a list of paths, zip those files up into the given zipfile'''
  if os.name == 'posix':
    cmd =  ['zip', '-j', zippath]
  elif os.name == 'nt':
    cmd = ["C:\Program Files\WinRAR\WinRAR.exe", "a", zippath]
  else:
    return
  cmd.extend(paths)
  print "Command I'm going to do %s" % ' '.join(cmd)
  subprocess.Popen(cmd)


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  for directory in args:
    special_paths = get_special_paths(directory)
    if todir:
      copy_to(special_paths, todir)
    elif tozip:
      zip_to(special_paths, tozip)
    else:
      print special_paths

if __name__ == "__main__":
  main()
