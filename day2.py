# 1. Indexing and Slicing
#    Given the string s = "PythonPractice", what are the outputs of:
#    - s[1]
#    - s[-3:]
#    - s[2:7]

# s = "PythonPractice"

# print(s[1])      
# print(s[-3:])    
# print(s[2:7])   



# 2. Reverse a String
#    Write a one-liner to reverse the string "developer" using slicing.
# print("developer"[::-1])
 

# 3. Count Vowels
#    Write a function that counts the number of vowels in a given string.
# def count_vowels(s):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in s:
#         if char in vowels:
#             count += 1
#     return count
# print(count_vowels("Python Practice"))  


# 4. Check for Palindrome
#    Write a function to check if a given string is a palindrome. Ignore spaces and capitalization.
# def is_palindrome(s):
#     cleaned = ''.join(s.split()).lower()  
#     return cleaned == cleaned[::-1]
# print(is_palindrome("Racecar"))          
# print(is_palindrome("A man a plan a canal Panama"))  
# print(is_palindrome("Hello")) 




#  5. Clean and Format String
#    Given text = "   hello world! welcome to Python.   ", write code to:
#    - Remove leading/trailing spaces
#    - Capitalize each word
#    - Replace the word "Python" with "Programming   
# text = "   hello world! welcome to Python.   "
# text = text.strip()
# text = text.title()
# text = text.replace("Python", "Programming")

# print(text)


# 6. Find Longest Word
#    Write a function that takes a sentence and returns the longest word in it.
# def find_longest_word(sentence):
#     words = sentence.split()
#     longest = max(words, key=len)
#     return longest
# print(find_longest_word("I love programming in Python"))  


# 7. String Operators
#    Given s1 = "Py" and s2 = "thon", what are the results of:
#    - s1 + s2
#    - s1 * 3
#    - "y" in s1
# s1 = "Py"
# s2 = "thon" 
# print(s1 + s2)

# 8.Remove Duplicate Characters
#    Write a function that removes all duplicate characters from a string but keeps the first occurrence.
# def remove_duplicates(s):
#     result = ""
#     seen = set()
#     for char in s:
#         if char not in seen:
#             result += char
#             seen.add(char)
#     return result
# print(remove_duplicates("programming"))  


# 9. Check for Anagram
#    Write a function that returns True if two strings are anagrams of each other.
# def are_anagrams(s1, s2):
#     s1_clean = s1.replace(" ", "").lower()
#     s2_clean = s2.replace(" ", "").lower()
#     return sorted(s1_clean) == sorted(s2_clean)
# print(are_anagrams("listen", "silent"))         
# print(are_anagrams("hello", "world"))            
# print(are_anagrams("Dormitory", "Dirty room"))  


# 10. Word Frequency Counter
#     Write a function that takes a sentence and returns a dictionary of word frequencies.
# def word_frequency(sentence):
#     words = sentence.lower().split()
#     freq = {}
#     for word in words:
#         freq[word] = freq.get(word, 0) + 1
#     return freq
# print(word_frequency("This is a test. This test is simple."))