# “Write a function that takes camel cased strings (i.e. ThisIsCamelCased),
# and converts them to snake case (i.e. this_is_camel_cased).
# Modify the function by adding an argument, separator, so it will also convert
# to kebab case (i.e. this-is-camel-case) as well.”

def convert(word, seperator="_"):
	n = len(word)
	change = list(word)
	converted = ""
    #print("{} is the length".format(n))
	#print("{} is the {} converted to a list".format(change,word))
	while n > 1:
		if change[n-1].isupper():
			change.insert(n-1,seperator)
		n -= 1
	#print("{} is the snake cased list.".format(change))
	for letter in change:
		converted += str(letter)
	#print("{} is the string.".format(converted))
	
	return converted.lower()


word = "ThisIsCamelCased"
snake = convert(word)
kebab = convert(word,"-")
print("Camel case: {}".format(word))
print("Snake case: {}".format(snake))
print("Kebab case: {}".format(kebab))