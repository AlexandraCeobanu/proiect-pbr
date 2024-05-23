import inflect

def getSingular(n1, n2, n3, n4):
    inflector = inflect.engine()


    singular_form = inflector.singular_noun(n1)
    if singular_form:
        n1 = singular_form

    singular_form = inflector.singular_noun(n2)
    if singular_form:
        n2 = singular_form

    singular_form = inflector.singular_noun(n3)
    if singular_form:
        n3 = singular_form

    singular_form = inflector.singular_noun(n4)
    if singular_form:
        n4 = singular_form

    return n1, n2, n3, n4




