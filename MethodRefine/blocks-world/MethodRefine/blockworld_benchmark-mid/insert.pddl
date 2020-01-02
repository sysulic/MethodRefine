(define (problem blocksworld-4-0)
(:domain blocksworld)
(:objects
 block-1 block-2 block-3 block-4 block-5 - block
)
(:init (on-table block-3) (on-table block-1) (on-table block-5) (clear block-3) (clear block-2) (clear block-1) (on block-4 block-5) (on block-2 block-4) (hand-empty) )
(:goal (and (holding block-2) (clear block-1) ))
)