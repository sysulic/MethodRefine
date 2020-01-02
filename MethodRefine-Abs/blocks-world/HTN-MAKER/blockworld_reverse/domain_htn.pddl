( define ( domain Blocks4 )
  ( :requirements :strips :typing :equality :htn )
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

  ( :method Make-On-Table
    :parameters ( ?goal - block )
    :precondition
    ( and
      ( on-table ?goal )
    )
    :subtasks
    (
    )
  )

  ( :method Make-On-Table
    :parameters ( ?goal - block )
    :precondition
    ( and
      ( holding ?goal )
    )
    :subtasks
    (
      ( !Putdown ?goal )
    )
  )

  ( :method Make-On-Table
    :parameters ( ?goal - block )
    :vars
    (
      ?is_on - block
    )
    :precondition
    ( and
      ( hand-empty )
      ( on ?goal ?is_on )
      ( clear ?goal )
    )
    :subtasks
    (
      ( !Unstack ?goal ?is_on )
      ( Make-On-Table ?goal )
    )
  )

  ( :method Make-On-Table
    :parameters ( ?goal - block )
    :vars
    (
      ?is_held - block
    )
    :precondition
    ( and
      ( holding ?is_held )
    )
    :subtasks
    (
      ( !Putdown ?is_held )
      ( Make-On-Table ?goal )
    )
  )

  ( :method Make-On-Table
    :parameters ( ?goal - block )
    :vars
    (
      ?on_goal - block
    )
    :precondition
    ( and
      ( on ?on_goal ?goal )
    )
    :subtasks
    (
      ( Make-Clear ?goal )
      ( Make-On-Table ?goal )
    )
  )

  ( :method Make-On
    :parameters ( ?top - block ?bottom - block )
    :precondition
    ( and
      ( on ?top ?bottom )
    )
    :subtasks
    (
    )
  )

  ( :method Make-On
    :parameters ( ?top - block ?bottom - block )
    :precondition
    ( and
      ( clear ?bottom )
      ( holding ?top )
    )
    :subtasks
    (
      ( !Stack ?top ?bottom )
    )
  )

  ( :method Make-On
    :parameters ( ?top - block ?bottom - block )
    :precondition
    ( and
      ( clear ?bottom )
      ( clear ?top )
      ( on-table ?top )
      ( hand-empty )
    )
    :subtasks
    (
      ( !Pickup ?top )
      ( Make-On ?top ?bottom )
    )
  )

  ( :method Make-On
    :parameters ( ?top - block ?bottom - block )
    :vars
    (
      ?below_top - block
    )
    :precondition
    ( and
      ( clear ?bottom )
      ( clear ?top )
      ( on ?top ?below_top )
      ( hand-empty )
    )
    :subtasks
    (
      ( !Unstack ?top ?below_top )
      ( Make-On ?top ?bottom )
    )
  )

  ( :method Make-On
    :parameters ( ?top - block ?bottom - block )
    :vars
    (
      ?is_held - block
    )
    :precondition
    ( and
      ( clear ?bottom )
      ( clear ?top )
      ( holding ?is_held )
    )
    :subtasks
    (
      ( !Putdown ?is_held )
      ( Make-On ?top ?bottom )
    )
  )

  ( :method Make-On
    :parameters ( ?top - block ?bottom - block )
    :vars
    (
      ?on_top - block
    )
    :precondition
    ( and
      ( clear ?bottom )
      ( on ?on_top ?top )
    )
    :subtasks
    (
      ( Make-Clear ?top )
      ( Make-On ?top ?bottom )
    )
  )

  ( :method Make-On
    :parameters ( ?top - block ?bottom - block )
    :vars
    (
      ?on_bottom - block
    )
    :precondition
    ( and
      ( on ?on_bottom ?bottom )
    )
    :subtasks
    (
      ( Make-Clear ?bottom )
      ( Make-On ?top ?bottom )
    )
  )

  ( :method Make-Clear
    :parameters ( ?goal - block )
    :precondition
    ( and
      ( clear ?goal )
    )
    :subtasks
    (
    )
  )

  ( :method Make-Clear
    :parameters ( ?goal - block )
    :vars
    (
      ?on_goal - block
    )
    :precondition
    ( and
      ( on ?on_goal ?goal )
      ( clear ?on_goal )
      ( hand-empty )
    )
    :subtasks
    (
      ( !Unstack ?on_goal ?goal )
    )
  )

  ( :method Make-Clear
    :parameters ( ?goal - block )
    :vars
    (
      ?on_goal - block
      ?is_held - block
    )
    :precondition
    ( and
      ( on ?on_goal ?goal )
      ( clear ?on_goal )
      ( holding ?is_held )
    )
    :subtasks
    (
      ( !Putdown ?is_held )
      ( Make-Clear ?goal )
    )
  )

  ( :method Make-Clear
    :parameters ( ?goal - block )
    :vars
    (
      ?on_goal - block
      ?on_on_goal - block
    )
    :precondition
    ( and
      ( on ?on_goal ?goal )
      ( on ?on_on_goal ?on_goal )
    )
    :subtasks
    (
      ( Make-Clear ?on_goal )
      ( Make-Clear ?goal )
    )
  )

)
