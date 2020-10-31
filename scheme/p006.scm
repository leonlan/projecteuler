;scheme --quiet < p006.scm
(define (sum term a next b)
  (if (> a b)
      0
      (+ (term a)
         (sum term (next a) next b))))
(define (inc x) (+ x 1))

(define (sum-squares n)
  (define (square x) (* x x))
  (sum square 1 inc n))

(define (square-sum n)
  (define (identity x) x)
  (square (sum identity 1 inc n)))

(define (difference n)
  (- (sum-squares n) (square-sum n)))

(define (p006 n)
  (abs (difference n)))

(display (p006 100))
(newline)
