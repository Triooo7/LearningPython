import itertools
from itertools import permutations
list_items = [' - UHZ187', '- XYE08C', '- WJN78N', '- GFF546', '- KHF164']
names = ['Annika - Jessica', 'Peter Her- Raju  - Magnus -  E ', 'Tiago  - Mohammad- Johan Ankner', 'Viktor - Magnus Svantesson -Daniel', 'Martin - Lucia']

for r in itertools.product(names, list_items):
    x = r[0] + r[1]
    print(x)



