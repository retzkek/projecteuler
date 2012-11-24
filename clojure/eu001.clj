(defn div3or5? 
  "tests if x is divisble by 3 or 5"
  [x]
  (or (= (rem x 3) 0) 
      (= (rem x 5) 0)))

(defn sum-div-3or5 
  "Computes sum of all integers below n that are 
  divisble by 3 or 5"
  [n]
  (reduce + (filter div3or5? (range n))))

(def run-test '(= (sum-div-3or5 10) 23))
(def run-problem '(sum-div-3or5 1000))
;(sum-div-3or5 1000) ;=> 233168
