(ns kmr.projecteuler.eu017
  (:require [clojure.string :as string]))

(defn num-to-words
  "Converts a positive integer into written form, e.g. 156 ->
  one hundred and fifty-six."
  [n]
  (let [digits  ["zero" "one" "two" "three" "four" "five"
                 "six" "seven" "eight" "nine" "ten"
                 "eleven" "twelve" "thirteen" "fourteen" "fifteen"
                 "sixteen" "seventeen" "eighteen" "nineteen"]
        tens ["zero" "ten" "twenty" "thirty" "forty" "fifty"
              "sixty" "seventy" "eighty" "ninety"]]
    (cond
     (< n 20)
     (digits n)
     (< n 100)
     (str (tens (quot n 10))
          (if (> (rem n 10) 0)
            (str "-" (digits (rem n 10)))))
     (< n 1000)
     (str (digits (quot n 100))
          " hundred"
          (if (> (rem n 100) 0)
            (str " and " (num-to-words (rem n 100)))))
     (< n 1000000)
     (str (num-to-words (quot n 1000))
          " thousand"
          (if (> (rem n 1000) 0)
            (str " and " (num-to-words (rem n 1000)))))
     :else
     "dunno")))

(defn count-letters
  "Returns length of string not including spaces and hyphens."
  [s]
  (count (string/replace s #"[ -]" "")))

(def run-test '(and (= 23 (count-letters (num-to-words 342)))
                    (= 20 (count-letters (num-to-words 115)))))
(def run-problem '(reduce + (map #(-> % num-to-words count-letters)
                                 (range 1 1001))))
