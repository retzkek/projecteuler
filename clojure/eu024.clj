(ns kmr.projecteuler)

(defn remove-nth
  "Returns s with the value at location n removed."
  [s n]
  (let [[a b] (split-at n s)]
    (concat a (rest b))))

(defn permutations
  "Returns sequence of permutations of values in s."
  [s]
  (reduce concat
          (map-indexed
           (fn [i x]
             (map #(conj % x) (permutations (remove-nth s i))))
           s)))

(defn nth-permutation
  "Returns the nth permutation of values in s."
  [s n]
  (first (drop (dec n) (permutations s))))

;; test
(= '(2 1 0) (nth-permutation (range 3) 6))

;; problem
(apply str (nth-permutation (range 10) 1e6))
