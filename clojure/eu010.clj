(ns kmr.projecteuler
  (:use clojure.set))

(defn eratos
  "Compute all primes below n using Sieve of Eratosthenes."
  [n]
  (loop [i 2
         sieve (set (range 2 (inc n)))]
    (if (> (* i i) n)
      sieve
      (recur (first (drop-while #(not (contains? sieve %)) (range (inc i) n)))
             (difference sieve (set (range (+ i i) (inc n) i)))))))

(def run-test '(= 17 (reduce + (eratos 7))))
(def run-problem '(reduce + (eratos 2e6)))

