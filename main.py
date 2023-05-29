"""This program counts the number of vowels in a string."""
def count_vowels(string:str) -> int:
    vogal = 'aeiouAEIOU'
    result = 0
    for i in vogal:
        result += string.count(i)
    return result

if __name__ == "__main__": 
    palavra = input("Digite uma palavra: ")
    print(count_vowels(palavra))
