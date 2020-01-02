( define ( domain satellite )
  ( :requirements :strips :typing :equality :htn )
  ( :types direction instrument mode satellite )
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
      ( not ( pointing ?s ?d_prev ) )
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
      ( not ( calibrated ?i ) )
      ( not ( power_avail ?s ) )
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
      ( not ( power_on ?i ) )
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
      ( not ( not_calibrated ?i ) )
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

  ( :method GET_IMAGE
    :parameters
    (
      ?goal_dir - direction
      ?goal_mode - mode
    )
    :precondition
    ( and 
      ( HAVE_IMAGE ?goal_dir ?goal_mode ) 
    )
    :subtasks
    (  )
  )

  ( :method GET_IMAGE
    :parameters
    (
      ?goal_dir - direction
      ?goal_mode - mode
    )
    :vars
    (
      ?using_inst - instrument
      ?using_sat - satellite
    )
    :precondition
    ( and
      ( calibrated ?using_inst )
      ( on_board ?using_inst ?using_sat )
      ( supports ?using_inst ?goal_mode )
      ( power_on ?using_inst )
      ( pointing ?using_sat ?goal_dir )
    )
    :subtasks
    ( 
      ( !TAKE_IMAGE ?using_sat ?goal_dir ?using_inst ?goal_mode )
    )
  )

  ( :method GET_IMAGE
    :parameters
    (
      ?goal_dir - direction
      ?goal_mode - mode
    )
    :vars
    (
      ?using_inst - instrument
      ?using_sat - satellite
      ?old_dir - direction
    )
    :precondition
    ( and
      ( calibrated ?using_inst )
      ( on_board ?using_inst ?using_sat )
      ( supports ?using_inst ?goal_mode )
      ( power_on ?using_inst )
      ( pointing ?using_sat ?old_dir )
      ( not ( = ?old_dir ?goal_dir ) )
    )
    :subtasks
    ( 
      ( !TURN_TO ?using_sat ?goal_dir ?old_dir )
      ( GET_IMAGE ?goal_dir ?goal_mode )
    )
  )

  ( :method GET_IMAGE
    :parameters
    (
      ?goal_dir - direction
      ?goal_mode - mode
    )
    :vars
    (
      ?using_inst - instrument
      ?using_sat - satellite
      ?calib_dir - direction
    )
    :precondition
    ( and
      ( not_calibrated ?using_inst )
      ( on_board ?using_inst ?using_sat )
      ( supports ?using_inst ?goal_mode )
      ( power_on ?using_inst )
      ( pointing ?using_sat ?calib_dir )
      ( calibration_target ?using_inst ?calib_dir )
    )
    :subtasks
    ( 
      ( !CALIBRATE ?using_sat ?using_inst ?calib_dir )
      ( GET_IMAGE ?goal_dir ?goal_mode )
    )
  )

  ( :method GET_IMAGE
    :parameters
    (
      ?goal_dir - direction
      ?goal_mode - mode
    )
    :vars
    (
      ?using_inst - instrument
      ?using_sat - satellite
      ?calib_dir - direction
      ?old_dir - direction
    )
    :precondition
    ( and
      ( not_calibrated ?using_inst )
      ( on_board ?using_inst ?using_sat )
      ( supports ?using_inst ?goal_mode )
      ( power_on ?using_inst )
      ( pointing ?using_sat ?old_dir )
      ( calibration_target ?using_inst ?calib_dir )
      ( not ( = ?old_dir ?calib_dir ) )
    )
    :subtasks
    ( 
      ( !TURN_TO ?using_sat ?calib_dir ?old_dir )
      ( GET_IMAGE ?goal_dir ?goal_mode )
    )
  )

  ( :method GET_IMAGE
    :parameters
    (
      ?goal_dir - direction
      ?goal_mode - mode
    )
    :vars
    (
      ?using_inst - instrument
      ?using_sat - satellite
    )
    :precondition
    ( and
      ( on_board ?using_inst ?using_sat )
      ( supports ?using_inst ?goal_mode )
      ( power_avail ?using_sat )
    )
    :subtasks
    ( 
      ( !SWITCH_ON ?using_inst ?using_sat )
      ( GET_IMAGE ?goal_dir ?goal_mode )
    )
  )

  ( :method GET_IMAGE
    :parameters
    (
      ?goal_dir - direction
      ?goal_mode - mode
    )
    :vars
    (
      ?using_inst - instrument
      ?using_sat - satellite
      ?old_inst - instrument
    )
    :precondition
    ( and
      ( on_board ?using_inst ?using_sat )
      ( supports ?using_inst ?goal_mode )
      ( on_board ?old_inst ?using_sat )
      ( power_on ?old_inst )
      ( not ( = ?old_inst ?using_inst ) )
    )
    :subtasks
    ( 
      ( !SWITCH_OFF ?old_inst ?using_sat )
      ( GET_IMAGE ?goal_dir ?goal_mode )
    )
  )


)

