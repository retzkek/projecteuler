(defn div3or5? [x]
  "tests if x is divisble by 3 or 5"
  (or (= (% x 3) 0) 
      (= (% x 5) 0)))

(defn sum-div-3or5  [n]
  "Computes sum of all integers below n that are 
  divisble by 3 or 5"
  (reduce + (filter div3or5? (range n))))

(defmain [&rest args]
  (if (> (len args) 1)
    (print "test:" (= (sum-div-3or5 10) 23))
    (print "result:" (sum-div-3or5 1000))))
