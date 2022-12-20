; Question 1.3
; Write a function map-stream, which takes a function f and a stream s. It returns a
; new stream which has all the elements from s, but with f applied to each one.
(define (map-stream f s)
  (if (null? s) nil
      (cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

; Question 1.4
; Write a function slice which takes in a stream s, a start, and an end. It should
; return a Scheme list that contains the elements of s between index start and end,
; not including end. If the stream ends before end, you can return nil.
(define (slice s start end)
  (cond ((null? s)   nil)
        ((> start 0) (slice (cdr-stream s) (- start 1) (- end 1)))
        ((> end 0)   (cons (car s) (slice (cdr-stream s) start (- end 1))))
        (else        nil)))

; Question 1.5
; Since streams only evaluate the next element when they are needed, we can combine
; infinite streams together for interesting results! Use it to define a few of our favorite
; sequences. We've defined the function combine-with for you below, as well as an
; example of how to use it to define the stream of even numbers.
(define (combine-with f xs ys)
  (if (or (null? xs) (null? ys))
      nil
      (cons-stream
        (f (car xs) (car ys))
        (combine-with f (cdr-stream xs) (cdr-stream ys)))))

; For these questions, you may use the naturals stream in addition to combine-with.
(define (naturals start) (cons-stream start (naturals (+ start 1))))

(define factorials (cons-stream 1 (combine-with * (naturals 1) factorials)))
(define fibs (cons-stream 0 (cons-stream 1 (combine-with + (cdr-stream fibs) fibs))))

; Question 1.6
; We can even represent the sequence of all prime numbers as an infinite stream!
; Define a function sieve, which takes in a stream of increasing numbers and returns
; a stream containing only those numbers which are not multiples of an earlier number
; in the stream. We can define primes by sifting all natural numbers starting at 2.
; Look online for the Sieve of Eratosthenes if you need some inspiration.
; Hint: You might find using filter-stream as defined earlier helpful.
(define (filter-stream f s)
  (cond ((null? s)   nil)
        ((f (car s)) (cons-stream (car s) (filter-stream f (cdr-stream s))))
        (else        (filter-stream f (cdr-stream s)))))

(define (sieve s)
  (if (null? s) nil
      (let ((first (car s)))
      (cons-stream first (sieve (filter-stream (lambda (x) (not (zero? (modulo x first)))) (cdr-stream s))))))
      )