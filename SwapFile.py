def swapfile():
    with open(r"sample1.txt", 'r') as a:
        data_a = a.read()
    with open(r"sample2.txt", 'r') as b:
        data_b = b.read()
    with open(r"sample1.txt", 'w') as a:
        a.write(data_b)
    with open(r"sample2.txt", 'w') as b:
        b.write(data_a)

swapfile()
