import pyperclip as pc
import re
import sys

while True:
    s = re.findall("[^0-9]", input().strip().lower())
    if "".join(s) == "paswordhax": 
        sys.exit("omg u found hax")

    out = ""

    for c in s:
        if c != " ":
            out += f":regional_indicator_{c}: "
        else:
            out += "      "

    pc.copy(out)        