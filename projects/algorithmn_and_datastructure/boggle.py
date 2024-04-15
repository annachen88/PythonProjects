"""
File: boggle.py
Name: Anna
----------------------------------------
TODO: Find the vocabulary from users inputs (2D) in dictionary.txt
"""
import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
    start = time.time()
    ####################
    counter = 1
    input_dic = []
    input_set = []
    while counter < 5:
        user_input = input(str(counter) + ' ' + 'row of letters: ')
        tokens = user_input.split()
        if len(tokens) != 4:
            print('Illegal input')
            break
        else:
            input_dic =[]
            for i in range(len(tokens)):
                if len(tokens[i]) > 1:
                    print('Illegal input')
                    break
                else:
                    input_dic.append(tokens[i])
            counter += 1
            input_set.append(input_dic)
    dictionary = read_dictionary()
    find_anagrams(input_dic, dictionary, input_set)

    end = time.time()
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


# 1 row of letters: f y c l
# 2 row of letters: i o m g
# 3 row of letters: o r i l
# 4 row of letters: h j h u


def find_anagrams(input_dic, dictionary, input_set):
    """
    :param s: string, by user input
    :return: none
    """
    result_list = []
    for x in range(4):
        for y in range(4):
            current_string = input_set[x][y]
            find_anagrams_helper(current_string, x, y, dictionary, result_list, [(x, y)], input_set)
    print('There are ' + str(len(result_list)) + ' words in total. ', end='')


def find_anagrams_helper(current_string, row, column, dict_list, result_list, visit_list, input_set):
    if len(current_string) >= 4:
        if current_string in dict_list and not (current_string in result_list):
            print('Founds: ' + current_string)
            result_list.append(current_string)
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_row = row + i
            new_column = column + j
            if (new_row, new_column) not in visit_list:
                if 0 <= new_row <= 3 and 0 <= new_column <= 3:
                    visit_list.append((new_row, new_column))
                    current_string = current_string + input_set[new_row][new_column]
                    if has_prefix(current_string, dict_list):
                        find_anagrams_helper(current_string, new_row, new_column, dict_list, result_list, visit_list,
                                             input_set)
                    # un-choose
                    current_string = current_string[:-1]
                    visit_list.pop()


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    dictionary = []
    with open(FILE, 'r') as f:
        for line in f:
            tokens = line.split()
            dictionary.append(tokens[0])
    return dictionary


def has_prefix(sub_s, dictionary):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    if len(sub_s) > 0:
        for i in range(len(dictionary)):
            if dictionary[i].startswith(sub_s) and len(dictionary[i]) >= 4:
                return True
    return False


if __name__ == '__main__':
    main()
