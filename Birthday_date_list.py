# Create lists with 5 empty spaces
names = ["", "", "", "", ""]
birthdays = ["", "", "", "", ""]

# Take input
for i in range(5):
    names[i] = input("Name: ")
    birthdays[i] = input("Birthday: ")

# Print output
print("\nBirthday List:")

for i in range(5):
    print(names[i], birthdays[i])
