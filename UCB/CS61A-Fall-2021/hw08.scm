(define (my-filter func lst)
  (cond ((null? lst) nil)     ; base case: an empty list
        ((func (car lst))
           (cons (car lst) (my-filter func (cdr lst))))
        (else (my-filter func (cdr lst))))
)

(define (interleave s1 s2)
  (cond ((and (null? s1) (null? s2)) nil)                ; base case: return nil if both are empty
        ((null? s1) (interleave s2 s1))                  ; change the positions of s1 and s2
        (else (cons (car s1) (interleave s2 (cdr s1))))) ; we always insert (car s1) to the result :)
)

(define (accumulate merger start n term)
  (cond ((= n 1) (merger (term n) start))           ; base case: n = 1
        (else (merger (term n) (accumulate merger start (- n 1) term))))
)

(define (no-repeats lst)
  (cond ((null? lst) nil)
        (else (cons (car lst) 
                    (no-repeats 
                       ; choose the elements that are not equal to `car lst`
                       (my-filter (lambda (x) (not (= x (car lst)))) (cdr lst))))))
)
