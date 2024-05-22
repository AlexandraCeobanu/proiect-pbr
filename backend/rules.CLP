(deftemplate major-premise
    (slot type)
    (slot subject)
    (slot predicate)
)

(deftemplate minor-premise
    (slot type)
    (slot subject)
    (slot predicate)
)

(deftemplate conclusion
    (slot type)
    (slot subject)
    (multislot verb)
    (slot predicate)
)
(deffacts fapte_initiale
(read-premises)
)

(defrule read_premises
?a<-(read-premises)
=>
(retract ?a)
(printout t "Introduceti prima premisa" crlf)
(assert (words-major-premise (explode$ (readline))))
(printout t "Introduceti a doua premisa" crlf)
(assert (words-minor-premise (explode$ (readline))))
)

(defrule build_major_premise
?a<-(words-major-premise ?t ?s ?v ?p) 
=> 
(retract ?a)
(assert (major-premise (type ?t) (subject ?s) (predicate ?p)))
)

(defrule build_major_premise2
?a<-(words-major-premise ?t ?s ?v not ?p) 
=> 
(retract ?a)
(assert (major-premise (type some-not) (subject ?s) (predicate ?p)))
)

(defrule build_minor_premise
?a<-(words-minor-premise ?t ?s ?v ?p) 
=> 
(retract ?a)
(assert (minor-premise (type ?t) (subject ?s) (predicate ?p)))
)

(defrule build_minor_premise2
?a<-(words-minor-premise ?t ?s ?v not ?p) 
=> 
(retract ?a)
(assert (minor-premise (type some-not) (subject ?s) (predicate ?p)))
)


(defrule 1aaa
?a <- (major-premise (type all) (subject ?s) (predicate ?p))
?b <- (minor-premise (type all) (subject ?x) (predicate ?s))
=> 
(assert (conclusion (type all) (subject ?x) (verb are) (predicate ?p)))
)

(defrule 1aii
?a <- (major-premise (type all) (subject ?s) (predicate ?p))
?b <- (minor-premise (type some) (subject ?x) (predicate ?s))
=> 
(assert (conclusion (type some) (subject ?x) (verb are) (predicate ?p)))
)

(defrule 1eae
?a <- (major-premise (type no) (subject ?s) (predicate ?p))
?b <- (minor-premise (type all) (subject ?x) (predicate ?s))
=> 
(assert (conclusion (type no) (subject ?x) (verb are) (predicate ?p)))
)

(defrule 1eio
?a <- (major-premise (type no) (subject ?s) (predicate ?p))
?b <- (minor-premise (type some) (subject ?x) (predicate ?s))
=> 
(assert (conclusion (type some) (subject ?x) (verb are not) (predicate ?p)))
)

(defrule 2aee
?a <- (major-premise (type all) (subject ?s) (predicate ?p))
?b <- (minor-premise (type no) (subject ?x) (predicate ?p))
=> 
(assert (conclusion (type no) (subject ?x) (verb are ) (predicate ?s)))
)

(defrule 2aoo
?a <- (major-premise (type all) (subject ?s) (predicate ?p))
?b <- (minor-premise (type some-not) (subject ?x) (predicate ?p))
=> 
(assert (conclusion (type some) (subject ?x) (verb are not ) (predicate ?s)))
)

(defrule 2eae
?a <- (major-premise (type no) (subject ?s) (predicate ?p))
?b <- (minor-premise (type all) (subject ?x) (predicate ?p))
=> 
(assert (conclusion (type no) (subject ?x) (verb are ) (predicate ?s)))
)

(defrule 2eio
?a <- (major-premise (type no) (subject ?s) (predicate ?p))
?b <- (minor-premise (type some) (subject ?x) (predicate ?p))
=> 
(assert (conclusion (type some) (subject ?x) (verb are not) (predicate ?s)))
)

(defrule 3aai
?a <- (major-premise (type all) (subject ?s) (predicate ?p1))
?b <- (minor-premise (type all) (subject ?s) (predicate ?p2))
=> 
(assert (conclusion (type some) (subject ?p2) (verb are ) (predicate ?p1)))
)

(defrule 3aii
?a <- (major-premise (type all) (subject ?s) (predicate ?p1))
?b <- (minor-premise (type some) (subject ?s) (predicate ?p2))
=> 
(assert (conclusion (type some) (subject ?p2) (verb are ) (predicate ?p1)))
)

(defrule 3eao
?a <- (major-premise (type no) (subject ?s) (predicate ?p1))
?b <- (minor-premise (type all) (subject ?s) (predicate ?p2))
=> 
(assert (conclusion (type some) (subject ?p2) (verb are not) (predicate ?p1)))
)

(defrule 3eio
?a <- (major-premise (type no) (subject ?s) (predicate ?p1))
?b <- (minor-premise (type some) (subject ?s) (predicate ?p2))
=> 
(assert (conclusion (type some) (subject ?p2) (verb are not) (predicate ?p1)))
)

(defrule 3iai
?a <- (major-premise (type some) (subject ?s) (predicate ?p1))
?b <- (minor-premise (type all) (subject ?s) (predicate ?p2))
=> 
(assert (conclusion (type some) (subject ?p2) (verb are) (predicate ?p1)))
)

(defrule 3oao-de-facut 
?a <- (major-premise (type some-not) (subject ?s) (predicate ?p1))
?b <- (minor-premise (type all) (subject ?s) (predicate ?p2))
=> 
(assert (conclusion (type some) (subject ?p2) (verb are not) (predicate ?p1)))
)

(defrule 4aai
?a <- (major-premise (type all) (subject ?s) (predicate ?p))
?b <- (minor-premise (type all) (subject ?p) (predicate ?p2))
=> 
(assert (conclusion (type some) (subject ?p2) (verb are) (predicate ?s)))
)

(defrule 4aee
?a <- (major-premise (type all) (subject ?s) (predicate ?p))
?b <- (minor-premise (type no) (subject ?p) (predicate ?p2))
=> 
(assert (conclusion (type no) (subject ?p2) (verb are) (predicate ?s)))
)

(defrule 4eao
?a <- (major-premise (type no) (subject ?s) (predicate ?p))
?b <- (minor-premise (type all) (subject ?p) (predicate ?p2))
=> 
(assert (conclusion (type some) (subject ?p2) (verb are not) (predicate ?s)))
)

(defrule 4eio
?a <- (major-premise (type no) (subject ?s) (predicate ?p))
?b <- (minor-premise (type some) (subject ?p) (predicate ?p2))
=> 
(assert (conclusion (type some) (subject ?p2) (verb are not) (predicate ?s)))
)

(defrule 4iai
?a <- (major-premise (type some) (subject ?s) (predicate ?p))
?b <- (minor-premise (type all) (subject ?p) (predicate ?p2))
=> 
(assert (conclusion (type some) (subject ?p2) (verb are) (predicate ?s)))
)


(defrule print_conclusion
?a <- (conclusion (type ?t) (subject ?s) (verb ?v ?v2) (predicate ?p))
=> 
(printout t "Conclusion: " ?t " " ?s " " ?v " " ?v2 " "  ?p)
)

(defrule print_conclusion2
?a <- (conclusion (type ?t) (subject ?s) (verb ?v) (predicate ?p))
=> 
(printout t "Conclusion: " ?t " " ?s " " ?v " "  ?p)
)
