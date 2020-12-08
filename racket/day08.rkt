#lang racket

(define inputs
  (map (lambda (l)
         (let* ([ls (string-split l)])
           (list (string->symbol (first ls))
                 (string->number (second ls)))))
       (file->lines "../files/day08.txt")))

(define (run instructions)
  (let loop ([acc 0]
             [idx 0]
             [visited (list)])
    (cond
      [(> idx (sub1 (length instructions))) (list 'finished  acc)]
      [(member idx visited) (list 'infinite-loop acc)]
      [else (match (list-ref instructions idx)
              [`(acc ,n) (loop (+ acc n) (add1 idx) (cons idx visited))]
              [`(jmp ,n) (loop acc (+ idx n) (cons idx visited))]
              [`(nop ,_) (loop acc (add1 idx) visited)])])))

; part 1
(displayln (run inputs))

(define (build-tests instructions)
  (for/fold ([acc (list)])
            ([i (in-list instructions)]
             [idx (in-range (length instructions))])
    (match i
      [`(jmp ,n) (cons (list-set instructions idx `(nop ,n)) acc)]
      [`(nop ,n) (cons (list-set instructions idx `(jmp ,n)) acc)]
      [_ acc])))

(define (run-tests tests)
  (cond
    [(empty? tests) '()]
    [else (let ([r (run (first tests))])
            (match r
              [(list 'finished n) n]
              [(list 'infinite-loop _) (run-tests (cdr tests))]))]))

; part 2
(displayln (run-tests (build-tests inputs)))
