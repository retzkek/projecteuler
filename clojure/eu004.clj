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
   (- (Math/round (Math/pow 10 n)) 1))
 (test/is (= 9 (max-n-digit-num 1)))
 (test/is (= 99 (max-n-digit-num 2)))
 (test/is (= 999 (max-n-digit-num 3))))

(defn palindrome
  "Returns the largest palindrome made from two digits-digit numbers."
  ([digits]
   (palindrome digits 0))
  ([digits last-max]
   (+ last-max)))

(let [start (max-n-digit-num 2)
      stop (+ 1 (max-n-digit-num 1))]
  (range start (dec stop) -1))

(test/run-tests)



