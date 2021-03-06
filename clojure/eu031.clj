(defn count-coins 
  [coins rem]
  (cond (= rem 0) 1
        (= (count coins) 0) 0
        (<= (first coins) rem)
          (+ (count-coins coins (- rem (first coins)))
             (count-coins (rest coins) rem))
        :else  (count-coins (rest coins) rem)))
(def coins (list 200 100 50 20 10 5 2 1))

(def run-test '(println "no test"))
(def run-problem '(count-coins coins 200))
