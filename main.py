import codecs
import re
import sys
import os
from evaluate import get_test_results


def is_suffix(word, suffix):
    return word.endswith(suffix)

# structure of description is:
# 'Original': original form.
# 'Type': 'V', 'N', 'A'.

def get_word_raw_descriptions (word):

    raw_descriptions = []

    if (is_suffix(word, '')):
    # TODO method for suffix removing and producing original form.
        raw_descriptions.append({'Original': 'abc', 'Type': 'V'})

    return raw_descriptions

def apply_heuristics (raw_descriptions):
    return raw_descriptions

def get_word_descriptions (word):
    return apply_heuristics(get_word_raw_descriptions(word))

def get_converted_to_output_form (description):
    return description['Original'] + '+' + description['Type']

def produce_output(input_path, output_path):
    inputer = codecs.open(input_path, "r", "utf-8")
    outputer = codecs.open(output_path, "w", "latin1")
    for word in inputer:
        descriptions = get_word_descriptions(word)
        line = word.rstrip('\r\n')
        for description in descriptions:
            line = line + '\t' + get_converted_to_output_form(description)
        outputer.write(line + '\n')

def get_train_score():
    produce_output('data\\spanish.txt.learn.utf-8.clean','data\\temp.txt')
    score = get_test_results('data\\spanish.txt.learn', 'data\\temp.txt')
    os.remove('data\\temp.txt')
    return score


def main():
    print get_train_score()

if __name__ == '__main__':
    main()
