(define (even? n)
  (= (remainder n 2) 0))

(define (even-fibonnaci sum a b max-number)
  (cond ((> b max-number) sum)
        ((even? b) (even-fibonnaci (+ sum b) b (+ a b) max-number))
        (else (even-fibonnaci sum b (+ a b) max-number))))

(define (p002 n)
  (even-fibonnaci 0 1 2 n))

(display (p002 4000000))
(newline)
