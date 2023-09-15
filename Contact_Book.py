# list of list
names = []
phone_numbers = []
num = 3

for i in range(num):
    name = input("Enter the Name: ")
    phone_number = int(input("Enter the Number: "))

    names.append(name)
    phone_numbers.append(phone_number)

print("\nName\t\t\tPhone Number\n")

for i in range(num):
    print("{}\t\t\t{}".format(names[i], phone_numbers[i]))


# input search term
search_term = input("Input Search Term: ")

if search_term in names:
    index = names.index(search_term)
    phone_number = phone_numbers[index]

    print("Name: {}, Phone_Number: {}".format(search_term, phone_number))

else:
    print("Not found the value")