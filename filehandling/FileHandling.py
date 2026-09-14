try:
    filename = input("enter the file name: ")

    with open( filename, "r") as myfile:
        content = myfile.read()

    print("myfile: \n")
    print(content)

except FileNotFoundError:
    print("Error : File NOT Found!!")
