import string
from _ast import List


def replace_letter(letter_to_replace, letter_to_replace_with):
    for k in range(len(a)):
        a[k].replace(f"{letter_to_replace.lower()}", f"{letter_to_replace_with.upper()}")
a= ["There acdgiER HERE\n" "lEEdfEmEnTH THE\n"
    "coRqnpEncgoRpE\n" "EsacTciEHnbEfoaut\n"
    "THREE REcEnRpH\n"
    "qnpauataEccgnR\n"
    "foTaqwjpguuEnvoEc\n"
    "vET THE arinjiEiauu\n"
    "pgwEnEnjiaTHwErg\n"
    "THE juocTnREmgt\n"
    "nfuETgcEEwjbacagm\n"
    "THacpgovlpHnmvE\n"
    "EbERjoapzTgqEnR\n"
    "nREjoapztgqEnR\n"
    "iEmEEllgofuE THE\n"
    "REcEnRpH"]
abc=List(string.ascii_lowercase)
print(abc)
i=0
indices_a= []
indices_b=[]
for r in range(len(abc)):
    a.count(a[r])== abc[r]
    print(abc[r])
while i <= 1:
    a_input=  input("letter_to_replace: ")
    b_input=  input("letter_to_replace_with: ")
    if a_input=="end":
        break
    replace_letter(a_input,b_input)
    indices_a.append(a_input)
    indices_b.append(b_input)
    print(a)

