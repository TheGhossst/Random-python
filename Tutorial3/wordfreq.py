if __name__ == "__main__":
    d = {}
    string = input("Enter the string: ")
    lst = string.split()
    for word in lst:
        if word not in d.keys():
            d[word] = 1
        else:
            d[word] += 1
    print(d.items())