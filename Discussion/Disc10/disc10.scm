; Question 4.1
; Write a function that returns the factorial of a number.
(define (factorial x)
  (if (= x 0)
      1
      (* x (factorial (- x 1)))))

; Question 4.2
; Write a function that returns the nth Fibonacci number.
(define (fib n)
  (if (<= n 1)
      n
      (+ (fib (- n 1)) (fib (- n 2)))))

; Question 5.1
; Write a function which takes two lists and concatenates them.
; Notice that simply calling (cons a b) would not work because it will create a
; deep list. Do not call the builtin procedure append, which does the same thing as
; my-append.
(define (my-append a b)
  (if (null? a)
      b
      (cons (car a) (my-append (cdr a) b))))

; Question 5.2
; Write a Scheme function that, when given an element, a list, and an index, inserts
; the element into the list at that index.
(define (insert element lst index)
  (if (= index 0)
      (cons element lst)
      (cons (car lst)
            (insert element (cdr lst) (- index 1)))))

; Question 5.3
; Write a Scheme function that, when given a list, such as (1 2 3 4), duplicates
; every element in the list (i.e. (1 1 2 2 3 3 4 4)).
(define (duplicate lst)
  (if (null? lst)
      nil
      (cons (car lst)
            (cons (car lst) (duplicate (cdr lst))))))
