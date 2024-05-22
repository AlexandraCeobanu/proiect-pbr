import json
import re

def validate(type, sentence):
    sentence = sentence.lower()
    type = type.lower()
    words_list = sentence.split()

    verb_list = ["are", "is", "have", "has"]
    pattern1 = r'^\s*\w+(\s+\w+)?\s*$'
    pattern2 = r'^\s*(\s+not)?\w+(\s+\w+)?\s*$'
    for word in words_list:
        if word in verb_list:
            verb = word

    first_half = sentence.split(verb)[0]
    second_half = sentence.split(verb)[1]

    second_half = second_half.replace(".", "")
    
    verif_sent = bool(re.match(pattern1, first_half)) and bool(re.match(pattern2, second_half))

    if verif_sent == True:
        if type == "(empty)":
            type = "all"
        elif type == "some":
            if "not" in words_list:
                type = "some-not"
        
        subject = first_half.strip()
        if "not" in words_list:
            predicate = second_half.replace("not", "").strip()
        else:
            predicate = second_half.strip()
        return (type, subject, predicate, verb)
    else:
        return (-1,-1,-1,-1)

