#lang racket

(require rackunit)

(define (file->inputs f) (map string->number (file->lines f)))
(define example-file "../files/day09_example.txt")
(define input-file "../files/day09.txt")
(define inputs (file->inputs input-file))
(define consider 25)

(define (valid? options n)
  (for*/first ([i (in-list options)]
               [j (in-list (cdr options))]
               #:when (= (+ i j) n))
    #t))


(define (attack inputs [consider 25])
  (let loop ([idx consider])
    (cond
      [(> idx (sub1 (length inputs))) #f]
      [(valid? (take (drop inputs (- idx consider)) consider)
               (list-ref inputs idx))
       (loop (add1 idx))]
      [else (list-ref inputs idx)])))

; part 1
(define weakness (attack inputs consider))
(check-eq? weakness 20874512)

(define (find-enc-weaknesses inputs weakness)
  (let loop ([idx 0]
             [ns (take inputs 2)])
    (cond
      ; We didn't find any matches
      [(> idx (sub1 (length inputs))) #f]
      ; No more numbers to take, move to next idx
      [(= (length ns) (length (drop inputs idx))) (loop (add1 idx) (take (drop inputs idx) 2))]
      ; Here's our match
      [(= (apply + ns)  weakness) ns]
      ; No match, so take an additional number
      [else (loop idx (take (drop inputs idx) (add1 (length ns))))])))

(define enc-weaknesses (find-enc-weaknesses inputs weakness))
(define enc-weakness (+ (apply max enc-weaknesses) (apply min enc-weaknesses)))
(check-eq? enc-weakness 3012420)
