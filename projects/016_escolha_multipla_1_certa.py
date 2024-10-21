question="Quanto e 1+1?"
options="a:1, b:2 ou c:3"
print(question)
print(options)
k=input().lower()

while k not in options: #k!=1 or k!=2 or k!=3
    k= (input(question)).lower()

if k=="b":
    print("Correto")
else:
    print("Volta para a primaria.")