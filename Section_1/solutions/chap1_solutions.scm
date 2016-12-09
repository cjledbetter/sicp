10
;Value: 10


(+ 5 3 4)
;Value: 12

(- 9 1)
;Value: 8

(/ 6 2)
;Value: 3

(+ (* 2 4) (- 4 6))
;Value: 6

(define a 3)
;Value: a

(define b (+ a 1))
;Value: b


(+ a b (* a b))
;Value: 19

(= a b)
;Value: #f

(if (and (> b a) (< b (* a b)))
    b
    a)
;Value: 4

(cond ((= a 4) 6)
      ((= b 4) (+ 6 7 a))
      (else 25))
;Value: 16

(+ 2 (if (> b a) b a))
;Value: 6

(* (cond ((> a b) a)
         ((< a b) b)
         (else -1))
   (+ a 1))
;Value: 16

; I hand wrote all of these solutions and was 100% correct

(/ (+ 5 4
     (- 2
      (- 3
       (+ 6
        ( / 4 5)))))
    (* 3
      ( - 6 2)
      (- 2 7)))
;Value: -37/150

; Did not get correct but need to be more careful 

(define (squarert x) (* x x))
;Value: squarert

(squarert 3)
;Value: 9

(define (sum_of_sqr x y) (+ (squarert x) (squarert y)))
;Value: sum_of_sqr

(sum_of_sqr 3 4)
;Value: 25


