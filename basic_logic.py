
def is_suffix(word, suffix):
    return word.encode('utf-8').endswith(suffix)

def replace_suffix(word, suffix, new_suffix):
    return word[:-len(suffix)] + new_suffix

# structure of description is:
# 'Original': original form.
# 'Type': 'V', 'N', 'A'.

verbs_base = [
        {'Suffix': 'ar', 'Rules': [['Indic. Pres. Ar', 'o', 'as', 'a', 'amos', 'áis', 'an'],
                                   ['Indic. Fut.  Ar', 'é', 'ás', 'á', 'emos', 'éis', 'án'],
                                   ['Indic. Past  Ar', 'é', 'aste', 'ó', 'amos', 'asteis', 'aron'],
                                   ['Indic. Impf. Ar', 'aba', 'abas', 'aba', 'ábamos', 'abais', 'an'],
                                   ['Subj.  Pres. Ar', 'e', 'es', 'e', 'emos', 'éis', 'en'],
                                   ['Subj.  Past1 Ar', 'ara', 'aras', 'ara', 'áramos', 'areis', 'aran'],
                                   ['Subj.  Past2 Ar', 'ase', 'ases', 'ase', 'ásemos', 'aseis', 'asen']
                                   ]
        },
        {'Suffix': 'er', 'Rules': [['Indic. Pres. Er', 'o', 'es', 'e', 'emos', 'éis', 'en'],
                                   ['Indic. Fut.  Er', 'é', 'ás', 'á', 'emos', 'éis', 'án'],
                                   ['Indic. Past  Er', 'é', 'aste', 'ó', 'amos', 'asteis', 'aron'],
                                   ['Indic. Impf. Er', 'ía', 'ías', 'ía', 'íamos', 'íais', 'ían'],
                                   ['Subj.  Pres. Er', 'a', 'as', 'a', 'amos', 'áis', 'an'],
                                   ['Subj.  Past1 Er', 'iera', 'ieras', 'iera', 'iéramos', 'ierais', 'ieran'],
                                   ['Subj.  Past2 Er', 'iese', 'ieses', 'iese', 'iésemos', 'ieseis', 'iesen']
                                   ]
        }
    ]

def get_word_raw_descriptions (word):

    raw_descriptions = []

    # verbs


    for suffix_data in verbs_base:
        suffix = suffix_data['Suffix']
        for rule in suffix_data['Rules']:
            description = rule[0]
            for index in range(1, 7):
                if (is_suffix(word, rule[index])):
                    raw_descriptions.append({'Original': replace_suffix(word, rule[index], suffix),
                                             'Type': 'V',
                                             'Details': description + ' ' + str(index)
                                            })


    return raw_descriptions

def apply_heuristics (raw_descriptions):
    return raw_descriptions

def get_word_descriptions (word):
    return apply_heuristics(get_word_raw_descriptions(word))