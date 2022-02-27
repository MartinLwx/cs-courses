(define (cddr s) (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)

(define (ordered? s)
  (cond ( (null? s) #t)                     ; base case 1. empty list
        ( (null? (cdr s)) #t)               ; base case 2. a list with size 1
        ( else (and (<= (car s) (cadr s))
               (ordered? (cdr s)))))
)

(define (square x) (* x x))

(define (pow base exp)
  (cond ( (= exp 1) base )                                    ; base^1 = base
        ( (= exp 0) 1)                                        ; base^0 = 1
        ( (= 0 (modulo exp 2))
            (begin
              (define tmp (pow base (quotient exp 2)))        ; store the value temporarily
              (* tmp tmp)
            )
        )
        ( (= 1 (modulo exp 2))
            (begin
              (define tmp (pow base (quotient exp 2)))        ; store the value temporarily
              (* tmp tmp base)
            )
        )
  )
)
