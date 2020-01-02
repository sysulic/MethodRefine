( define ( domain Blocks4 )
  ( :requirements :strips :typing :equality :htn )
  ( :types block )
  ( :predicates
    ( ON-TABLE ?b - BLOCK )
    ( ON ?b1 - BLOCK ?b2 - BLOCK )
    ( CLEAR ?b - BLOCK )
    ( HAND-EMPTY )
    ( HOLDING ?b - BLOCK )
  )
  ( :action !PICKUP
    :parameters
    (
      ?b - BLOCK
    )
    :precondition
    ( and ( ON-TABLE ?b ) ( CLEAR ?b ) ( HAND-EMPTY ) )
    :effect
    ( and ( not ( ON-TABLE ?b ) ) ( not ( CLEAR ?b ) ) ( not ( HAND-EMPTY ) ) ( HOLDING ?b ) )
  )
  ( :action !PUTDOWN
    :parameters
    (
      ?b - BLOCK
    )
    :precondition
    ( and ( HOLDING ?b ) )
    :effect
    ( and ( not ( HOLDING ?b ) ) ( HAND-EMPTY ) ( ON-TABLE ?b ) ( CLEAR ?b ) )
  )
  ( :action !UNSTACK
    :parameters
    (
      ?b1 - BLOCK
      ?b2 - BLOCK
    )
    :precondition
    ( and ( ON ?b1 ?b2 ) ( CLEAR ?b1 ) ( HAND-EMPTY ) )
    :effect
    ( and ( not ( ON ?b1 ?b2 ) ) ( not ( CLEAR ?b1 ) ) ( not ( HAND-EMPTY ) ) ( CLEAR ?b2 ) ( HOLDING ?b1 ) )
  )
  ( :action !STACK
    :parameters
    (
      ?b1 - BLOCK
      ?b2 - BLOCK
    )
    :precondition
    ( and ( HOLDING ?b1 ) ( CLEAR ?b2 ) )
    :effect
    ( and ( not ( HOLDING ?b1 ) ) ( not ( CLEAR ?b2 ) ) ( HAND-EMPTY ) ( ON ?b1 ?b2 ) ( CLEAR ?b1 ) )
  )
  ( :method MAKE-ON-TABLE
    :parameters
    (
      ?goal - BLOCK
    )
    :precondition
    ( and ( ON-TABLE ?goal ) )
    :subtasks
    (  )
  )

  ( :method MAKE-ON
    :parameters
    (
      ?top - BLOCK
      ?bottom - BLOCK
    )
    :precondition
    ( and ( ON ?top ?bottom ) )
    :subtasks
    (  )
  )

  ( :method MAKE-ON
    :parameters
    (
      ?auto_2 - BLOCK
      ?auto_3 - BLOCK
    )
    :precondition
    ( and ( HOLDING ?auto_2 ) ( CLEAR ?auto_3 ) )
    :subtasks
    ( ( !STACK ?auto_2 ?auto_3 ) )
  )

  ( :method MAKE-ON
    :parameters
    (
      ?auto_6 - BLOCK
      ?auto_7 - BLOCK
    )
    :precondition
    ( and ( CLEAR ?auto_7 ) ( ON-TABLE ?auto_6 ) ( CLEAR ?auto_6 ) ( HAND-EMPTY ) )
    :subtasks
    ( ( !PICKUP ?auto_6 )
      ( MAKE-ON ?auto_6 ?auto_7 ) )
  )

  ( :method MAKE-ON-TABLE
    :parameters
    (
      ?auto_12 - BLOCK
    )
    :precondition
    ( and ( HOLDING ?auto_12 ) )
    :subtasks
    ( ( !PUTDOWN ?auto_12 ) )
  )

  ( :method MAKE-ON-TABLE
    :parameters
    (
      ?auto_14 - BLOCK
    )
    :vars
    (
      ?auto_17 - BLOCK
    )
    :precondition
    ( and ( ON ?auto_14 ?auto_17 ) ( CLEAR ?auto_14 ) ( HAND-EMPTY ) )
    :subtasks
    ( ( !UNSTACK ?auto_14 ?auto_17 )
      ( MAKE-ON-TABLE ?auto_14 ) )
  )

  ( :method MAKE-ON-TABLE
    :parameters
    (
      ?auto_18 - BLOCK
    )
    :vars
    (
      ?auto_19 - BLOCK
      ?auto_21 - BLOCK
      ?auto_22 - BLOCK
    )
    :precondition
    ( and ( ON ?auto_18 ?auto_19 ) ( CLEAR ?auto_18 ) ( HOLDING ?auto_21 ) ( CLEAR ?auto_22 ) )
    :subtasks
    ( ( !STACK ?auto_21 ?auto_22 )
      ( MAKE-ON-TABLE ?auto_18 ) )
  )

  ( :method MAKE-ON-TABLE
    :parameters
    (
      ?auto_23 - BLOCK
    )
    :vars
    (
      ?auto_26 - BLOCK
      ?auto_27 - BLOCK
      ?auto_24 - BLOCK
    )
    :precondition
    ( and ( ON ?auto_23 ?auto_26 ) ( CLEAR ?auto_23 ) ( CLEAR ?auto_27 ) ( ON-TABLE ?auto_24 ) ( CLEAR ?auto_24 ) ( HAND-EMPTY ) )
    :subtasks
    ( ( !PICKUP ?auto_24 )
      ( MAKE-ON-TABLE ?auto_23 ) )
  )

  ( :method MAKE-ON
    :parameters
    (
      ?auto_40 - BLOCK
      ?auto_41 - BLOCK
    )
    :vars
    (
      ?auto_44 - BLOCK
    )
    :precondition
    ( and ( CLEAR ?auto_41 ) ( ON-TABLE ?auto_40 ) ( CLEAR ?auto_40 ) ( HOLDING ?auto_44 ) )
    :subtasks
    ( ( !PUTDOWN ?auto_44 )
      ( MAKE-ON ?auto_40 ?auto_41 ) )
  )

  ( :method MAKE-ON
    :parameters
    (
      ?auto_45 - BLOCK
      ?auto_46 - BLOCK
    )
    :vars
    (
      ?auto_47 - BLOCK
    )
    :precondition
    ( and ( CLEAR ?auto_46 ) ( ON-TABLE ?auto_45 ) ( ON ?auto_47 ?auto_45 ) ( CLEAR ?auto_47 ) ( HAND-EMPTY ) )
    :subtasks
    ( ( !UNSTACK ?auto_47 ?auto_45 )
      ( MAKE-ON ?auto_45 ?auto_46 ) )
  )

  ( :method MAKE-ON
    :parameters
    (
      ?auto_52 - BLOCK
      ?auto_53 - BLOCK
    )
    :vars
    (
      ?auto_56 - BLOCK
      ?auto_58 - BLOCK
    )
    :precondition
    ( and ( ON-TABLE ?auto_52 ) ( ON ?auto_56 ?auto_52 ) ( CLEAR ?auto_56 ) ( HOLDING ?auto_53 ) ( CLEAR ?auto_58 ) )
    :subtasks
    ( ( !STACK ?auto_53 ?auto_58 )
      ( MAKE-ON ?auto_52 ?auto_53 ) )
  )

  ( :method MAKE-ON
    :parameters
    (
      ?auto_59 - BLOCK
      ?auto_60 - BLOCK
    )
    :vars
    (
      ?auto_62 - BLOCK
      ?auto_61 - BLOCK
    )
    :precondition
    ( and ( ON-TABLE ?auto_59 ) ( ON ?auto_62 ?auto_59 ) ( CLEAR ?auto_62 ) ( CLEAR ?auto_61 ) ( ON-TABLE ?auto_60 ) ( CLEAR ?auto_60 ) ( HAND-EMPTY ) )
    :subtasks
    ( ( !PICKUP ?auto_60 )
      ( MAKE-ON ?auto_59 ?auto_60 ) )
  )

  ( :method MAKE-ON
    :parameters
    (
      ?auto_77 - BLOCK
      ?auto_78 - BLOCK
    )
    :vars
    (
      ?auto_82 - BLOCK
    )
    :precondition
    ( and ( ON-TABLE ?auto_77 ) ( CLEAR ?auto_77 ) ( HOLDING ?auto_78 ) ( CLEAR ?auto_82 ) )
    :subtasks
    ( ( !STACK ?auto_78 ?auto_82 )
      ( MAKE-ON ?auto_77 ?auto_78 ) )
  )

  ( :method MAKE-ON
    :parameters
    (
      ?auto_149 - BLOCK
      ?auto_150 - BLOCK
    )
    :vars
    (
      ?auto_151 - BLOCK
      ?auto_154 - BLOCK
    )
    :precondition
    ( and ( ON-TABLE ?auto_149 ) ( CLEAR ?auto_149 ) ( ON-TABLE ?auto_150 ) ( CLEAR ?auto_150 ) ( CLEAR ?auto_151 ) ( ON-TABLE ?auto_154 ) ( CLEAR ?auto_154 ) ( HAND-EMPTY ) )
    :subtasks
    ( ( !PICKUP ?auto_154 )
      ( MAKE-ON ?auto_149 ?auto_150 ) )
  )

  ( :method MAKE-ON
    :parameters
    (
      ?auto_95 - BLOCK
      ?auto_96 - BLOCK
    )
    :vars
    (
      ?auto_99 - BLOCK
      ?auto_100 - BLOCK
    )
    :precondition
    ( and ( ON-TABLE ?auto_95 ) ( CLEAR ?auto_95 ) ( CLEAR ?auto_99 ) ( ON-TABLE ?auto_96 ) ( ON ?auto_100 ?auto_96 ) ( CLEAR ?auto_100 ) ( HAND-EMPTY ) )
    :subtasks
    ( ( !UNSTACK ?auto_100 ?auto_96 )
      ( MAKE-ON ?auto_95 ?auto_96 ) )
  )

  ( :method MAKE-ON
    :parameters
    (
      ?auto_103 - BLOCK
      ?auto_104 - BLOCK
    )
    :vars
    (
      ?auto_106 - BLOCK
      ?auto_108 - BLOCK
      ?auto_110 - BLOCK
    )
    :precondition
    ( and ( ON-TABLE ?auto_103 ) ( CLEAR ?auto_103 ) ( ON-TABLE ?auto_104 ) ( ON ?auto_106 ?auto_104 ) ( CLEAR ?auto_106 ) ( HOLDING ?auto_108 ) ( CLEAR ?auto_110 ) )
    :subtasks
    ( ( !STACK ?auto_108 ?auto_110 )
      ( MAKE-ON ?auto_103 ?auto_104 ) )
  )

  ( :method MAKE-ON
    :parameters
    (
      ?auto_111 - BLOCK
      ?auto_112 - BLOCK
    )
    :vars
    (
      ?auto_113 - BLOCK
      ?auto_117 - BLOCK
      ?auto_116 - BLOCK
    )
    :precondition
    ( and ( ON-TABLE ?auto_111 ) ( CLEAR ?auto_111 ) ( ON-TABLE ?auto_112 ) ( ON ?auto_113 ?auto_112 ) ( CLEAR ?auto_113 ) ( CLEAR ?auto_117 ) ( ON-TABLE ?auto_116 ) ( CLEAR ?auto_116 ) ( HAND-EMPTY ) )
    :subtasks
    ( ( !PICKUP ?auto_116 )
      ( MAKE-ON ?auto_111 ?auto_112 ) )
  )

  ( :method MAKE-ON
    :parameters
    (
      ?auto_142 - BLOCK
      ?auto_143 - BLOCK
    )
    :vars
    (
      ?auto_146 - BLOCK
      ?auto_148 - BLOCK
    )
    :precondition
    ( and ( ON-TABLE ?auto_142 ) ( CLEAR ?auto_142 ) ( ON-TABLE ?auto_143 ) ( CLEAR ?auto_143 ) ( HOLDING ?auto_146 ) ( CLEAR ?auto_148 ) )
    :subtasks
    ( ( !STACK ?auto_146 ?auto_148 )
      ( MAKE-ON ?auto_142 ?auto_143 ) )
  )

  ( :method MAKE-ON
    :parameters
    (
      ?auto_156 - BLOCK
      ?auto_157 - BLOCK
    )
    :vars
    (
      ?auto_160 - BLOCK
      ?auto_158 - BLOCK
    )
    :precondition
    ( and ( ON-TABLE ?auto_157 ) ( CLEAR ?auto_157 ) ( CLEAR ?auto_160 ) ( ON-TABLE ?auto_158 ) ( CLEAR ?auto_158 ) ( HOLDING ?auto_156 ) )
    :subtasks
    ( ( MAKE-ON-TABLE ?auto_156 )
      ( MAKE-ON ?auto_156 ?auto_157 ) )
  )

  ( :method MAKE-ON
    :parameters
    (
      ?auto_163 - BLOCK
      ?auto_164 - BLOCK
    )
    :vars
    (
      ?auto_165 - BLOCK
      ?auto_166 - BLOCK
    )
    :precondition
    ( and ( ON-TABLE ?auto_164 ) ( CLEAR ?auto_164 ) ( CLEAR ?auto_165 ) ( ON-TABLE ?auto_166 ) ( ON ?auto_163 ?auto_166 ) ( CLEAR ?auto_163 ) ( HAND-EMPTY ) )
    :subtasks
    ( ( !UNSTACK ?auto_163 ?auto_166 )
      ( MAKE-ON ?auto_163 ?auto_164 ) )
  )

  ( :method MAKE-ON
    :parameters
    (
      ?auto_171 - BLOCK
      ?auto_172 - BLOCK
    )
    :vars
    (
      ?auto_174 - BLOCK
      ?auto_173 - BLOCK
      ?auto_178 - BLOCK
    )
    :precondition
    ( and ( ON-TABLE ?auto_172 ) ( CLEAR ?auto_172 ) ( ON-TABLE ?auto_174 ) ( ON ?auto_171 ?auto_174 ) ( CLEAR ?auto_171 ) ( HOLDING ?auto_173 ) ( CLEAR ?auto_178 ) )
    :subtasks
    ( ( !STACK ?auto_173 ?auto_178 )
      ( MAKE-ON ?auto_171 ?auto_172 ) )
  )

  ( :method MAKE-ON
    :parameters
    (
      ?auto_179 - BLOCK
      ?auto_180 - BLOCK
    )
    :vars
    (
      ?auto_185 - BLOCK
      ?auto_182 - BLOCK
      ?auto_184 - BLOCK
    )
    :precondition
    ( and ( ON-TABLE ?auto_180 ) ( CLEAR ?auto_180 ) ( ON-TABLE ?auto_185 ) ( ON ?auto_179 ?auto_185 ) ( CLEAR ?auto_179 ) ( CLEAR ?auto_182 ) ( ON-TABLE ?auto_184 ) ( CLEAR ?auto_184 ) ( HAND-EMPTY ) )
    :subtasks
    ( ( !PICKUP ?auto_184 )
      ( MAKE-ON ?auto_179 ?auto_180 ) )
  )

)

