import re

file = open("RegEx\\text files\\Test4.txt", 'r')
text = file.read()

spaces = re.findall(r"\s", text)
vowels = re.findall(r"\b[aeiouAEIOU][a-zA-Z]*\b", text)
alice = re.findall("Alice", text)

print(text, "\n")
print("Whitespaces:", len(spaces))
print("Vowel count:", len(vowels))
print("Alice count:", len(alice))

file.close()