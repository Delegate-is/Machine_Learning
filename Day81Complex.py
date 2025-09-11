# program to get 5 no and store in list, then convert to pandas series to change default indexes to alpha
import pandas as pd
list_1 = []
for i in range(5):
    list_1.append(i)
    print(list_1)
ps = pd.Series(list_1)
print("Pandas Items" +str(ps))
ps_ = pd.Series(list_1, index=['a','b','c','d','e'])
print(ps_)

# Programe to find keyword density in an article
para = input("Enter a paragraph: ")
word = input("Enter a word to find density: ")
sp = 0
for i in para:
    if i == " ":
        sp += 1
total_words = sp + 1
print("Total Words = "+str(total_words))
user_word = para.count(word)
print("User Word Occurences = "+str(user_word))

keyword_density =(user_word / total_words) * 100
print("Keyword Density = "+str(keyword_density)+"%")
if keyword_density >= 3:
    print("Density is above 3%!")