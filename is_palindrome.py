def is_palindrome(word):
	palindrome = False
	for i in range(0,len(word)):
		print(word[i],word[len(word)-i-1],i,len(word)-i-1,sep=', ')
		if word[i] is word[len(word)-i-1]:
			palindrome = True
		else:
			palindrome = False
			break
	return palindrome


print(is_palindrome('racecar'))
print(is_palindrome('world'))
print(is_palindrome('civic'))