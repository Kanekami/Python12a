from bdb import Breakpoint


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
i=0
indice= []
while i <= 1:
    b=  input("letter_to_replace: ")
    c=  input("letter_to_replace_with: ")
    if b=="end":
        break
    replace_letter(b,c)
    print(a)

