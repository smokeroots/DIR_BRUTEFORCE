########################################
# ->         Smoke Root             <- #
# ->                                <- #
# ->       DIR BRUTEFORCE           <- #
# ->          DEVELOPED             <- #
# ->             IN                 <- #
# ->           PYTHON               <- #
# ->                                <- #
# ->       DATE: 08/21/2021         <- #
########################################

import requests

FILE = open('/usr/share/dirbuster/wordlists/directory-list-2.3-small.txt')

LINES = FILE.readlines()

url = '' #LINK EX: http(s)://www.google.com.br/

for LINE in LINES:
    CODE = 404
    if LINE[0] != "#":
        ANSWER = requests.get(url+LINE)
        CODE = ANSWER.status_code
    if CODE != 404 and CODE != 403:
        print url+LINE, CODE