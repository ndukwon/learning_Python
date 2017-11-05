
# Quiz: Days and Hours
if False:
    print("\n# Quiz: Days and Hours")
    '''
    Try your hand at writing a function that uses a tuple to return multiple values.
    Write an hours2days function that takes one argument, an integer, that is a time period in hours.
    The function should return a tuple of how long that period is in days and hours, with hours being the remainder that can't be expressed in days.
    For example, 39 hours is 1 day and 15 hours, so the function should return (1,15).

    These examples demonstrate how the function can be used:
    >>> hours2days(24) # 24 hours is one day and zero hours
    (1, 0)
    >>> hours2days(25) # 25 hours is one day and one hour
    (1, 1)
    >>> hours2days(10000)
    (416, 16)
    '''

    def hours2days(time_in_hour):
        hours_a_day = 24
        days = time_in_hour // hours_a_day
        hours = time_in_hour % hours_a_day

        return days, hours

    print(hours2days(24))
    print(hours2days(25))
    print(hours2days(10000))


# Quiz: Default Arguments
if False:
    print("\n# Quiz: Default Arguments")
    '''
    print_list is a function that takes a list as its input and prints it line by line as a numbered or bulleted list.
    It takes three arguments:
        l: The list to print
        numbered: set to True to print a numbered list.
        bullet_character: The symbol placed before each list element. This is ignored if numbered is True.
    This function is pretty cumbersome to call.
    It requires a bullet_character even if the user wants a numbered list!

    Make the function easier to use by adding default arguments.
    By default the function should produce a bulleted list, and the default bullet character should be "-".
    
    After your changes, the function should behave like this:
    
    >>> print_list(["cats", "in", "space"])
    - cats
    - in
    - space
    >>> print_list(["cats", "in", "space"], True)
    1: cats
    2: in
    3: space
    '''

    def print_list(l, numbered=False, bullet_character='-'):
        """Prints a list on multiple lines, with numbers or bullets

        Arguments:
        l: The list to print
        numbered: set to True to print a numbered list
        bullet_character: The symbol placed before each list element. This is
                          ignored if numbered is True.
        """
        for index, element in enumerate(l):
            if numbered:
                print("{}: {}".format(index+1, element))
            else:
                print("{} {}".format(bullet_character, element))


    print(print_list(["cats", "in", "space"]))
    print(print_list(["cats", "in", "space"], True))


# Quiz: Flying Circus cast list
if False:
    print("\n# Quiz: Flying Circus cast list")
    '''
    You're going to create a list of the actors who appeared in the television programme Monty Python's Flying Circus.

    Write a function called create_cast_list that takes a filename as input and returns a list of actors' names.
    It will be run on the file flying_circus_cast.txt (this information was collected from imdb.com).
    Each line of that file consists of an actor's name, a comma, and then some (messy) information about roles they played in the programme.
    You'll need to extract only the name and add it to a list.
    You might use the .split() method to process each line.
    '''

    def create_cast_list(filename):
        cast_list = []
        #use with to open the file filename
        #use the for loop syntax to process each line
        #and add the actor name to cast_list


        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                element_list = line.split(',')
                cast_list.append(element_list[0])

        return cast_list

    print(create_cast_list('flying_circus_cast.txt'))


# Quiz: Compute an Exponent
if False:
    print("\n# Quiz: Compute an Exponent")
    '''
    It's your turn to import and use the math module.
    Use the math module to calculate e to the power of 3.
    print the answer.

    Refer to the math module's documentation to find the function you need!
    '''

    import math

    print(math.exp(3))


# Quiz: Password Generator
if True:
    print("\n# Quiz: Password Generator")
    '''
    Write a function called generate_password
      that selects three random words from a provided file of words
      and concatenates them into a single string.
    The code to read in the data from the file is already in the starter code,
      you will need to build a password out of these parts.
    '''
    # Use an import statement at the top
    import random

    word_file = "words.txt"
    word_list = []

    #fill up the word_list
    with open(word_file,'r') as words:
        for line in words:
            # remove white space and make everything lowercase
            word = line.strip().lower()
            # don't include words that are too long or too short
            if 3 < len(word) < 8:
                word_list.append(word)

    # Add your function generate_password here
    # It should return a string consisting of three random words
    # concatenated together without spaces
    def generate_password():
        selected_words = []

        # while len(selected_words) < 3:
        #     selected_index = random.randint(0, len(word_list) - 1)
        #     selected_word = word_list[selected_index]
        #     if selected_word in selected_words:
        #         continue
        #
        #     selected_words.append(selected_word)
        selected_words = random.sample(word_list, 3)

        return ''.join(selected_words)

    print(generate_password())
