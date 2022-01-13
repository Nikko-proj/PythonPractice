# “Write a function to write a comma separated value (CSV) file.
# It should accept a filename and a list of tuples as parameters.
# The tuples should have a name, address, and age.
# The file should create a header row followed by a row for each tuple.
# If the following list of tuples was passed in:

# [('George', '4312 Abbey Road', 22),
# ('John', '54 Love Ave', 21)]
# it should write the following in the file:

# name,address,age
# George,4312 Abbey Road,22
# John,54 Love Ave,21”

import os.path


def get_file_name():
    '''
    Asks user for file name and type
    '''
    name = input("Enter the name of your file: ")
    ext = input("Enter the extension (ex. .txt or .csv): ")
    return name+ext


def check_exist(filename):
    '''
    Returns result of os.path.exists()
    '''
    return os.path.exists(filename)


def create_file(filename):
    '''
    Checks if file exists before creation
    '''
    if check_exist(filename) is True:
        print("{} already exists!".format(filename))
    else:
        tempOpen = open(filename, mode='x')
        # 'x' create a new file and open it for writing
        tempOpen.close()
        # close file


def write_header(filename):
    '''
    Writes required header
    '''

    with open(filename, 'w') as fout:
        fout.write('Name\tAddress\tAge\n')


def write_file(filename, info):
    '''
    Writes to file
    '''
    write_header(filename)
    # info will be in ([name,address,age]) format
    with open(filename, 'a') as fout:  # append to file
        for name, place, age in info:
            fout.write(name+'\t'+place+'\t'+age+'\n')


filename = get_file_name()  # object to hold file name
myFriends = (['Kirby', 'Best House', '2'],
             ['Duke', 'Cool House', '13'],
             ['Toldo', 'Super House', '3'])  # tuple of information
print(filename)  # prints filename
print(check_exist(filename))  # prints if it exists
create_file(filename)  # creates file if it does not exist
print(check_exist(filename))  # should return True
write_file(filename, myFriends)  # writes to file
