'''
Alphabetizer Project
Order a list of words in alphabetical order from a roster using merge sort
'''


class Person:
    '''
    This class defines first name, last, name, and email for the user
    '''

    def __init__(self, first, last, email):
        self.first = first
        self.last = last
        self.email = email

    def __str__(self):
        return '{0} {1} <{2}>'.format(self.first, self.last, self.email)

    def __repr__(self):
        return '({0}, {1}, {2})'.format(self.first, self.last, self.email)

    def __eq__(self, other):
        return self.first == other.first and self.last == other.last and self.email == other.email


def merge_sort(sorted_roster, ordering):
    '''
    Sorts the roster in alphabetical order
    :param roster: the list of names
    :param ordering: a way to compare names
    '''

    if len(sorted_roster) <= 1:  # if the roster only has one name
        return sorted_roster, 0

    # else - split your list in half and order the list
    mid = len(sorted_roster) // 2  # split list into half
    left_half = sorted_roster[:mid]  # creates left side
    right_half = sorted_roster[mid:]  # creates right side

    left_half, left_comparison = merge_sort(left_half, ordering)
    right_half, right_comparison = merge_sort(right_half, ordering)

    # left and right comparison keep a track of the comparison count

    i = 0
    j = 0
    k = 0

    comparison = 0

    while i < len(left_half) and j < len(right_half):
        # left side is less than the right side, if a<b
        if ordering(left_half[i], right_half[j]):
            sorted_roster[k] = left_half[i]
            # update list so first name is added to front
            comparison += 1
            i += 1

        elif ordering(right_half[j], left_half[i]):  # accounting for if b <a
            sorted_roster[k] = right_half[j]
            # update list so last name is added to front
            comparison += 1
            j += 1

        else:
            sorted_roster[k] = left_half[i]  # accounts for a = b
            i += 1
            comparison += 5
        k += 1

    while i < len(left_half):
        sorted_roster[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        sorted_roster[k] = right_half[j]
        j += 1
        k += 1

    return sorted_roster, comparison + left_comparison + right_comparison


def order_first_name(a, b):
    """
    Orders two people by their first names
    :param a: a Person
    :param b: a Person
    :return: True if a comes before b alphabetically and False otherwise
    """

    if a.first == b.first:  # if they are the same first name

        if a.last < b.last:
            # if first last name comes before second last name
            # in alphabetical order
            return True  # a comes before b

        return False  # other wise b comes before a

    if a.first < b.first:
        return True  # a comes before b

    return False  # b comes before a


def order_last_name(a, b):
    """
    Orders two people by their last names
    :param a: a Person
    :param b: a Person
    :return: True if a comes before b alphabetically and False otherwise
    """

    if a.last == b.last:  # if last names are the same

        if a.first < b.first:  # if the a first name comes before b first name

            return True  # a will come before b

        return False  # otherwise b will come before a

    if a.last < b.last:
        return True  # a comes before b

    return False  # b comes before a


def is_alphabetized(roster, ordering):
    """
    Checks whether the roster of names is alphabetized in the given order
    :param roster: a list of people
    :param ordering: a function comparing two elements
    :return: True if the roster is alphabetized and False otherwise
    """

    i = 0

    for i in range(i, len(roster) - 1):

        if roster[i] == roster[i + 1]:  # if first name is the same as next name
            continue

        elif not ordering(roster[i], roster[i + 1]):

            return False

        i += 1

    return True


def alphabetize(roster, ordering):
    """
    Alphabetizes the roster according to the given ordering
    :param roster: a list of people
    :param ordering: a function comparing two elements
    :return: a sorted version of roster
    :return: the number of comparisons made
    """
    return merge_sort(roster, ordering)
