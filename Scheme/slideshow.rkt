#lang slideshow
(define c (circle 10))
(define r (rectangle 10 20))
(define (square n)
  (filled-rectangle n n))
(define (four p)
  (define two-p (hc-append p p))
  (vc-append two-p two-p))
(define (checker p1 p2)
  (let ([p12 (
