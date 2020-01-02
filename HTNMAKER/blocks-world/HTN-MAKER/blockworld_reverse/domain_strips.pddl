( define ( domain Blocks4 )
  ( :requirements :strips :typing :equality )
  ( :types block )

  ( :predicates
    ( on-table ?b - block )
    ( on ?b1 - block ?b2 - block )
    ( clear ?b - block )
    ( hand-empty )
    ( holding ?b - block )
  )

  ( :action !Pickup
    :parameters
    (
      ?b - block
    )
    :precondition
    ( and
      ( on-table ?b )
      ( clear ?b )
      ( hand-empty )
    )
    :effect
    ( and
      ( not ( on-table ?b ) )
      ( not ( clear ?b ) )
      ( not ( hand-empty ) )
      ( holding ?b )
    )
  )

  ( :action !Putdown
    :parameters
    (
      ?b - block
    )
    :precondition
    ( and
      ( holding ?b )
    )
    :effect
    ( and
      ( not ( holding ?b ) )
      ( hand-empty )
      ( on-table ?b )
      ( clear ?b )
    )
  )

  ( :action !Unstack
    :parameters
    (
      ?b1 - block
      ?b2 - block
    )
    :precondition
    ( and
      ( on ?b1 ?b2 )
      ( clear ?b1 )
      ( hand-empty )
    )
    :effect
    ( and
      ( not ( on ?b1 ?b2 ) )
      ( not ( clear ?b1 ) )
      ( not ( hand-empty ) )
      ( clear ?b2 )
      ( holding ?b1 )
    )
  )

  ( :action !Stack
    :parameters
    (
      ?b1 - block
      ?b2 - block
    )
    :precondition
    ( and
      ( holding ?b1 )
      ( clear ?b2 )
    )
    :effect
    ( and
      ( not ( holding ?b1 ) )
      ( not ( clear ?b2 ) )
      ( hand-empty )
      ( on ?b1 ?b2 )
      ( clear ?b1 )
    )
  )

)
