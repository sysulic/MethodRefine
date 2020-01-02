( define 
  ( tasks logistics-tasks )

  ( :task Deliver-Pkg
    :parameters
    (
      ?obj - obj
      ?dst - location
    )
    :precondition
    (
    )
    :effect
    ( and
      ( obj-at ?obj ?dst )
    )
  )

)
