"""
Downloads files from a webroot.
BASE_URL - The webroot.
files - The list of files.
completed - The list of downloaded files.
"""

import os

BASE_URL = ''
with open('files', 'r') as filelist:
    for raw_file in filelist:
        song = raw_file.rstrip('\n')
        url = BASE_URL + file
        os.system('wget ' + url)
        a = open('completed', 'a')
        a.write(song + "\n")
        a.close()
