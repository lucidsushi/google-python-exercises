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

# get_special_paths(dir) -- returns a list of the absolute paths of the special
  #files in the given directory

# copy_to(paths, dir) given a list of paths, copies those files into the given
  #directory

# zip_to(paths, zippath) given a list of paths, zip those files up into the
  #given zipfile
def get_special_paths(dir):
  special_paths = []
  filenames = os.listdir(dir)
  for filename in filenames:
    #                 word?__word__.ext
    special_path_re = r'\w*__\w+__\.\w+'
    special_path_re_match = re.search(special_path_re, filename)
    if special_path_re_match:
      special_paths.append(os.path.abspath(special_path_re_match.group()))
  return special_paths



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
  for filepath in args:
    special_paths = get_special_paths(filepath)

    if todir:
      for path in special_paths:
        try:
          os.mkdir(todir)
        except WindowsError:
          shutil.copy(path, todir)

    elif tozip:
      special_paths = ["%s" % s for s in special_paths]
      cmd = ["C:\Program Files\WinRAR\WinRAR.exe", "a", "%s" % tozip]
      cmd.extend(special_paths)
      print "Command I'm going to do %s" % cmd
      #(status, output) = commands.getstatusoutput(cmd)
      subprocess.Popen(cmd)

    else:
      print special_paths
  
if __name__ == "__main__":
  main()
