def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    #STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #STEP 2 and STEP 3 find the average of the middle three scores
    average_score = sum_of_middle_three(score1,score2,score3,score4,score5)/3

    #STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating

def convert_to_numeric(score_raw):
    '''
    type-cast the argument to a float

    :param score_raw: a int, a float or a string representing the score
    :return: a float representing the score in a float
    '''

    score_float = float(score_raw)
    print('score_raw:', score_raw, '[' + str(type(score_raw)) + ']', ' score_float:', score_float)
    return score_float

def sum_of_middle_three(*scores):
    '''
    calculate the sum of three scores in the middle value bound

    :param scores: a list of score values
    :return: a float the result of the sum
    '''
    print('scores:', scores, '[' + str(type(scores)) + ']')
    # tuple(immutable) to list(mutable)
    score_list = list(scores)
    print('score_list:', score_list, '[' + str(type(score_list)) + ']')

    max_score = max(score_list)
    min_score = min(score_list)

    score_list.remove(max_score)
    score_list.remove(min_score)

    return sum(score_list)

def score_to_rating_string(average_score):
    '''
    convert score to the rating comment

    :param average_score: a float or int the score to convert to the rating comment
    :return: a string the rating comment
    '''
    if average_score < 1:
        return 'Terrible'
    elif average_score < 2:
        return 'Bad'
    elif average_score < 3:
        return 'OK'
    elif average_score < 4:
        return 'Good'
    elif average_score < 5:
        return 'Excellent'
    else:
        return None

print(scores_to_rating('5', 4, '3', 2.0, 1.0))
