(ns kmr.projecteuler)

;; a+b+c = 1000
;; a^2+b^2 = c^2
;; a < b < c

(defn triplet-with-sum [n]
  (loop [a 1]
    (let [b (int (/ (- (* n n) (* 2 n a)) (* 2 (- n a))))
          c (- n a b)]
      (if (and (== (+ (* a a) (* b b)) (* c c))
              (> c b a))
        (* a b c)
        (recur (inc a))))))

(def run-problem '(triplet-with-sum 1000))
