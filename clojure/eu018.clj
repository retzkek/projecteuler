(ns kmr.projecteuler
  (:require [clojure.java.io :as io]
            [clojure.string :as string]))

(defn reduce-rows [a b]
  (if (= 1 (- (count a) (count b)))
    (map-indexed (fn [i x]
                   (max (+ x (nth a i)) (+ x (nth a (inc i)))))
                 b)
    (throw (Exception. "(count a) must be one more than (count b)"))))

(defn split-ints [s]
  (map #(Integer/parseInt %) (string/split s #"\s+")))

(with-open [input (io/reader "/Users/kmr/Documents/projecteuler/data/eu018.dat")]
  (reduce reduce-rows (reverse (map split-ints (line-seq input)))))
