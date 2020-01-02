( define 
  ( domain satellite )
  ( :requirements :strips :typing :equality )
  ( :types satellite direction instrument mode )

  ( :predicates
    ( on_board ?i - instrument ?s - satellite )
    ( supports ?i - instrument ?m - mode )
    ( pointing ?s - satellite ?d - direction )
    ( power_avail ?s - satellite )
    ( power_on ?i - instrument )
    ( calibrated ?i - instrument )
    ( not_calibrated ?i - instrument )
    ( have_image ?d - direction ?m - mode )
    ( calibration_target ?i - instrument ?d - direction )
    ( different ?d_new - direction ?d_pre - direction )
  )

  ( :action !TURN_TO
    :parameters
    (
      ?s - satellite
      ?d_new - direction
      ?d_prev - direction
    )
    :precondition
    ( and 
      ( pointing ?s ?d_prev )
      ( not ( = ?d_new ?d_prev ) )
    )
    :effect
    ( and 
      ( pointing ?s ?d_new )
      ( not 
        ( pointing ?s ?d_prev )
      )
    )
  )

  ( :action !SWITCH_ON
    :parameters
    (
      ?i - instrument
      ?s - satellite
    )
    :precondition
    ( and 
      ( on_board ?i ?s )
      ( power_avail ?s )
    )
    :effect
    ( and 
      ( power_on ?i )
      ( not_calibrated ?i )
      ( not 
        ( calibrated ?i )
      )
      ( not 
        ( power_avail ?s )
      )
    )
  )

  ( :action !SWITCH_OFF
    :parameters
    (
      ?i - instrument
      ?s - satellite
    )
    :precondition
    ( and 
      ( on_board ?i ?s )
      ( power_on ?i )
    )
    :effect
    ( and 
      ( power_avail ?s )
      ( not 
        ( power_on ?i )
      )
    )
  )

  ( :action !CALIBRATE
    :parameters
    (
      ?s - satellite
      ?i - instrument
      ?d - direction
    )
    :precondition
    ( and 
      ( on_board ?i ?s )
      ( calibration_target ?i ?d )
      ( pointing ?s ?d )
      ( power_on ?i )
      ( not_calibrated ?i )
    )
    :effect
    ( and
      ( calibrated ?i )
      ( not
        ( not_calibrated ?i )
      )
    )
  )

  ( :action !TAKE_IMAGE
    :parameters
    (
      ?s - satellite
      ?d - direction
      ?i - instrument
      ?m - mode
    )
    :precondition
    ( and 
      ( calibrated ?i )
      ( on_board ?i ?s )
      ( supports ?i ?m )
      ( power_on ?i )
      ( pointing ?s ?d )
      ( power_on ?i )
    )
    :effect
    ( and
      ( have_image ?d ?m )
    )
  )
)
