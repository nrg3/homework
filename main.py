import codecs
import re
import sys
import os
from basic_logic import get_word_descriptions
from evaluate import get_test_results

def get_converted_to_output_form (description):
    return description['Original'] + '+' + description['Type']

def produce_output(input_path, output_path):
    inputer = codecs.open(input_path, "r", "utf-8")
    outputer = codecs.open(output_path, "w", "latin1")
    for word in inputer:
        descriptions = get_word_descriptions(word.rstrip('\r\n'))
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
    #produce_output('data\\spanish.txt.test.clean.utf-8','data\\release.txt')
    print get_train_score()

if __name__ == '__main__':
    main()
