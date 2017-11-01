
# join
print("-".join(["This", "is", "Sparta"]))


# Quiz: Top Three
if False:
    def top_three(input_list):
        """Returns a list of the three largest elements input_list in order from largest to smallest.

        If input_list has fewer than three elements, return input_list element sorted largest to smallest/
        """
        # temp_list = input_list.copy()
        # result_list = []
        #
        # for i in range(3):
        #     max_value = max(temp_list)
        #     result_list.append(max_value)
        #     temp_list.remove(max_value)
        #
        # return result_list
        sorted_list = sorted(input_list, reverse=True)
        return sorted_list[:3]

    print(top_three([2,3,5,6,8,4,2,1]))


# Quiz: Median
if False:
    def median(numbers):
        numbers.sort() #The sort method sorts a list directly, rather than returning a new sorted list
        print(numbers, len(numbers))
        middle_index = int(len(numbers)/2)
        print("middle_index:", middle_index)
        if len(numbers)%2 == 0:
            return sum(numbers[middle_index - 1 : middle_index + 1])/2
        else:
            return numbers[middle_index]

    test1 = median([1,2,3])
    print("expected result: 2, actual result: {}".format(test1))

    test2 = median([1,2,3,4])
    print("expected result: 2.5, actual result: {}".format(test2))

    test3 = median([53, 12, 65, 7, 420, 317, 88])
    print("expected result: 65, actual result: {}".format(test3))

    print("first last".title())


# Quiz: Sum of a List
if False:
    print("\n# Quiz: Sum of a List")
    def list_sum(input_list):
        sum = 0
        # todo: Write a for loop that adds the elements
        # of input_list to the sum variable

        for item in input_list:
            sum += item


        return sum

    #These test cases check the list_sum works correctly
    test1 = list_sum([1, 2, 3])
    print("expected result: 6, actual result: {}".format(test1))

    test2 = list_sum([-1, 0, 1])
    print("expected result: 0, actual result: {}".format(test2))


# Quiz: XML Tag Counter
if False:
    print("\n# Quiz: XML Tag Counter")
    """Write a function, `tag_count`, that takes as its argument a list
    of strings. It should return a count of how many of those strings
    are XML tags. You can tell if a string is an XML tag if it begins
    with a left angle bracket "<" and end with a right angle bracket ">".
    """
    #TODO: Define the tag_count function
    def tag_count(list):
        count = 0
        for element in list:
            if element[0] == '<' and element[-1] == '>':
                count += 1
        return count



    # Test for the tag_count function:
    list1 = ['<greeting>', 'Hello World!', '</greeting>']
    count = tag_count(list1)
    print("Expected result: 2, Actual result: {}".format(count))


# Quiz: Create an HTML List
if False:
    print("\n# Quiz: Create an HTML List")
    '''
    Write the html_list function.
    The function takes one argument, a list of strings, and returns a single string which is an HTML list.
    For example, if the function should produce the following string when provided the list ['first string', 'second string'].
    
    <ul>
    <li>first string</li>
    <li>second string</li>
    </ul>
    '''

    def html_list(text_lines):
        html_text_lines = []
        html_text_lines.append('<ul>')
        for text_line in text_lines:
            html_text_lines.append('<li>' + text_line + '</li>')

        html_text_lines.append('</ul>')

        return '\n'.join(html_text_lines)

    print(html_list(['first string', 'second string']))


# Quiz: Starbox
if False:
    print("\n# Quiz: Starbox")
    '''
    The starbox function in the quiz below prints a box made out of asterisks.
    The function takes two arguments, width and height, that specify how many characters wide the box is and how many lines tall it is.
    The function isn't quite complete: it prints boxes of the correct width, but the height argument is ignored.
    Complete the function so that both of the provided test cases print boxes that are the correct size.
    Hint: The range function could be helpful!
    '''
    def starbox(width, height):
        """print a box made up of asterisks.

        width: width of box in characters, must be at least 2
        height: height of box in lines, must be at least 2
        """
        print("*" * width) #print top edge of box

        # print sides of box
        # todo: print this line height-2 times, instead of three times
        for i in range(height - 2) :
            print("*" + " " * (width-2) + "*")

        print("*" * width) #print bottom edge of box

    # Test Cases
    print("Test 1:")
    starbox(5, 5) # this prints correctly

    print("Test 2:")
    starbox(2, 3)  # this currently prints two lines too tall - fix it!

# Quiz: Nearest Square
if False:
    print("\n# Quiz: Nearest Square")
    '''
    Implement the nearest_square function.
    The function takes an integer argument limit, and returns the largest square number that is less than limit.
    A square number is the product of an integer multiplied by itself, for example 36 is a square number because it equals 6*6.

    There's more than one way to write this code, but I suggest you use a while loop!
    '''
    def nearest_square(limit):
        i = 1
        while i**2 <= limit:
            i += 1
        return (i - 1)**2

    test1 = nearest_square(40)
    print("expected result: 36, actual result: {}".format(test1))


# Stopping for a break
if False:
    print("Stopping for a break")
    manifest = [["bananas", 15], ["mattresses", 34], ["dog kennels",42], ["machine that goes ping!", 120], ["tea chests", 10], ["cheeses", 0]]
    cargo_weight = 0
    cargo_hold = []

    for cargo in manifest:
        print("debug: the weight is currently: {}".format(cargo_weight))
        if cargo_weight + cargo[1] >= 100:
            print("debug: breaking loop now!")
            break
        else:
            print("debug: adding item: {}".format(cargo[0]))
            print("debug: with weight: {}".format(cargo[1]))
            cargo_hold.append(cargo[0])
            cargo_weight += cargo[1]


# Quiz: Break the String
if False:
    print("\n# Quiz: Break the String")
    '''
    Time to write your own loop with a break statement.
    Your task is to create a string, news_ticker that is exactly 140 characters long.
    You should create the news ticker by adding headlines from the headlines list, inserting a space in between each headline.
    If necessary, truncate the last headline in the middle so that news_ticker is exactly 140 characters long.

    Remember that break works in both for and while loops.
    Use whichever loop seems most appropriate.
    Consider adding print statements to your code to help you resolve bugs.
    '''
    headlines = ["Local Bear Eaten by Man",
                 "Legislature Announces New Laws",
                 "Peasant Discovers Violence Inherent in System",
                 "Cat Rescues Fireman Stuck in Tree",
                 "Brave Knight Runs Away",
                 "Papperbok Review: Totally Triffic"]

    news_ticker = ""
    # TODO: set news_ticker to a string that contains no more than 140 characters long.
    # HINT: modify the headlines list to verify your loop works with different inputs
    for i in range(len(headlines)):
        remained_length = 140 - len(news_ticker)
        print("len(news_ticker):", len(news_ticker))
        print("len(headlines[i]):", len(headlines[i]))

        if len(headlines[i]) + 1 <= remained_length:
            if i != 0:
                news_ticker += ' '
            news_ticker += headlines[i]
        else:
            length_to_truncate = len(headlines[i]) - remained_length + 1    # +1 for "space"
            index_of_middle = len(headlines[i])//2
            start_index_to_truncate = index_of_middle - length_to_truncate//2
            end_index_to_truncate = index_of_middle + length_to_truncate//2
            truncated_headline = headlines[i][:start_index_to_truncate] + headlines[i][end_index_to_truncate:]
            print("len(truncated_headline):", len(truncated_headline))
            news_ticker += " " + truncated_headline
            break

    print("len(news_ticker):", len(news_ticker))
    print("news_ticker:", news_ticker)

    # news_ticker_list = []
    # news_ticker_length = 0
    #
    # for headline in headlines:
    #     if news_ticker_length + len(headline) + 1 <= 140:
    #         news_ticker_list.append(headline)
    #         news_ticker_length += len(headline)
    #     else:
    #         break
    #
    # extra_spaces = 140 - news_ticker_length
    # dividing_spaces = len(news_ticker_list) - 1
    # each_padding = extra_spaces//dividing_spaces
    # for i in range(len(news_ticker_list)):
    #     if i != 0:
    #         news_ticker += " " * each_padding
    #         extra_spaces -= each_padding
    #     if i + 1 == len(news_ticker_list):
    #         news_ticker += " " * extra_spaces
    #     news_ticker += news_ticker_list[i]
    #
    # print("len(news_ticker):", len(news_ticker))
    # print("news_ticker:", news_ticker)


'''
Reading the code, is it clear what each piece does? How could it be be easier?
If you needed to change some part of the functionality, would that be easy? Would you have to change the same thing in several places?
If you break down what the function does into steps, how many steps are there? It's best to have each function doing only one thing.
Is there unnecessary repetition? Does every piece of code get used? Could anything be more succinct whilst still being readable? This is called the DRY (Don't Repeat Yourself) principle.

- 읽었을때 명확한가? 어떻게 더 쉽게 할 수 있을까?
- 기능의 일부를 변경하려할 때 쉬울까? 똑같은 수정을 여러군데에다 해야할까?
- 함수를 절차적으로 나누면 얼마나 많은 스텝으로 나누어 질까? 하나의 함수는 하나의 기능을 하는게 최고
- 불필요한 반복이 있는가? 모두다 쓰이는 코드인가? 읽기 쉬우면서도 간결하게 할 수 있을까?
  DRY 원칙을 명심
'''

# Quiz: Refactor the Code
if False:
    print("\n# Quiz: Refactor the Code")
    '''
    This was a pretty long list of ways to improve this code!
    Don't be daunted, we don't have to take them all on at once - in fact, it's better to make one change at a time, and test the results.
    In this quiz, make two changes to the program:
        Move (refactor) the code that checks the answers into a separate function.
        Give it a good name. Use a loop to call that function on each answer, so that there aren't five calls to the function.
        Improve the docstring and add comments to make the code easier to understand.
    This doesn't cover the whole list of improvements, but it's a good start!
    If you want to do more, feel free.
    Your code will be tested on some test cases, so just make sure it still works correctly!
    '''
    def check_answers(my_answers, answers):
        """
        Checks the five answers provided to a multiple choice quiz and returns the results.
        """
        def checking(my_answers, answers):
            correct_count = 0
            for my_answer, answer in zip(my_answers, answers):
                if my_answer == answer:
                    correct_count += 1

            return correct_count

        def scoring(correct_count, total_count):
            if correct_count/total_count > 0.7:
                return "Congratulations, you passed the test! You scored " + str(correct_count) + " out of 5."
            elif (total_count - correct_count)/5 >= 0.3:
                return "Unfortunately, you did not pass. You scored " + str(correct_count) + " out of 5."


        correct_count = checking(my_answers, answers)
        total_count= len(answers)

        return scoring(correct_count, total_count)

    print(check_answers([1, 2, 2, 4, 5], [1, 2, 3, 4, 5]))

# remove_duplicates
if False:
    print("\n# remove_duplicates")

    '''
    Write a function, remove_duplicates that takes a list as its argument and returns a new list containing the unique elements of the original list. 
    The elements in the new list without duplicates can be in any order.

    Suggested test cases:
    Try an input list with no duplicate elements.
    The output list should be the same size as the original list.
    Try a small input list with a known number of unique entries, and some duplicates.
    Verify that the list without duplicates has the correct length.
    '''
    # def remove_duplicates(duplicated_list):
    #     new_list = duplicated_list.copy()
    #     list_size = len(new_list)
    #     i = 0
    #     while i < len(new_list):
    #         for j in range(i + 1, len(new_list)):
    #             if new_list[i] == new_list[j]:
    #                 new_list.pop(j)
    #                 j -= 1
    #         i += 1
    #
    #     return new_list

    def remove_duplicates(duplicated_list):
        new_list = []
        for item in duplicated_list:
            if item not in new_list:
                new_list.append(item)

        return new_list

    list_a = ['Angola', 'Maldives', 'India', 'United States', 'India']
    print("type(list_a):", type(list_a))
    list_b = remove_duplicates(list_a)
    list_c = remove_duplicates(list_b)
    print("list_a:", list_a)
    print("list_b:", list_b)
    print("list_c:", list_c)


# Quiz: Build a Set
if False:
    print("\n# Quiz: Build a Set")
    '''
    In a similar way to building an empty list with my_list = [],
     you can create an empty set with my_set = set().
    Using this technique, and the add method, build a set of all of the square numbers greater than 0 and less than 2,000.
    For reference, I included my implementation of nearest_square function from an earlier quiz.
    You may call the function in your code, integrate it into your code, or ignore it altogether.
    '''

    squares = set()

    # todo: populate "squares" with the set of all of the integers less than 2000 that are square numbers
    i = 1
    while i**2 < 2000:
        squares.add(i**2)
        i += 1

    # Note: If you want to call the nearest_square function, you must define
    # the function on a line before you call it. Feel free to move this code up!
    def nearest_square(limit):
        answer = 0
        while (answer+1)**2 < limit:
            answer += 1
        return answer**2


# Quiz: Define a Dictionary
if False:
    print("\n# Quiz: Define a Dictionary")
    # Define a Dictionary, population,
    # that provides information
    # on the world's largest cities.
    # The key is the name of a city
    # (a string), and the associated
    # value is its population in
    # millions of people.

    #   Key     |   Value
    # Shanghai  |   17.8
    # Istanbul  |   13.3
    # Karachi   |   13.0
    # Mumbai    |   12.5

    population = {
        'Shanghai': 17.8,
        'Istanbul': 13.3,
        'Karachi': 13.0,
        'Mumbai': 12.5,
    }

    print('population:', population)

    print('Seoul' in population)
    print(population.get('Seoul'))
    print(population['Seoul'])


# Quiz: Users by Country
if False:
    print("\n# Quiz: Users by Country")
    '''
    Let's revisit the survey information from earlier.
    Before we used a set to determine how many unique countries were in the dataset.
    Suppose this dataset actually contains information about users who downloaded and installed a certain application:
      for each user that did this their country appears in the list.
    Now let's use a dict to perform a more sophisticated analysis:
      how many users there are from each country?

    Create a dict, country_counts whose keys are country names, and whose values are the number of times the country occurs in the countries list.
    Write your code in the app.py file.
    '''

    from countries import country_list # Note: since the list is so large, it's tidier
                                   # to put in in a separate file. We'll learn more
                                   # about "import" later on.

    country_counts = {}
    for country in country_list:
        #todo: insert countries into the country_count dict.
        # If the country isn't in the dict already, add it and set the value to 1
        # If the country is in the dict, increment its value by one to keep count
        current_count = country_counts.get(country)
        if current_count == None:
            current_count = 0
        country_counts[country] = current_count + 1

    print('country_counts:', country_counts)


# Quiz: Prolific Year
if False:
    print('\n# Quiz: Prolific Year')
    '''
    Write a function most_prolific that takes a dict formatted like Beatles_Discography example above
      and returns the year in which the most albums were released.
    If you call the function on the Beatles_Discography
      it should return 1964, which saw more releases than any other year in the discography.

    If there are multiple years with the same maximum number of releases,
      the function should return a list of years.
    '''
    def most_prolific(discography):
        count_map = {}

        for album in discography:
            year = discography[album]
            if year in count_map:
                count_map[year] += 1
            else:
                count_map[year] = 1

        most_frequent_year = []
        most_frequent_count = 0
        for year in count_map:
            count = count_map[year]
            if most_frequent_count < count:
                most_frequent_year = [year]
                most_frequent_count = count
            elif most_frequent_count == count:
                most_frequent_year.append(year)

        if len(most_frequent_year) > 1:
            return most_frequent_year
        else:
            return most_frequent_year[0]

    Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963,
        "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
        "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
        "Sgt. Pepper's Lonely Hearts Club Band": 1967,
        "Magical Mystery Tour": 1967, "The Beatles": 1968,
        "Yellow Submarine": 1969 ,'Abbey Road': 1969,
        "Let It Be": 1970}
    print("most_prolific(Beatles_Discography):", most_prolific(Beatles_Discography))



# Quiz: Adding Values to Nested Dictionaries
if False:
    print("\n# Quiz: Adding Values to Nested Dictionaries")
    '''
    Try your hand at working with nested dictionaries.
    Add another entry, 'is_noble_gas' to each dictionary in the elements dictionary.
    After inserting the new entries you should be able to perform these lookups:

    >>> print(elements['hydrogen']['is_noble_gas'])
    False
    >>> print(elements['helium']['is_noble_gas'])
    True
    '''

    elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

    # todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
    # hint: helium is a noble gas, hydrogen isn't
    elements['hydrogen']['is_noble_gas'] = False
    elements['helium']['is_noble_gas'] = True


    print(elements['hydrogen']['is_noble_gas'])
    print(elements['helium']['is_noble_gas'])


# Quiz: Flying Circus Records
if False:
    print('\n# Quiz: Flying Circus Records')
    '''
    A regular flying circus happens twice or three times a month.
    For each month, information about the amount of money taken at each event is saved in a list,
      so that the amounts appear in the order in which they happened.
    The months' data is all collected in a dictionary called monthly_takings.

    For this quiz, write a function total_takings that calculates the sum of takings from every circus in the year.
    '''
    monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
                   'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
                   'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
                   'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}

    def total_takings(yearly_record):
        pass # TODO: Implemenent this function
        total = 0
        for month in yearly_record:
            taking_list = yearly_record[month]
            total += sum(taking_list)

        return total

    print(total_takings(monthly_takings))
