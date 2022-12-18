(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s)))

(define (caddr s)
  (car (cddr s)))


(define (sign num)
  (cond ((= num 0) 0)
        ((< num 0) -1)
        ((> num 0) 1)))


(define (square x) (* x x))

(define (pow x y)
  (cond ((= y 0) 1)
        ((even? y) (square (pow x (quotient y 2))))
        (else (* x (pow x (- y 1))))))


(define (unique s)
  (if (null? s)
    nil
    (cons (car s) (filter (lambda (x) (not (equal? x (car s)))) (unique (cdr s))))))


(define (replicate x n)
  (define (replicate-helper x n sofar)
    (if (zero? n)
      sofar
      (replicate-helper x (- n 1) (cons x sofar))))
  (replicate-helper x n nil))


(define (accumulate combiner start n term)
  (if (zero? n)
      start
      (accumulate combiner (combiner start (term n)) (- n 1) term)))


(define (accumulate-tail combiner start n term)
  (if (zero? n)
      start
      (accumulate-tail combiner (combiner start (term n)) (- n 1) term)))


(define-macro (list-of map-expr for var in lst if filter-expr)
  `(map (lambda (,var) ,map-expr) (filter (lambda (,var) ,filter-expr) ,lst)))

