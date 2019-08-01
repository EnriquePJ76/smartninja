"""
import mimodulo.funcs as f

f.hello()
f.bye()

f.hello_by_name("Pepe")
f.hello_by_name("Antonio")
n = "Maria"
f.hello_by_name(n)
f.hello_by_name(2.3)
f.hello_by_name(name="Marisa")


print(f.mifunc(2, 1, 3))
print(f.mifunc(2, 1))
print(f.mifunc(2))

print(f.mifunc(2, val2=3))
print(f.mifunc(val1=2,val2=3))
print(f.mifunc()+5)

print(f.mifunc5(2, 1, 3))
"""

import mimodulo.funcs as f

top=30
filename = "score_data.json"

score_list = f.get_score(filename)

f.score_top_print(score_list)

secret = f.get_secrect(top)

while True:
    input("Dame un número para acertar el secreto: ")

    f.save_score(filename, score_list)





















