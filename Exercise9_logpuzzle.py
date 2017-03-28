#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
import urlparse

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order. (If url has the pattern "-wordchars-wordchars.jpg" then
  it should be sorted with the "second" wordchars)"""
  #GET /edu/languages/google-python-class/images/puzzle/p-biai-bacj.jpg HTTP
  #if ufile.info().gettype() == 'text/plain'
  #if ufile.info().gettype() == 'text/html':

  def sort_multi_word(full_url):
    '''match multi-worded image of a-b-c.jpg using "c" '''
    #                          words?-words-(words).jpg
    multi_w_match = re.search('\w*-\w+-(\w+)\.jpg', os.path.basename(full_url))
    if multi_w_match:
      return multi_w_match.group(1)
    else:
      return full_url

  result_urls = []
  ufile = urllib.urlopen(filename)
  text = ufile.read()
  #                            GET (non-whitepuzzlenon-white) HTTP
  url_re_matches = re.findall('GET\s(\S*puzzle\S*)\sHTTP', text)
  for url in url_re_matches:
    full_url = urlparse.urljoin('http://code.google.com', url)
    if full_url not in result_urls:
      result_urls.append(full_url)
  return sorted(result_urls, key=sort_multi_word)


def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  index.html looks like:
  # <html><body>
  # <img src="img0"><img src="img1">...
  # </body></html>
  """
  img_htmls = []
  index_html = ''
  try:
    os.mkdir(dest_dir)
  except OSError:
    pass
  for index, url in enumerate(img_urls):
    img_name = 'img%s' % index
    img_dest = os.path.join(dest_dir, img_name)
    img_htmls.append('<img src="%s">' % img_name)
    if not os.path.exists(img_dest):
      print "Retrieving... %s" % url
      urllib.urlretrieve(url, img_dest)

  with open(os.path.join(dest_dir, 'index.html'), 'a+') as f:
    index_html ='''
    <html><body>
    %s
    </body></html>''' % ''.join(img_htmls)

    f.write(index_html)


def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
