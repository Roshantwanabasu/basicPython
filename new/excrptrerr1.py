try:
    file = open("textfile2", "w")
    try:
        file.write("new file written")
    finally:
        print("file written")
        file.close()
except IOError as e:
    print("IO error")