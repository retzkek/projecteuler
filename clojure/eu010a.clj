(ns kmr.projecteuler)

(defn eratos
  "Compute all primes below n using Sieve of Eratosthenes. Uses Java Boolean array of odds."
  [n]
  (let [array (boolean-array (-> n (quot 2) (dec)) true) ;; 0=3,1=5,2=7,...
        n-to-i (fn [n] (-> n (- 3) (/ 2)))
        i-to-n (fn [i] (+ i i 3))]
    (loop [i 3]
      (if (> (* i i) n)
        (areduce array ii ret [2]
                 (if (aget array ii)
                   (conj ret (i-to-n ii))
                   ret))
        (recur (do
                 (doseq [j (range (+ i i) n i)]
                   (if (odd? j)
                     (aset-boolean array (n-to-i j) false)))
                 (+ i 2)))))))

(def run-test '(= 17 (reduce + (eratos 8))))
(def run-problem '(reduce + (eratos 2e6)))
