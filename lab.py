
new_lits = []
ass = 'zapalenie wyrostka robaczkowego'

if " " in ass:
    print('hurra')
    qw = ass.split()
    for el in qw:
        new_lits.append(el)
else:
    print('dupa')

print(new_lits)



list_1 = range(1,20)
for i, num in enumerate(list_1):
    warunek = (i % 3 == 0) and (i % 2 == 0)
    print(warunek)
    if warunek:
        print(f'liczba spelnai warinek {num}')
        print(f'jej miejsce w wektorze {i} ')

przychody = [84757, 54948, 86904, 59980, 20374, 11088, 43246, 13536, 65826, 15734, 53326, 36996]
koszty = [32638, 11634, 35996, 22360, 22806, 49289, 10965, 33326, 44062, 24529, 18493, 55171]
miesiace = ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec', 'Lipiec', 'Sierpień', 'Wrzesień', 'Październik',
            'Listopad', 'Grudzień', ]

# Założenia:
# - podatek CIT płacimy w każdym miesiącu niezależnie,
# - podatek płacimy tylko od dodatniego zysku.

ernigs = {}

for przy, kosz, mies in zip(przychody, koszty, miesiace):
    if przy > kosz:
        ernigs[mies] = 0.9*(przy - kosz)
    else:
        przy - kosz

print(ernigs)
