; project euler (projecteuler.net) problem 3
; solution by Kevin Retzke (retzkek@gmail.com)
; November 2012, 2013

(defn largest-prime-factor
  "Calculate the largest prime factor of num."
  ([n] (largest-prime-factor n 2 1))
  ([n fac result]
   (cond
    (> (* fac fac) n)
      (if (= n 1) result n)
    (and (= (rem n fac) 0) (> fac result))
      (largest-prime-factor (/ n fac) fac fac)
    :default
      (largest-prime-factor n (inc fac) result))))

(def run-test '(= (largest-prime-factor 13195) 29))
(def run-problem '(largest-prime-factor 600851475143))
