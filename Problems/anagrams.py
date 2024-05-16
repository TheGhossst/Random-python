#Check if two strings are anagrams of each other or not
#Time complexity -> O(nlogn)

def anagram(string1, string2):
    if len(string1) != len(string2):
        return -1
    
    if sorted(string1) == sorted(string2):
       return 0
        
    return -1

if __name__ == "__main__":
    string1 = input()
    string2 = input()
    result = anagram(string1, string2)
    if result == 0:
        print("Anagram")
    else:
        print("Not Anagram")
            