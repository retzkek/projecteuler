(ns kmr.projecteuler
  (:use clojure.set))

(defn multiples
  "Returns a lazy seq of all multiples of n from start to end (inclusive), where
  start defaults to n and end to infinity."
  ([n]
   (iterate #(+ n %) n))
  ([n end]
   (take-while #(<= % end) (multiples n)))
  ([n start end]
   (drop-while #(< % start) (multiples n end))))

(defn eratos
  "Compute all primes below n using Sieve of Eratosthenes."
  [n]
  (loop [i 2
         sieve (set (range 2 (inc n)))]
    (if (> (* i i) n)
      sieve
      (recur (first (drop-while #(not (contains? sieve %)) (range (inc i) n)))
             (difference sieve (set (multiples i (inc i) n)))))))

(def run-test '(= 17 (reduce + (eratos 7))))
(def run-problem '(reduce + (eratos 2e6)))
