(ns kmr.projecteuler
  (:require [clojure.test :as test]))

(test/with-test
 (defn palindrome?
   [n]
   "tests if n is palindromic"
   (= (str n) (apply str (reverse (str n)))))
 (test/is (not (palindrome? 123)))
 (test/is (palindrome? 121))
 (test/is (not (palindrome? "abc")))
 (test/is (palindrome? "aba")))

(test/with-test
 (defn max-n-digit-num
   "Returns largest n-digit integer."
   [n]
   (dec (Math/round (Math/pow 10 n))))
 (test/is (= 9 (max-n-digit-num 1)))
 (test/is (= 99 (max-n-digit-num 2)))
 (test/is (= 999 (max-n-digit-num 3))))

(test/with-test
 (defn min-n-digit-num
   "Returns smallest n-digit integer."
   [n]
   (if (= n 1)
     0
     (inc (max-n-digit-num (dec n)))))
 (test/is (= 0 (min-n-digit-num 1)))
 (test/is (= 10 (min-n-digit-num 2)))
 (test/is (= 100 (min-n-digit-num 3))))

(defn n-digit-nums
  "Returns all n-digit integers in reverse order."
  [n]
  (let [start (max-n-digit-num n)
        stop (+ 1 (max-n-digit-num (dec n)))]
    (range start (dec stop) -1)))

(defn max-palindrome
  "Returns the largest palindrome made from two digits-digit numbers."
  [digits]
  (apply max (for [x (n-digit-nums digits)
                   y (n-digit-nums digits)
                   :when (palindrome? (* x y))]
               (* x y))))
(def run-test '(= (max-palindrome 2) 9009))
(def run-problem '(max-palindrome 3))

;(test/run-tests)


