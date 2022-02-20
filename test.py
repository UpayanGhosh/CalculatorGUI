import re
import math

def replace(expression):
    # Replace the sqrt symbol with the sqrt funcion from the math module
    return eval(re.sub(r'√(\d+)', r'math.sqrt(\1)', expression))
   
# print(replace("√100"))                  # 10.0
# print(replace("√25 + √36"))             # 11.0
# print(replace("2+346-677*78/6+√567+7")) # -8422.188238200419


mystr= "8+8+√9"

patt = re.compile(r'√')

matches = patt.finditer(mystr)
for match in matches:
    print(replace(mystr))