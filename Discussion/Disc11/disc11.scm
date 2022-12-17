; Question 1.2
; Write a tail recursive function, reverse, that takes in a Scheme list and returns a
; reversed copy.
(define (reverse lst)
  (define (reverse-helper lst sofar)
    (if (null? lst)
        sofar
        (reverse-helper (cdr lst) (cons (car lst) sofar))))
  (reverse-helper lst nil))

; Question 1.3
; Write a tail recursive function, insert, that takes in a number and a sorted list.
; The function returns a sorted copy with the number inserted in the correct position.
; For example, (insert 6 '(2 4 5 7)) should result in (2 4 5 6 7).
(define (insert n lst)
  (define (insert-helper lst result)
    (cond 
      ((null? lst)
       (cons n result))
      ((< n (car lst))
       (append (reverse lst) (cons n result)))
      (else
       (insert-helper (cdr lst) (cons (car lst) result)))))
  (reverse (insert-helper lst nil)))

; Question 3.1
; Write a macro that takes in two expressions and or’s them together (applying short-
; circuiting rules). However, do this without using the or special form. You may also
; assume the name v1 doesn’t appear anywhere outside of our macro. Fill in the
; implementation below.
(define-macro (or-macro expr1 expr2)
  `(let ((v1 ,expr1))
     (if v1
         v1
         ,expr2)))

; Question 3.2
; Write a macro that takes in a call expression and strips out every other argument.
; The first argument is kept, the second is removed, and so on. You may find it
; helpful to write a helper function.

(define (prune lst)
  (if (or (null? lst) (null? (cdr lst)))
      lst
      (cons (car lst) (prune (cdr (cdr lst))))))

(define-macro (prune-expr expr)
  (cons (car expr) (prune (cdr expr))))

; Question 3.3
; Using macros, let's make a new special form, when, that has the following structure:
; (when <condition>
; (<expr1> <expr2> <expr3> ...))
; If the condition is not false (a truthy expression), all the subsequent operands are
; evaluated in order and the value of the last expression is returned. Otherwise, the
; entire when expression evaluates to okay.

; (a) Fill in the skeleton below to implement this without using quasiquotes.
(define-macro (when condition exprs)
  (list 'if condition (cons 'begin exprs) ''okay))

; (b) Now, implement the macro using quasiquotes.
(define-macro (when condition exprs)
  `(if ,condition ,(cons 'begin exprs) 'okay))
