(define-macro (def func args body)
  `(define ,(cons func args) ,body))

(define (map-stream f s)
  (if (null? s)
      nil
      (cons-stream (f (car s))
                   (map-stream f (cdr-stream s)))))

(define all-three-multiples
        (cons-stream 3
                     (map-stream (lambda (x) (+ x 3))
                                 all-three-multiples)))

(define (compose-all funcs)
  (cond
    ((null? funcs)
     (lambda (x) x))
    ((null? (cdr funcs))
     (car funcs))
    (else
     (compose-all (cons
                   (lambda (x) ((car (cdr funcs)) ((car funcs) x)))
                   (cdr (cdr funcs)))))))

(define (partial-sums stream)
  (define (helper sum stream)
    (if (null? stream)
        nil
        (let ((sum (+ sum (car stream))))
          (cons-stream sum (helper sum (cdr-stream stream))))))
  (helper 0 stream))
