def replace_letter(letter_to_replace, letter_to_replace_with):
    for k in range(len(a)):
        a[k] = a[k].replace(f"{letter_to_replace.lower()}", f"{letter_to_replace_with.upper()}")
a= ["There ac dgiER HERE" 
    "lEEd fEmEnTH THE"
    "coRqnpEncgo RpE" 
    "EsacTciEHnbEfoaut"
    "THREE REcEnRpH"
    "qnpauataEccgnR"
    "foTaqwjpguuEnvoEc"
    "vET THE arinjiEiauu"
    "pgwEnEnjiaTHwErg"
    "THE juocTnREmgt"
    "nfuETgcEEwjbacagm"
    "THacpgovlpHnmvE"
    "EbERjoapzTgqEnR"
    "nREjoapztgqEnR"
    "iEmEEllgofuE THE"
    "REcEnRpH"]
abc = list(map(chr, range(97, 123)))
i=0
indices_a= []
indices_b=[]
for r in range(len(abc)):
    letter_count = a.count(abc[r])
    print(f"{abc[r]}: {letter_count}")
while i <= 1:
    a_input=  input("letter_to_replace: ")
    b_input=  input("letter_to_replace_with: ")
    if a_input=="end":
        break
    replace_letter(a_input,b_input)
    indices_a.append(a_input)
    indices_b.append(b_input)
    print(a)

