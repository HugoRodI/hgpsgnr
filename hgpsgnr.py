#!/usr/bin/python

import sys
import os

def parse_arguments():
    number_of_arguments = len(sys.argv)
    if (number_of_arguments <= 1) or sys.argv[1] == '-h':
        print_help()
        exit()
    elif (number_of_arguments == 2) and sys.argv[1] == '-v':
        print_version()
        exit()
    elif (number_of_arguments == 2) and sys.argv[1] == '-l':
        keywords = ask_for_keywords()
        keywords_combination(keywords)
        exit()
    elif (number_of_arguments == 3) and sys.argv[1] == '-l' and sys.argv[2] == 't':
        keywords_combination_with_date()
        exit()


def print_help():
    print "\r\n"
    print " [ Options ]\r\n"
    print " -h  display this help and exit\r\n"
    print " -l  enter keywords to generate the password's dictionary\r\n"
    print " -t  passwords contains current month and year\r\n"
    print " -v  display the running version of hgpsgnr\r\n"

def print_version():
    print "a"

def ask_for_keywords():
    print " Enter the keywords separated by ';': key_1; key2; key3; ...\r\n"
    keywords = raw_input(" ").split(";")
    keywords = [keyword.strip(' ') for keyword in keywords]
    print " Keywords saved!\r\n"
    return keywords

def keywords_combination(keywords):
    print " Generating passwords...\r\n"
    passwords_list = to_lower(keywords)
    passwords_list += to_upper(keywords)
    passwords_list += capitalize_vowels(keywords)
    passwords_list += capitalize_consonants(keywords)
    passwords_list += capitalize_first_letter(keywords)
    
    #At this points, short words can cause duplicates.
    #remove duplicates before mixing
    passwords_list = remove_duplicates(passwords_list)

    separators = ['-', '_']

    passwords_list += combine_passwords_and_separators(passwords_list, separators)
    #for p in passwords_list:
        #print p

    create_passwords_dictionary(passwords_list)

def to_lower(keywords):
    return [key.lower() for key in keywords]

def to_upper(keywords):
    return [key.upper() for key in keywords]


def capitalize_vowels(keywords):    
    vowels = ('a', 'e', 'i', 'o', 'u')
    
    keywords = to_lower(keywords)
    aux_keywords = []
    for keyword in keywords:
        for letter in keyword:
            if letter in vowels:
                keyword = keyword.replace(letter, letter.upper())
        aux_keywords.append(keyword)
    
    return aux_keywords

def capitalize_consonants(keywords):
    vowels = ('a', 'e', 'i', 'o', 'u')
    
    keywords = to_lower(keywords)
    aux_keywords = []
    for keyword in keywords:
        for letter in keyword:
            if letter not in vowels:
                keyword = keyword.replace(letter, letter.upper())
        aux_keywords.append(keyword)

    return aux_keywords
    

def capitalize_first_letter(keywords):
    keywords = to_lower(keywords)
    
    return [keyword[0].upper()+keyword[1:] for keyword in keywords]

def remove_duplicates(passwords_list):
    return list(set(passwords_list))

def combine_passwords_and_separators(passwords_list, separators):
    passwords_with_separators = []
    
    for separator in separators:
        for i in range(0, len(passwords_list)):
            for j in range(i + 1, len(passwords_list)):
                passwords_with_separators.append(passwords_list[i] + separator + passwords_list[j])
                passwords_with_separators.append(passwords_list[j] + separator + passwords_list[i])

    return passwords_with_separators


def create_passwords_dictionary(passwords_list):
    passwords_dictionary = open('passwords_dictionary.txt', 'w+')

    for password in passwords_list:
        passwords_dictionary.write("%s\n" % password)

    print " Passwords dictionary sucessfully created in {0}\r\n".format(os.path.abspath(__file__))

def keywords_combination_with_date():
    print "c"

parse_arguments()