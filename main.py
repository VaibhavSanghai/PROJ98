def swapFileData():
    file1 = input("original file : ")
    file2 = input("swapped file : ")

    with open(file1, 'r') as a:
        data_a = a.read()

    with open(file2, 'r') as b:
        data_b = b.read()
        
    with open(file1, 'w+') as a:
        a.write(data_b)

    with open(file2, 'w+') as b:
        b.write(data_a)

    print("file1", file1)
    print("file2", file2)
    print("data1", data_a)
    print("data2", data_b)

swapFileData()
