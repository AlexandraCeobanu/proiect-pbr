import clips

def solve(type1, type2, subject1, subject2, pred1, pred2):
    DEFTEMPLATE_STRING = """
    (deftemplate major-premise
        (slot type)
        (slot subject)
        (slot predicate)
    )
    """

    DEFTEMPLATE_STRING1 = """
    (deftemplate minor-premise
        (slot type)
        (slot subject)
        (slot predicate)
    )
    """

    DEFTEMPLATE_STRING2 = """
    (deftemplate conclusion
        (slot type)
        (slot subject)
        (multislot verb)
        (slot predicate)
    )
    """

    DEFRULE_STRING = """
    (defrule 1aaa
    ?a <- (major-premise (type "all") (subject ?s) (predicate ?p))
    ?b <- (minor-premise (type "all") (subject ?x) (predicate ?s))
    => 
    (assert (conclusion (type "all") (subject ?x) (verb are) (predicate ?p)))
    )
    """

    DEFRULE_STRING1 = """
    (defrule 1aii
    ?a <- (major-premise (type "all") (subject ?s) (predicate ?p))
    ?b <- (minor-premise (type "some") (subject ?x) (predicate ?s))
    => 
    (assert (conclusion (type "some") (subject ?x) (verb are) (predicate ?p)))
    )
    """

    DEFRULE_STRING2 = """
    (defrule 1eae
    ?a <- (major-premise (type "no") (subject ?s) (predicate ?p))
    ?b <- (minor-premise (type "all") (subject ?x) (predicate ?s))
    => 
    (assert (conclusion (type "no") (subject ?x) (verb are) (predicate ?p)))
    )
    """

    DEFRULE_STRING3 = """
    (defrule 1eio
    ?a <- (major-premise (type "no") (subject ?s) (predicate ?p))
    ?b <- (minor-premise (type "some") (subject ?x) (predicate ?s))
    => 
    (assert (conclusion (type "some") (subject ?x) (verb are not) (predicate ?p)))
    )
    """

    DEFRULE_STRING4 = """
    (defrule 2aee
    ?a <- (major-premise (type "all") (subject ?s) (predicate ?p))
    ?b <- (minor-premise (type "no") (subject ?x) (predicate ?p))
    => 
    (assert (conclusion (type "no") (subject ?x) (verb are ) (predicate ?s)))
    )
    """

    DEFRULE_STRING5 = """
    (defrule 2aoo
    ?a <- (major-premise (type "all") (subject ?s) (predicate ?p))
    ?b <- (minor-premise (type "some-not") (subject ?x) (predicate ?p))
    => 
    (assert (conclusion (type "some") (subject ?x) (verb are not ) (predicate ?s)))
    )
    """

    DEFRULE_STRING6 = """
    (defrule 2eae
    ?a <- (major-premise (type "no") (subject ?s) (predicate ?p))
    ?b <- (minor-premise (type "all") (subject ?x) (predicate ?p))
    => 
    (assert (conclusion (type "no") (subject ?x) (verb are ) (predicate ?s)))
    )
    """

    DEFRULE_STRING7 = """
    (defrule 2eio
    ?a <- (major-premise (type "no") (subject ?s) (predicate ?p))
    ?b <- (minor-premise (type "some") (subject ?x) (predicate ?p))
    => 
    (assert (conclusion (type "some") (subject ?x) (verb are not) (predicate ?s)))
    )
    """

    DEFRULE_STRING8 = """
    (defrule 3aai
    ?a <- (major-premise (type "all") (subject ?s) (predicate ?p1))
    ?b <- (minor-premise (type "all") (subject ?s) (predicate ?p2))
    => 
    (assert (conclusion (type "some") (subject ?p2) (verb are ) (predicate ?p1)))
    )
    """

    DEFRULE_STRING9 = """
    (defrule 3aii
    ?a <- (major-premise (type "all") (subject ?s) (predicate ?p1))
    ?b <- (minor-premise (type "some") (subject ?s) (predicate ?p2))
    => 
    (assert (conclusion (type "some") (subject ?p2) (verb are ) (predicate ?p1)))
    )
    """

    DEFRULE_STRING10 = """
    (defrule 3eao
    ?a <- (major-premise (type "no") (subject ?s) (predicate ?p1))
    ?b <- (minor-premise (type "all") (subject ?s) (predicate ?p2))
    => 
    (assert (conclusion (type "some") (subject ?p2) (verb are not) (predicate ?p1)))
    )
    """

    DEFRULE_STRING11 = """
    (defrule 3eio
    ?a <- (major-premise (type "no") (subject ?s) (predicate ?p1))
    ?b <- (minor-premise (type "some") (subject ?s) (predicate ?p2))
    => 
    (assert (conclusion (type "some") (subject ?p2) (verb are not) (predicate ?p1)))
    )
    """

    DEFRULE_STRING12 = """
    (defrule 3iai
    ?a <- (major-premise (type "some") (subject ?s) (predicate ?p1))
    ?b <- (minor-premise (type "all") (subject ?s) (predicate ?p2))
    => 
    (assert (conclusion (type "some") (subject ?p2) (verb are) (predicate ?p1)))
    )
    """

    DEFRULE_STRING13 = """
    (defrule 3oao-de-facut 
    ?a <- (major-premise (type "some-not") (subject ?s) (predicate ?p1))
    ?b <- (minor-premise (type "all") (subject ?s) (predicate ?p2))
    => 
    (assert (conclusion (type "some") (subject ?p2) (verb are not) (predicate ?p1)))
    )
    """

    DEFRULE_STRING14 = """
    (defrule 4aai
    ?a <- (major-premise (type "all") (subject ?s) (predicate ?p))
    ?b <- (minor-premise (type "all") (subject ?p) (predicate ?p2))
    => 
    (assert (conclusion (type "some") (subject ?p2) (verb are) (predicate ?s)))
    )
    """

    DEFRULE_STRING15 = """
    (defrule 4aee
    ?a <- (major-premise (type "all") (subject ?s) (predicate ?p))
    ?b <- (minor-premise (type "no") (subject ?p) (predicate ?p2))
    => 
    (assert (conclusion (type "no") (subject ?p2) (verb are) (predicate ?s)))
    )
    """

    DEFRULE_STRING16 = """
    (defrule 4eao
    ?a <- (major-premise (type "no") (subject ?s) (predicate ?p))
    ?b <- (minor-premise (type "all") (subject ?p) (predicate ?p2))
    => 
    (assert (conclusion (type "some") (subject ?p2) (verb are not) (predicate ?s)))
    )
    """

    DEFRULE_STRING17 = """
    (defrule 4eio
    ?a <- (major-premise (type "no") (subject ?s) (predicate ?p))
    ?b <- (minor-premise (type "some") (subject ?p) (predicate ?p2))
    => 
    (assert (conclusion (type "some") (subject ?p2) (verb are not) (predicate ?s)))
    )
    """

    DEFRULE_STRING18 = """
    (defrule 4iai
    ?a <- (major-premise (type "some") (subject ?s) (predicate ?p))
    ?b <- (minor-premise (type "all") (subject ?p) (predicate ?p2))
    => 
    (assert (conclusion (type "some") (subject ?p2) (verb are) (predicate ?s)))
    )
    """

    DEFRULE_STRING19 = """
    (defrule print_conclusion
    ?a <- (conclusion (type ?t) (subject ?s) (verb ?v ?v2) (predicate ?p))
    => 
    (printout t "Conclusion: " ?t " " ?s " " ?v " " ?v2 " "  ?p)
    )
    """

    DEFRULE_STRING20 = """
    (defrule print_conclusion2
    ?a <- (conclusion (type ?t) (subject ?s) (verb ?v) (predicate ?p))
    => 
    (printout t "Conclusion: " ?t " " ?s " " ?v " "  ?p)
    )
    """

    DEFRULE_STRING21 = """
    (defrule blabla
    =>
    printout t "Hello"
    )
    """

    environment = clips.Environment()

    environment.build(DEFTEMPLATE_STRING)
    environment.build(DEFTEMPLATE_STRING1)
    environment.build(DEFTEMPLATE_STRING2)
    environment.build(DEFRULE_STRING)
    environment.build(DEFRULE_STRING1)
    environment.build(DEFRULE_STRING2)
    environment.build(DEFRULE_STRING3)
    environment.build(DEFRULE_STRING4)
    environment.build(DEFRULE_STRING5)
    environment.build(DEFRULE_STRING6)
    environment.build(DEFRULE_STRING7)
    environment.build(DEFRULE_STRING8)
    environment.build(DEFRULE_STRING9)
    environment.build(DEFRULE_STRING10)
    environment.build(DEFRULE_STRING11)
    environment.build(DEFRULE_STRING12)
    environment.build(DEFRULE_STRING13)
    environment.build(DEFRULE_STRING14)
    environment.build(DEFRULE_STRING15)
    environment.build(DEFRULE_STRING16)
    environment.build(DEFRULE_STRING17)
    environment.build(DEFRULE_STRING18)
    environment.build(DEFRULE_STRING19)
    environment.build(DEFRULE_STRING20)
    environment.build(DEFRULE_STRING21)

    template = environment.find_template('major-premise')

    fact = template.assert_fact(type=type1,
                                subject=subject1,
                                predicate=pred1)

    template1 = environment.find_template('minor-premise')

    fact1 = template1.assert_fact(type=type2,
                                  subject=subject2,
                                  predicate=pred2)

    environment.run()
    conclusion = ""
    for i, fact in enumerate(environment.facts()):
        if i == 2:
            if len(fact["verb"]) == 1:
                conclusion = fact["type"].capitalize() + " " + fact["subject"] + " " + fact["verb"][0] + " " + fact["predicate"]
            elif len(fact["verb"]) == 2:
                conclusion = fact["type"].capitalize() + " " + fact["subject"] + " " + fact["verb"][0] + " " + fact["verb"][1] + " " + fact["predicate"]
    return conclusion

#solve("no", "all", "rational beings", "people", "animals", "animals")

