( define 
  ( tasks Satellite-tasks )

  ( :task Get_Image
    :parameters
    (
      ?goal_dir - direction
      ?goal_mode - mode
    )
    :precondition
    (
    )
    :effect
    ( and
      ( have_image ?goal_dir ?goal_mode )
    )
  )

)
