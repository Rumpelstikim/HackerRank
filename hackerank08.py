n = int(input().strip())
       
PhoneBook = {}

for i in range(0, n):
    name, number = input().strip().split(" ")
    PhoneBook[name] = number

while True:
    try:
        entry = input().strip()
        if entry in PhoneBook.keys():
            print("{}={}".format(entry, PhoneBook[entry]))
        else:
            print("Not found")
    except EOFError:
        break

