
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