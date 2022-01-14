# Practicing counter keeping using dictionaries
# used the follow paragraph as an example:
# DO IT, just DO IT! Don’t let your dreams be dreams.
# Yesterday, you said tomorrow. So just. DO IT!
# Make. your dreams. COME TRUE! Just… do it!
# Some people dream of success,
# while you’re gonna wake up and work HARD at it!
# NOTHING IS IMPOSSIBLE!You should get to the point
# where anyone else would quit, and you’re not gonna stop there.
# NO! What are you waiting for? … DO IT! Just… DO IT! Yes you can!
# Just do it! If you’re tired of starting over, stop. giving. up.

# Creats a .csv file called justDoIt.csv
# i - key
# wordcount[i] - value
# len(i) - length of key
# len(wordcount[i]) length of value

paragraph = r"""DO IT, just DO IT! Don’t let your dreams be dreams. 
        Yesterday, you said tomorrow. So just. DO IT! 
        Make. your dreams. COME TRUE! Just… do it! 
        Some people dream of success, 
        while you’re gonna wake up and work HARD at it! 
        NOTHING IS IMPOSSIBLE!You should get to the point 
        where anyone else would quit, and you’re not gonna stop there. 
        NO! What are you waiting for? … DO IT! Just… DO IT! Yes you can! 
        Just do it! If you’re tired of starting over, stop. giving. up."""


def justDoIt(paragraph):
    paraList = paragraph.split() # splits the paragraph into list of words in paraList
    wordcount = {}  # empty dictionary
    for word in paraList: # Creates a key for every value into a list to be able to use .append
        wordcount.setdefault(word, []).append(word)
    
    #tempFile = open('justDoIt.csv', 'x')
    #tempFile.close()

    with open('justDoIt.csv', 'a') as fout: # 'a' allows for appending and creates file if non existant
        fout.write('i \t wordcount[i] \t len(i) \t len(wordcount[i]) \n')
        for i in wordcount:
            fout.write(str(i) + '\t' + str(wordcount[i]) + '\t' + str(
                len(i)) + '\t' + str(len(wordcount[i])) + '\n')

# don't forget to call the function!

def main():
    justDoIt(paragraph)

if __name__ == '__main__':
    main()
