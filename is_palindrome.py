#def is_palindrome(word):
#	palindrome = False
#	for i in range(0,len(word)):
#		print(word[i],word[len(word)-i-1],i,len(word)-i-1,sep=', ')
#		if word[i] is word[len(word)-i-1]:
#			palindrome = True
#		else:
#			palindrome = False
#			break
#	return palindrome

def is_palindrome(word):
	revword = word[::-1]
	for i in range(len(word)):
		print('word[i]: {} \t revword[i]: {}'.format(word[i],revword[i]))
		if word[i] is revword[i]:
			pass
		else:
			return False
	return True

print(is_palindrome('racecar'))
print(is_palindrome('world'))
print(is_palindrome('civic'))