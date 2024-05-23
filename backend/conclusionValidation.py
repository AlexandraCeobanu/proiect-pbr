import spacy

def validate_conclusion(conclusion):
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

    nlp = spacy.load('en_core_web_sm')
    doc = nlp(conclusion)
    result = ""
    no = 0

    for token in doc:
        if token.text == "All":
            continue
        elif token.text == "No":
            no = 1
        elif token.pos_ == 'PROPN':
            result += token.text.capitalize()
            result += " "
        elif token.text in verb_list_p:
            index = verb_list_p.index(token.text)
            result += verb_list_s[index]
            if no == 1:
                result += " not "
            else:
                result += " "
        elif token.text == "don't":
            result += "doesn't "
        else:
            result += token.text
            result += " "

    return result.capitalize().strip()

