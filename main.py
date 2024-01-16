# 1.

input_string = list(input("Enter the string 'Python': "))
if len(input_string) >= 2:
    del input_string[:2]
    reversed_string = ''.join(reversed(input_string))
    print("Sample output:")
    print(reversed_string)
else:
    print("Input string should have at least 2 characters.")

# 2.

sentence = input("Enter a sentence: ")
modified_sentence = sentence.replace('python', 'pythons')
print("Sample output:")
print(modified_sentence)

# 3.

score = float(input("Enter the class score: "))

if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
else:
    grade = 'F'

print("Letter Grade:", grade)
