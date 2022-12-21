(define (rle s)
  (if (null? s) nil
      (let ((c (rle (cdr-stream s))))
        (if (and (not (null? c)) (= (car s) (car (car c))))
            (cons-stream (list (car s) (+ 1 (car (cdr (car c))))) (cdr-stream c))
            (cons-stream (list (car s) 1) c)))))



(define (cadr s)
  (if (or (null? s) (null? (cdr s))) nil
      (car (cdr s))))
(define (find-nondecreasing s prev)
  (if (or (null? s) (and (not (null? prev)) (< (car s) prev))) nil
      (cons (car s) (find-nondecreasing (cdr-stream s) (car s)))))
(define (find-decr s prev)
  (if (null? s) nil
  (if (and (not (null? prev)) (< (car s) prev)) s
      (find-decr (cdr-stream s) (car s)))))
(define (group-by-nondecreasing s)
  (if (null? s) nil
      (cons-stream (find-nondecreasing s nil) (group-by-nondecreasing (find-decr s nil)))))


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))

