(require hy.contrib.loop)

(defn next-fib [xs]
  "Computes next number in the fibonacci sequence,
  returns next and previous as list.
  e.g. (next-fib '(2 1)) -> '(3 2)"
  [(+ (first xs) (second xs)) (first xs)])

(defn even-fib-sum [max-n]
  "Computes sum of all even-numbered members of the 
  fibonacci sequence below max-n"
  (loop [[fibs [2 1]]
         [sum 0]]first
    (if (> (first fibs) max-n)
      sum
      (recur (next-fib fibs) 
             (if (even? (first fibs))
               (+ sum (first fibs))
               sum)))))

(defmain [&rest args]
  (if (> (len args) 1)
    (print "test:" (= (even-fib-sum 50) 44))
    (print "result:" (even-fib-sum 4e6))))
