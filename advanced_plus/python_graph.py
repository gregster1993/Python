def py_symbols(horiz):
    for number in range(horiz):
        if number == 0 or number == 8:
            print("- " * 21)
        elif number == 1:
            print("o","*" * 5,"*"," ","*","*" * 5,"*","","*","*" * 4,"*","*","*",""," *","o")
        elif number == 2:
            print("|","*","" * 2, " *","*", " ","*",""," *", " ", "*"," *","*","","*","*",""," *",""," *","|")
        elif number == 3:
            print("|","*" * 5,"* " * 3," *", " ", "*"," *","*","","*","*",""," *",""," *","|")
        elif number == 4:
            print("|","*"," " * 6, " *", " ", "*", " ", "*" * 4,"*","","*","*",""," *",""," *","|")
        elif number == 5:
            print("|","*", " " * 6, " *", " ", "*", " ", "*"," *","*","","*","*",""," *",""," *","|")
        elif number == 6:
            print("|","*", " " * 6, " *", " ", "*", " ", "*"," *","*","","*","*",""," *",""," *","|")
        else:
            print("o","* "," "," *" * 3, " ", "*", " ", "*"," *","*" * 4,"*",""," *","*","*","o")

py_symbols(9)