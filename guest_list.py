

# with open ('guest_book.txt', 'a') as file_obect:
#     while True:
#         quest_name = input("please type name and sernme of the quest, if you finishd please type 'end to quite >:")
#         if quest_name == 'end':
#             break
#         file_obect.write(f"Id like to add visitor {quest_name}\n")
#         print(f"We added visitor {quest_name} to our")


print("Podaj dwie liczby, które zostaną podzielone.")
print("Wpisz 'q', aby zakończyć działanie programu.")

while True:
    first_number = input("\nPierwsza liczba: ")
    if first_number == 'q':
        break
    second_number = input("Druga liczba: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    # except ZeroDivisionError:
    except:
        print("Nie można dzielić przez zero!")
    else:
        answer = int(first_number) / int(second_number)
        print(answer)

