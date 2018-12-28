try:
    file = open("testfile.txt","w")
    file.write("this is a brand new file")
#except IOError as e:
#    print("there was an IO error")
#else:
#    print("the file was written")
#    file.close()
finally:
    print("clearly goes on")
    file.close()

