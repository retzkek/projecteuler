(ns kmr.projecteuler
  (:require [clojure.test :as test]))

(defn divisible-by-all?
  "Tests if n is divisible by all ms."
  [n ms]
  (every? true? (map #(zero? (rem n %)) ms)))

(defn lowest-divisible-by-all
  "Returns lowest number divisible by all ms."
  [ms]
  (first (drop-while #(not (divisible-by-all? % ms)) (iterate inc 1))))

(def run-test '(= 2520 (lowest-divisible-by-all (range 2 11))))
(def run-problem '(lowest-divisible-by-all (range 2 21)))
