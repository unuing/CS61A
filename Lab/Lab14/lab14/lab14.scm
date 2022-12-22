(define (split-at lst n)
  (if (null? lst) (cons nil nil)
  (if (zero? n)   (cons nil lst)
  (let ((s (split-at (cdr lst) (- n 1))))
      (cons (cons (car lst) (car s)) (cdr s))))))


; (define-macro (switch expr cases)
	; (cons 'cond
		; (map (lambda (case) (cons (list 'eq? expr (car case)) (cdr case)))
    			; cases))
; )

(define-macro (switch expr cases)
	 (cons 'cond 
	   (map (lambda (case) (cons (list 'eq? expr (list 'quote (car case))) (cdr case))) 
    			cases)))