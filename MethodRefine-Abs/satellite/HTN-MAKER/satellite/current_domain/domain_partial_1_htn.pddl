( define ( domain satellite )
  ( :requirements :strips :typing :equality :htn )
  ( :types direction instrument mode satellite )
  ( :predicates
    ( ON_BOARD ?i - INSTRUMENT ?s - SATELLITE )
    ( SUPPORTS ?i - INSTRUMENT ?m - MODE )
    ( POINTING ?s - SATELLITE ?d - DIRECTION )
    ( POWER_AVAIL ?s - SATELLITE )
    ( POWER_ON ?i - INSTRUMENT )
    ( CALIBRATED ?i - INSTRUMENT )
    ( NOT_CALIBRATED ?i - INSTRUMENT )
    ( HAVE_IMAGE ?d - DIRECTION ?m - MODE )
    ( CALIBRATION_TARGET ?i - INSTRUMENT ?d - DIRECTION )
    ( DIFFERENT ?d_new - DIRECTION ?d_pre - DIRECTION )
  )
  ( :action !TURN_TO
    :parameters
    (
      ?s - SATELLITE
      ?d_new - DIRECTION
      ?d_prev - DIRECTION
    )
    :precondition
    ( and ( POINTING ?s ?d_prev ) ( not ( = ?d_new ?d_prev ) ) )
    :effect
    ( and ( POINTING ?s ?d_new ) ( not ( POINTING ?s ?d_prev ) ) )
  )
  ( :action !SWITCH_ON
    :parameters
    (
      ?i - INSTRUMENT
      ?s - SATELLITE
    )
    :precondition
    ( and ( ON_BOARD ?i ?s ) ( POWER_AVAIL ?s ) )
    :effect
    ( and ( POWER_ON ?i ) ( NOT_CALIBRATED ?i ) ( not ( CALIBRATED ?i ) ) ( not ( POWER_AVAIL ?s ) ) )
  )
  ( :action !SWITCH_OFF
    :parameters
    (
      ?i - INSTRUMENT
      ?s - SATELLITE
    )
    :precondition
    ( and ( ON_BOARD ?i ?s ) ( POWER_ON ?i ) )
    :effect
    ( and ( POWER_AVAIL ?s ) ( not ( POWER_ON ?i ) ) )
  )
  ( :action !CALIBRATE
    :parameters
    (
      ?s - SATELLITE
      ?i - INSTRUMENT
      ?d - DIRECTION
    )
    :precondition
    ( and ( ON_BOARD ?i ?s ) ( CALIBRATION_TARGET ?i ?d ) ( POINTING ?s ?d ) ( POWER_ON ?i ) ( NOT_CALIBRATED ?i ) )
    :effect
    ( and ( CALIBRATED ?i ) ( not ( NOT_CALIBRATED ?i ) ) )
  )
  ( :action !TAKE_IMAGE
    :parameters
    (
      ?s - SATELLITE
      ?d - DIRECTION
      ?i - INSTRUMENT
      ?m - MODE
    )
    :precondition
    ( and ( CALIBRATED ?i ) ( ON_BOARD ?i ?s ) ( SUPPORTS ?i ?m ) ( POWER_ON ?i ) ( POINTING ?s ?d ) ( POWER_ON ?i ) )
    :effect
    ( and ( HAVE_IMAGE ?d ?m ) )
  )
  ( :method GET_IMAGE
    :parameters
    (
      ?goal_dir - DIRECTION
      ?goal_mode - MODE
    )
    :precondition
    ( and ( HAVE_IMAGE ?goal_dir ?goal_mode ) )
    :subtasks
    (  )
  )

  ( :method GET_IMAGE
    :parameters
    (
      ?auto_2 - DIRECTION
      ?auto_3 - MODE
    )
    :vars
    (
      ?auto_4 - INSTRUMENT
      ?auto_5 - SATELLITE
    )
    :precondition
    ( and ( CALIBRATED ?auto_4 ) ( ON_BOARD ?auto_4 ?auto_5 ) ( SUPPORTS ?auto_4 ?auto_3 ) ( POWER_ON ?auto_4 ) ( POINTING ?auto_5 ?auto_2 ) )
    :subtasks
    ( ( !TAKE_IMAGE ?auto_5 ?auto_2 ?auto_4 ?auto_3 ) )
  )

  ( :method GET_IMAGE
    :parameters
    (
      ?auto_8 - DIRECTION
      ?auto_9 - MODE
    )
    :vars
    (
      ?auto_13 - INSTRUMENT
      ?auto_12 - SATELLITE
      ?auto_15 - SATELLITE
      ?auto_16 - DIRECTION
    )
    :precondition
    ( and ( ON_BOARD ?auto_13 ?auto_12 ) ( SUPPORTS ?auto_13 ?auto_9 ) ( POWER_ON ?auto_13 ) ( POINTING ?auto_12 ?auto_8 ) ( ON_BOARD ?auto_13 ?auto_15 ) ( CALIBRATION_TARGET ?auto_13 ?auto_16 ) ( POINTING ?auto_15 ?auto_16 ) ( NOT_CALIBRATED ?auto_13 ) )
    :subtasks
    ( ( !CALIBRATE ?auto_15 ?auto_13 ?auto_16 )
      ( GET_IMAGE ?auto_8 ?auto_9 ) )
  )

  ( :method GET_IMAGE
    :parameters
    (
      ?auto_146 - DIRECTION
      ?auto_147 - MODE
    )
    :vars
    (
      ?auto_149 - INSTRUMENT
      ?auto_155 - SATELLITE
      ?auto_148 - DIRECTION
      ?auto_154 - DIRECTION
      ?auto_157 - DIRECTION
    )
    :precondition
    ( and ( ON_BOARD ?auto_149 ?auto_155 ) ( SUPPORTS ?auto_149 ?auto_147 ) ( POWER_ON ?auto_149 ) ( not ( = ?auto_146 ?auto_148 ) ) ( not ( = ?auto_148 ?auto_154 ) ) ( CALIBRATION_TARGET ?auto_149 ?auto_154 ) ( NOT_CALIBRATED ?auto_149 ) ( POINTING ?auto_155 ?auto_157 ) ( not ( = ?auto_154 ?auto_157 ) ) )
    :subtasks
    ( ( !TURN_TO ?auto_155 ?auto_154 ?auto_157 )
      ( GET_IMAGE ?auto_146 ?auto_147 ) )
  )

  ( :method GET_IMAGE
    :parameters
    (
      ?auto_159 - DIRECTION
      ?auto_160 - MODE
    )
    :vars
    (
      ?auto_161 - INSTRUMENT
      ?auto_162 - SATELLITE
      ?auto_166 - DIRECTION
      ?auto_164 - DIRECTION
      ?auto_165 - DIRECTION
      ?auto_169 - SATELLITE
    )
    :precondition
    ( and ( ON_BOARD ?auto_161 ?auto_162 ) ( SUPPORTS ?auto_161 ?auto_160 ) ( not ( = ?auto_159 ?auto_166 ) ) ( not ( = ?auto_166 ?auto_164 ) ) ( CALIBRATION_TARGET ?auto_161 ?auto_164 ) ( POINTING ?auto_162 ?auto_165 ) ( not ( = ?auto_164 ?auto_165 ) ) ( ON_BOARD ?auto_161 ?auto_169 ) ( POWER_AVAIL ?auto_169 ) )
    :subtasks
    ( ( !SWITCH_ON ?auto_161 ?auto_169 )
      ( GET_IMAGE ?auto_159 ?auto_160 ) )
  )

  ( :method GET_IMAGE
    :parameters
    (
      ?auto_45 - DIRECTION
      ?auto_46 - MODE
    )
    :vars
    (
      ?auto_50 - INSTRUMENT
      ?auto_49 - SATELLITE
      ?auto_52 - DIRECTION
    )
    :precondition
    ( and ( CALIBRATED ?auto_50 ) ( ON_BOARD ?auto_50 ?auto_49 ) ( SUPPORTS ?auto_50 ?auto_46 ) ( POWER_ON ?auto_50 ) ( POINTING ?auto_49 ?auto_52 ) ( not ( = ?auto_45 ?auto_52 ) ) )
    :subtasks
    ( ( !TURN_TO ?auto_49 ?auto_45 ?auto_52 )
      ( GET_IMAGE ?auto_45 ?auto_46 ) )
  )

  ( :method GET_IMAGE
    :parameters
    (
      ?auto_61 - DIRECTION
      ?auto_62 - MODE
    )
    :vars
    (
      ?auto_64 - INSTRUMENT
      ?auto_63 - SATELLITE
      ?auto_65 - DIRECTION
      ?auto_69 - SATELLITE
      ?auto_70 - DIRECTION
    )
    :precondition
    ( and ( ON_BOARD ?auto_64 ?auto_63 ) ( SUPPORTS ?auto_64 ?auto_62 ) ( POWER_ON ?auto_64 ) ( POINTING ?auto_63 ?auto_65 ) ( not ( = ?auto_61 ?auto_65 ) ) ( ON_BOARD ?auto_64 ?auto_69 ) ( CALIBRATION_TARGET ?auto_64 ?auto_70 ) ( POINTING ?auto_69 ?auto_70 ) ( NOT_CALIBRATED ?auto_64 ) )
    :subtasks
    ( ( !CALIBRATE ?auto_69 ?auto_64 ?auto_70 )
      ( GET_IMAGE ?auto_61 ?auto_62 ) )
  )

  ( :method GET_IMAGE
    :parameters
    (
      ?auto_71 - DIRECTION
      ?auto_72 - MODE
    )
    :vars
    (
      ?auto_74 - INSTRUMENT
      ?auto_77 - SATELLITE
      ?auto_78 - DIRECTION
      ?auto_81 - DIRECTION
    )
    :precondition
    ( and ( ON_BOARD ?auto_74 ?auto_77 ) ( SUPPORTS ?auto_74 ?auto_72 ) ( POWER_ON ?auto_74 ) ( not ( = ?auto_71 ?auto_78 ) ) ( CALIBRATION_TARGET ?auto_74 ?auto_78 ) ( NOT_CALIBRATED ?auto_74 ) ( POINTING ?auto_77 ?auto_81 ) ( not ( = ?auto_78 ?auto_81 ) ) )
    :subtasks
    ( ( !TURN_TO ?auto_77 ?auto_78 ?auto_81 )
      ( GET_IMAGE ?auto_71 ?auto_72 ) )
  )

  ( :method GET_IMAGE
    :parameters
    (
      ?auto_83 - DIRECTION
      ?auto_84 - MODE
    )
    :vars
    (
      ?auto_89 - INSTRUMENT
      ?auto_88 - SATELLITE
      ?auto_87 - DIRECTION
      ?auto_90 - DIRECTION
      ?auto_92 - SATELLITE
    )
    :precondition
    ( and ( ON_BOARD ?auto_89 ?auto_88 ) ( SUPPORTS ?auto_89 ?auto_84 ) ( not ( = ?auto_83 ?auto_87 ) ) ( CALIBRATION_TARGET ?auto_89 ?auto_87 ) ( POINTING ?auto_88 ?auto_90 ) ( not ( = ?auto_87 ?auto_90 ) ) ( ON_BOARD ?auto_89 ?auto_92 ) ( POWER_AVAIL ?auto_92 ) )
    :subtasks
    ( ( !SWITCH_ON ?auto_89 ?auto_92 )
      ( GET_IMAGE ?auto_83 ?auto_84 ) )
  )

  ( :method GET_IMAGE
    :parameters
    (
      ?auto_117 - DIRECTION
      ?auto_118 - MODE
    )
    :vars
    (
      ?auto_123 - INSTRUMENT
      ?auto_121 - SATELLITE
      ?auto_119 - DIRECTION
      ?auto_125 - DIRECTION
    )
    :precondition
    ( and ( CALIBRATED ?auto_123 ) ( ON_BOARD ?auto_123 ?auto_121 ) ( SUPPORTS ?auto_123 ?auto_118 ) ( POWER_ON ?auto_123 ) ( not ( = ?auto_117 ?auto_119 ) ) ( POINTING ?auto_121 ?auto_125 ) ( not ( = ?auto_119 ?auto_125 ) ) )
    :subtasks
    ( ( !TURN_TO ?auto_121 ?auto_119 ?auto_125 )
      ( GET_IMAGE ?auto_117 ?auto_118 ) )
  )

  ( :method GET_IMAGE
    :parameters
    (
      ?auto_135 - DIRECTION
      ?auto_136 - MODE
    )
    :vars
    (
      ?auto_142 - INSTRUMENT
      ?auto_138 - SATELLITE
      ?auto_140 - DIRECTION
      ?auto_141 - DIRECTION
      ?auto_144 - SATELLITE
      ?auto_145 - DIRECTION
    )
    :precondition
    ( and ( ON_BOARD ?auto_142 ?auto_138 ) ( SUPPORTS ?auto_142 ?auto_136 ) ( POWER_ON ?auto_142 ) ( not ( = ?auto_135 ?auto_140 ) ) ( POINTING ?auto_138 ?auto_141 ) ( not ( = ?auto_140 ?auto_141 ) ) ( ON_BOARD ?auto_142 ?auto_144 ) ( CALIBRATION_TARGET ?auto_142 ?auto_145 ) ( POINTING ?auto_144 ?auto_145 ) ( NOT_CALIBRATED ?auto_142 ) )
    :subtasks
    ( ( !CALIBRATE ?auto_144 ?auto_142 ?auto_145 )
      ( GET_IMAGE ?auto_135 ?auto_136 ) )
  )

)

