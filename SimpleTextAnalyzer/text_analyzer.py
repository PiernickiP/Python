punctuation = [".", ",", "!", "?"]
sentence = input("Type text for basic analysis: ")

letters = len(sentence)
print(f"Your text has {letters} marks.")

words = len(sentence.split(" "))
print(f"Your text has {words} words.")

counter = 0
for item in sentence:
    if item in punctuation:
        counter += 1

print(f"Your text has {counter} punctuatuion/s.")

reversed_sentence = sentence[::-1].lower()
if sentence.lower() == reversed_sentence:
    print("Your text is a palidrome.")
else:
    print("Your text is not a palidrome.")
