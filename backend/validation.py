import spacy
import re
import inflect


def validate(type, sentence):

    nlp = spacy.load('en_core_web_sm')
    inflector = inflect.engine()
    sentence = sentence.lower()
    type = type.lower()
    words_list = sentence.split()
    print(words_list)
    empty = 0

    verb_list_s = [
        "is", "has", "does", "goes", "says", "gets", "makes", "knows", "takes", "sees",
        "comes", "thinks", "looks", "wants", "gives", "uses", "finds", "tells", "asks", "works",
        "seems", "feels", "tries", "leaves", "calls", "becomes", "includes", "continues", "changes",
        "leads", "understands", "watches", "follows", "stops", "creates", "opens", "walks", "offers",
        "remembers", "considers", "appears", "buys", "serves", "sends", "expects", "builds", "stays",
        "hears", "moves", "believes", "can"]
    verb_list_p = [
        "are", "have", "do", "go", "say", "get", "make", "know", "take", "see",
        "come", "think", "look", "want", "give", "use", "find", "tell", "ask", "work",
        "seem", "feel", "try", "leave", "call", "become", "include", "continue", "change", "lead",
        "understand", "watch", "follow", "stop", "create", "open", "walk", "offer", "remember",
        "consider", "appear", "buy", "serve", "send", "expect", "build", "stay", "hear", "move",
        "believe", "can"]
    pattern1 = r'^\s*\w+(\s+\w+)?(\s+don\'t)?\s*$'
    pattern2 = r'^\s*(\s+not)?(\s+a)?\w+(\s+\w+)?\s*$'

    verb = None
    index = None
    for word in words_list:
        if word in verb_list_s:
            for i in range(len(verb_list_s)):
                if word == verb_list_s[i]:
                    verb = word
                    index = i
        elif word in verb_list_p:
            verb = word

    if verb is None:
        return -1, -1, -1, -1, -1

    first_half = sentence.split(verb)[0]
    second_half = sentence.split(verb)[1]

    second_half = second_half.replace(".", "")
    
    verif_sent = bool(re.match(pattern1, first_half)) and bool(re.match(pattern2, second_half))

    if verif_sent == True:
        if type == "(empty)":
            type = "all"
            empty = 1
        elif type == "some":
            if "not" in words_list:
                type = "some-not"
            elif "don't" in words_list:
                type = "some-dont"
        
        if "don't" in words_list:
            subject = first_half.replace("don't", "").strip()
        else:
            subject = first_half.strip()
        if "not" in words_list:
            predicate = second_half.replace("not", "").strip()
        elif "a" in words_list:
            predicate = second_half.replace("a", "").strip()
        else:
            predicate = second_half.strip()
        if index is None:
            return type, subject, predicate, verb, empty
        else:
            return type, subject, predicate, verb_list_p[index], empty
    else:
        return -1, -1, -1, -1, -1

