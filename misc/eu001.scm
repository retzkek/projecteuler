; project euler (projecteuler.net) problem 1
; solution by kevin retzke, july 2012
(define (range start end)
	(if (< (+ start 1) end) (cons start (range (+ start 1) end))
		(list (- end 1)))
)
(define (div35? n) (or (= (modulo n 3) 0) (= (modulo n 5) 0)))
(display (reduce + 0 (filter div35? (range 1 1000))))
(newline)
