import numpy as np
desc = ["mobile login form design","desktop login form design","iphone login form design",
		"login form template with just userid and password","dark login page design",
		"login form template with nature background","login form template with captcha"]
		
STOP_WORDS = []
unique_words = set()
for sent in desc:
	words = sent.split(" ")
	for word in words:
		unique_words.add(word)

print(len(unique_words))		
word_dict = {}
i = 0
for each in unique_words:
	word_dict[each] = i
	i+=1
	
print(word_dict)

global_word_vec = []
for each in desc:
	word_vec = []
	words = each.split(" ")
	for i in range(0,8):
		temp = np.zeros(17)
		if i < len(words):
			temp[word_dict[words[i]]] = 1
		
		word_vec+=list(temp)
	
	global_word_vec.append(word_vec)
		
# For each image these word vectors will be used
import os

