#Program that takes a strign as input and counts the frequency of each letter using a dictionary
#Print results in alphabetical order

if __name__ == "__main__":
    string = input("Enter a string: ")
    freq_dict = {}
    for char in string.lower():
        if char in 'abcdefghijklmnopqrstuvwxyz':
            if char not in freq_dict:
                freq_dict[char] = 1
            else:
                freq_dict[char] += 1
    
    sorted_chars = sorted(freq_dict.items(), key=lambda x: x[0])
    print("\nCharacter\tFrequency")
    for char, freq in sorted_chars:
        print(f"{char}\t\t{freq}")