



sentence = "The quick brown fox jumps over the lazy dog."
# Podpowiedź: W celu wydrukowania wartości w poziomie, zmodyfikuj argument end w funkcji print(). Zajrzyj do
# dokumentacji funkcji print po szczegółowe informacje.

ass = sentence.split()
for i in ass:
    # print(i, end='')
    for j in i :
        print(j,end=',')

print("\n")




ictionaryAngPol = {"appendicitis" : "zapalenie wyrostka robaczkowego", "borscht" : "barszcz", "depend" : "zależeć"}

list_dict = []
second_list =[]
for k, v in ictionaryAngPol.items():
    list_dict.append(k)
    list_dict.append(v)
print(list_dict)

for i in list_dict:
    print(i)
    if " " in i:
        qw = i.split()
        print('text check')
        for el in qw:
            second_list.append(el)

    list_dict.remove(i)

print('pre',list_dict)
print('sec', second_list)


#
# for i in list_dict:
#     if " " in i:
#         for j in i:
#             list_dict.append(j)
#
#
# print(list_dict)