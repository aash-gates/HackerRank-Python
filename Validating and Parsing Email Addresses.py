import re
from email.utils import *
for i in range(int(input())):
    email = parseaddr(input())
    # print email[1]
    # \w is equivalent to a-zA-Z_
    if bool(re.search(r'^[a-zA-Z][\w\-\.]*@[A-Za-z]+\.[a-zA-Z]{1,3}$', email[1])):
        print(formataddr(email))