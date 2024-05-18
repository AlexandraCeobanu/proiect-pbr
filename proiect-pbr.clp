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
    (slot subject)
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

(defrule build_minor_premise
?a<-(words-minor-premise ?t ?s ?v ?p) 
=> 
(retract ?a)
(assert (minor-premise (type ?t) (subject ?s) (predicate ?p)))
)


(defrule show_major_premise
?a<-(major-premise (type ?t) (subject ?s) (predicate ?p))
=>
(retract ?a)
(printout t "Tipul " ?t crlf)
(printout t "Subiectul " ?s crlf)
(printout t "Predicatul " ?p crlf)
)

(defrule show_minor_premise
?a<-(minor-premise (type ?t) (subject ?s) (predicate ?p))
=>
(retract ?a)
(printout t "Tipul " ?t crlf)
(printout t "Subiectul " ?s crlf)
(printout t "Predicatul " ?p crlf)
)