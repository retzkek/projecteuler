(defn next-fib 
  "Computes next number in the fibonacci sequence,
  returns next and previous as list.
  e.g. (next-fib '(2 1)) -> '(3 2)"
  [xs] 
  (list (+ (first xs) (second xs)) (first xs)))

(defn even-fib-sum
  "Computes sum of all even-numbered members of the 
  fibonacci sequence below max-n"
  [max-n]
  (loop [fibs '(2 1)
         sum 0]
    (if (> (first fibs) max-n)
      sum
      (recur (next-fib fibs) 
             (if (even? (first fibs))
               (+ sum (first fibs))
               sum)))))

(def run-test '(= (even-fib-sum 50) 44))
(def run-problem '(even-fib-sum 4e6))
;(even-fib-sum 4e6) ;-> 4613732
