"""
File: anagram.py
Name: Anna
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    print("Welcome to stanCode 'Anagram Generator' (or -1 to quit)")
    while True:
        user_input = input('Find anagrams for: ')
        if user_input == EXIT:
            break
        start = time.time()
        dictionary = read_dictionary()
        find_anagrams(user_input, dictionary)

        end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    dictionary = []
    with open(FILE, 'r') as f:
        for line in f:
            tokens = line.split()
            dictionary.append(tokens[0])
    return dictionary


def find_anagrams(s, dictionary):
    """
    :param s: string, by user input
    :return: none
    """
    dict_list = read_dictionary()
    result_list = []
    find_anagrams_helper(s, '', len(s), dict_list, result_list, dictionary)
    print(str(len(result_list)) + ' anagrams: ', end='')
    print(result_list)


def count_string_element(string_s):
    dict_string = {}
    for i in range(len(string_s)):
        if string_s[i] in dict_string:
            dict_string[string_s[i]] += 1
        else:
            dict_string[string_s[i]] = 1


def find_anagrams_helper(string_s, current_string, ans_len, dict_list, result_list, dictionary):
    if len(current_string) == ans_len:
        if current_string in dict_list and not (current_string in result_list):
            print('Searching...')
            print('Founds: ' + current_string)
            result_list.append(current_string)

    else:
        for s in string_s:
            # print(s + " current_string: " + current_string + " " + str(current_string.count(s)) + ":" + str(
            #     string_s.count(s)))
            if string_s.count(s) > current_string.count(s):
                # choose
                current_string = current_string + s
                if has_prefix(current_string, dictionary):
                    # explore
                    find_anagrams_helper(string_s, current_string, ans_len, dict_list, result_list, dictionary)
                # un-choose
                current_string = current_string[:-1]


def has_prefix(sub_s, dictionary):
    """
    :param sub_s: String
    :return: Boolean
    """
    if len(sub_s) > 0:
        # dict_list = read_dictionary()
        for i in range(len(dictionary)):
            if dictionary[i].startswith(sub_s):
                return True
    return False


if __name__ == '__main__':
    main()
