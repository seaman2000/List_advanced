word = input().split()
word_without_vowels = [char for char in word if char.lower() not in ['a', 'o', 'u', 'e', 'i']]
print(word_without_vowels)