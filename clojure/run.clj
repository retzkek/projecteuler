#!/usr/bin/clj
; Simple front end to run project euler problems and test cases
; Problem needs to be in file "euXXX.clj" where XXX is problem #
; Needs to define run-test and run-problem.
; TODO:
;   Maybe better as macro(s)?
;   Should probably be using namespaces

(def help-str "Usage: run.clj test|run problem-num")

(defn load-test
  [problem]
  (println "running test case for problem" problem)
  (load-file (str problem ".clj"))
  (if (eval '(eval run-test))
    (println "test passed")
    (println "test failed")))

(defn load-problem
  [problem]
  (println "running problem" problem)
  (load-file (str problem ".clj"))
  (println (time (eval '(eval run-problem)))))

(defn main
  ([] (println help-str))
  ([_] (println help-str))
  ([cmd problem] 
  (cond 
    (= cmd "test") (load-test (format "eu%03d" (read-string problem)))
    (= cmd "run") (load-problem (format "eu%03d" (read-string problem)))
    :else (println help-str)))
  ([_ _ & more] (println help-str)))

(apply main *command-line-args*)
