

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        anser = int(first_number) / int(second_number)
        print(anser)
    except :
        print('you cant divide by sero')
    # else:
    #     print(anser)


