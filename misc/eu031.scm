#!/usr/bin/guile -s
 project euler (projecteuler.net) problem 31
 solution by kevin retzke, june 2012
!#
(define (count-coins coins rem)
    (cond ((= rem 0) 1)
          ((= (length coins) 0) 0)
          ((<= (car coins) rem)
              (+ (count-coins coins (- rem (car coins)))
                 (count-coins (cdr coins) rem)))
          (else  (count-coins (cdr coins) rem))))
(define coins (list 200 100 50 20 10 5 2 1))
(display (count-coins coins 200))
(newline)
