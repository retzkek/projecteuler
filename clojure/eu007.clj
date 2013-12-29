(ns kmr.projecteuler)

(defn div-by-any?
  "Tests if n is divisible by any ms."
  [n ms]
  (some zero? (map #(rem n %) ms)))

(defn next-prime
  "Accepting a vector of primes, conjs the next prime
  and returns it. Note: first invocation will return [2 3]."
  ([]
   (next-prime [2] 3))
  ([primes]
   (if (< (count primes) 2)
     (next-prime)
     (next-prime primes (+ 2 (last primes)))))
  ([primes n]
   (if (not (div-by-any? n primes))
     (conj primes n)
     (recur primes (+ n 2)))))

(defn nth-prime
  [n]
  (loop
    [nn n primes []]
    (if (= nn 1)
      (last primes)
      (recur (dec nn) (next-prime primes)))))

(def run-test '(= 13 (nth-prime 6)))
(def run-problem '(nth-prime 10001))
