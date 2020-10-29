(define (sum-multiples-3-5 sum count max-count)
  (cond ((= max-count count) sum)
        ((or (= (remainder count 3) 0) (= (remainder count 5) 0))
         (sum-multiples-3-5 (+ sum count) (+ count 1) max-count))
        (else (sum-multiples-3-5 sum (+ count 1) max-count))))

(define (p001 n)
  (sum-multiples-3-5 0 1 1000))

(display (p001 1000))
(newline)
