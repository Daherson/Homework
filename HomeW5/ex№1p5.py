with open("file1.txt", "w") as the_file:
    while True:
        touch = input("Press enter to exit or write smth")
        if not touch:
            break
        the_file.write(touch + "\n")
        content = the_file.read
        print(content)
the_file.close()