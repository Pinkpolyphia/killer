# n = int(input("Type a number: "))
# # print("hello, " + a) 
# if n > 0:
#     print(f"{n} is positive")
# elif n < 0:
#     print(f"{n} is negative")
# else:
#     print("that's 0 you silly")

# l = "Laura"
# for i in range(len(l)):
#     print(l[i])
# print(f"Go {l}!")

wish = []
i = ""
while i != "t":
    i = input("Type p to see the list or e to edit the list or t to end: ")
    try:
        if i == "p":
            print(wish)
            i = ""
        elif i == "e":
            i = ""
            ii = input("Type a to append or r to remove ")
            try:
                if ii == "a":
                    wish.append(input("Enter your band: "))
                    ii = ""
                elif ii == "r":
                    n = input("which wish would you like to remove? ")
                    wish.remove(wish[n])
                    ii = ""
            except ii != "a":
                ii = ""
                print("that's not an option bitch")
    except i != "p" or "e" or "t":
        print("that's not an option bitch")
print("Thank you and may your wish happen soon!")