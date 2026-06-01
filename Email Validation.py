import re
pattern=r"[a-z A-Z 0-9 _.]+[@][a-z]+[.][a-z]{2,3}"
email="saicharan24@gmail.com"
if re.fullmatch(pattern,email):
    print("valid")
else:
    print("invalid")    