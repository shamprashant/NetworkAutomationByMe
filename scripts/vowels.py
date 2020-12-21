def is_valid_word(word):
	vowels = 'aeiou'

	alpha_dict = {}

	for char in word:
		alpha_dict[char] = alpha_dict.get(char,0) + 1

	for vowel in vowels:
		if vowel not in alpha_dict or alpha_dict[vowel] != 1:
			return False
			
	return True

if __name__ == '__main__':

	with open('words.txt','r') as file:
		for word in file:
			if is_valid_word(word.lower()):
				print(word.strip())








