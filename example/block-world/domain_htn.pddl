( define ( domain blocksworld )
  ( :requirements :strips :typing :equality)
  ( :types block )

  (:predicates (on-table ?b - block)
    	       (on ?b1 - block ?b2 - block)
    	       (clear ?b - block)
    	       (hand-empty)
    	       (holding ?b - block))

  ( :action PICK-UP
    :parameters     (?b - block)
    :precondition   (and (clear ?b) (hand-empty) (on-table ?b))
    :effect         (and (not ( clear ?b )) (not (hand-empty)) (holding ?b))
  )

  ( :action PICK-UP-FROM-BLOCK
    :parameters     (?b1 - block ?b2 - block)
    :precondition   (and (clear ?b1) (hand-empty) (on ?b1 ?b2))
    :effect         (and (not ( clear ?b1 )) (not (hand-empty)) (holding ?b1) (clear ?b2))
  )

  ( :action PUT-DOWN
    :parameters     (?b - block)
    :precondition   (and (holding ?b))
    :effect         (and (not (holding ?b)) (hand-empty) (on-table ?b) (clear ?b))
  )

  ( :action STACK
    :parameters     (?b1 - block ?b2 - block)
    :precondition   (and (holding ?b1) (clear ?b2))
    :effect	    (and (not (holding ?b1)) (not (clear ?b2)) (hand-empty) (on ?b1 ?b2) (clear ?b1))
  )
)
