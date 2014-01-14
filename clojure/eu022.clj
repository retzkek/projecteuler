(ns kmr.projecteuler
  (:require [clojure.string :as string]))

(defn string-val
  "Returns sum of character values in string when a=1, b=2, ..."
  [s]
  (let [chars (zipmap "abcdefghijklmnopqrstuvwxyz" (range 1 27))]
    (reduce + (map chars (string/lower-case s)))))

(def run-test '(= 53 (string-val "COLIN")))
(def run-problem
  '(reduce + (map-indexed (fn [i s] (* (inc i) (string-val s)))
                          (sort (string/split
                                 (string/replace
                                  (slurp "../data/names.txt")
                                  #"\"" "")
                                 #",")))))
