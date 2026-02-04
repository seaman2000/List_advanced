list_of_words = input().split()
palindrome_word = input()

palindrome_words = [word for word in list_of_words if word == word[::-1]]


print(palindrome_words)
print(f"Found palindrome {palindrome_words.count(palindrome_word)} times")
