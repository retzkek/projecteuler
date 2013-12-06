(ns kmr.projecteuler
  (:require [clojure.test :as test]))

(defn square [x] (* x x))

(defn sqsum-minus-sumsq
  "Returns the difference betweem the sum of the squares and the square
  of the sum of the first n natural numbers."
  [n]
  (let [ns (range 1 (inc n))]
    (- (square (reduce + ns))
       (reduce + (map square ns)))))

(def run-test '(= 2640 (sqsum-minus-sumsq 10)))
(def run-problem '(sqsum-minus-sumsq 100))
;(eval run-problem)