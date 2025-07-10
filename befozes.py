uveg=[5, 2, 2, 4, 3, 2, 4, 10, 5, 5, 3, 5, 4, 3, 3]
print("2.feladat")
while True:
    lekvar=int(input("Mari néni lekvárja (dl):"))
    if lekvar<=200:
        break
    if lekvar>0:
        break

print("3.feladat")
/*megjegyzés*/
max=uveg[0]
imax=0
for i in range(len(uveg)):
    if uveg[i]>max:
        max=uveg[i]
        imax=i
print(f"A legnagyobb üveg {max} dl és a {imax+1}.soban van")

if lekvar<sum(uveg):
    print("Elegendő üveg volt")
else:
    print("Maradt lekvár")
print("megfőztem")
