( define ( domain logistics )
  ( :requirements :strips :typing :equality :htn )
  ( :types airplane city location obj truck )
  ( :predicates
    ( OBJ-AT ?a - OBJ ?b - LOCATION )
    ( TRUCK-AT ?c - TRUCK ?d - LOCATION )
    ( AIRPLANE-AT ?e - AIRPLANE ?f - LOCATION )
    ( IN-TRUCK ?g - OBJ ?h - TRUCK )
    ( IN-AIRPLANE ?i - OBJ ?j - AIRPLANE )
    ( IN-CITY ?k - LOCATION ?l - CITY )
    ( AIRPORT ?o - LOCATION )
  )
  ( :action !LOAD-TRUCK
    :parameters
    (
      ?obj - OBJ
      ?truck - TRUCK
      ?loc - LOCATION
    )
    :precondition
    ( and ( TRUCK-AT ?truck ?loc ) ( OBJ-AT ?obj ?loc ) )
    :effect
    ( and ( not ( OBJ-AT ?obj ?loc ) ) ( IN-TRUCK ?obj ?truck ) )
  )
  ( :action !LOAD-AIRPLANE
    :parameters
    (
      ?obj - OBJ
      ?airplane - AIRPLANE
      ?loc - LOCATION
    )
    :precondition
    ( and ( OBJ-AT ?obj ?loc ) ( AIRPLANE-AT ?airplane ?loc ) )
    :effect
    ( and ( not ( OBJ-AT ?obj ?loc ) ) ( IN-AIRPLANE ?obj ?airplane ) )
  )
  ( :action !UNLOAD-TRUCK
    :parameters
    (
      ?obj - OBJ
      ?truck - TRUCK
      ?loc - LOCATION
    )
    :precondition
    ( and ( TRUCK-AT ?truck ?loc ) ( IN-TRUCK ?obj ?truck ) )
    :effect
    ( and ( not ( IN-TRUCK ?obj ?truck ) ) ( OBJ-AT ?obj ?loc ) )
  )
  ( :action !UNLOAD-AIRPLANE
    :parameters
    (
      ?obj - OBJ
      ?airplane - AIRPLANE
      ?loc - LOCATION
    )
    :precondition
    ( and ( IN-AIRPLANE ?obj ?airplane ) ( AIRPLANE-AT ?airplane ?loc ) )
    :effect
    ( and ( not ( IN-AIRPLANE ?obj ?airplane ) ) ( OBJ-AT ?obj ?loc ) )
  )
  ( :action !DRIVE-TRUCK
    :parameters
    (
      ?truck - TRUCK
      ?loc-from - LOCATION
      ?loc-to - LOCATION
      ?city - CITY
    )
    :precondition
    ( and ( TRUCK-AT ?truck ?loc-from ) ( IN-CITY ?loc-from ?city ) ( IN-CITY ?loc-to ?city ) ( not ( = ?loc-from ?loc-to ) ) )
    :effect
    ( and ( not ( TRUCK-AT ?truck ?loc-from ) ) ( TRUCK-AT ?truck ?loc-to ) )
  )
  ( :action !FLY-AIRPLANE
    :parameters
    (
      ?airplane - AIRPLANE
      ?loc-from - LOCATION
      ?loc-to - LOCATION
    )
    :precondition
    ( and ( AIRPORT ?loc-from ) ( AIRPORT ?loc-to ) ( AIRPLANE-AT ?airplane ?loc-from ) ( not ( = ?loc-from ?loc-to ) ) )
    :effect
    ( and ( not ( AIRPLANE-AT ?airplane ?loc-from ) ) ( AIRPLANE-AT ?airplane ?loc-to ) )
  )
  ( :method DELIVER-PKG
    :parameters
    (
      ?obj - OBJ
      ?dst - LOCATION
    )
    :precondition
    ( and ( OBJ-AT ?obj ?dst ) )
    :subtasks
    (  )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_2 - OBJ
      ?auto_3 - LOCATION
    )
    :vars
    (
      ?auto_6 - AIRPLANE
    )
    :precondition
    ( and ( IN-AIRPLANE ?auto_2 ?auto_6 ) ( AIRPLANE-AT ?auto_6 ?auto_3 ) )
    :subtasks
    ( ( !UNLOAD-AIRPLANE ?auto_2 ?auto_6 ?auto_3 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_7 - OBJ
      ?auto_8 - LOCATION
    )
    :vars
    (
      ?auto_11 - AIRPLANE
      ?auto_13 - LOCATION
    )
    :precondition
    ( and ( IN-AIRPLANE ?auto_7 ?auto_11 ) ( AIRPORT ?auto_13 ) ( AIRPORT ?auto_8 ) ( AIRPLANE-AT ?auto_11 ?auto_13 ) ( not ( = ?auto_13 ?auto_8 ) ) )
    :subtasks
    ( ( !FLY-AIRPLANE ?auto_11 ?auto_13 ?auto_8 )
      ( DELIVER-PKG ?auto_7 ?auto_8 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_15 - OBJ
      ?auto_16 - LOCATION
    )
    :vars
    (
      ?auto_20 - LOCATION
      ?auto_19 - AIRPLANE
      ?auto_21 - LOCATION
    )
    :precondition
    ( and ( AIRPORT ?auto_20 ) ( AIRPORT ?auto_16 ) ( AIRPLANE-AT ?auto_19 ?auto_20 ) ( not ( = ?auto_20 ?auto_16 ) ) ( OBJ-AT ?auto_15 ?auto_21 ) ( AIRPLANE-AT ?auto_19 ?auto_21 ) )
    :subtasks
    ( ( !LOAD-AIRPLANE ?auto_15 ?auto_19 ?auto_21 )
      ( DELIVER-PKG ?auto_15 ?auto_16 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_24 - OBJ
      ?auto_25 - LOCATION
    )
    :vars
    (
      ?auto_28 - LOCATION
      ?auto_32 - LOCATION
      ?auto_27 - AIRPLANE
    )
    :precondition
    ( and ( AIRPORT ?auto_28 ) ( AIRPORT ?auto_25 ) ( not ( = ?auto_28 ?auto_25 ) ) ( OBJ-AT ?auto_24 ?auto_28 ) ( AIRPORT ?auto_32 ) ( AIRPLANE-AT ?auto_27 ?auto_32 ) ( not ( = ?auto_32 ?auto_28 ) ) )
    :subtasks
    ( ( !FLY-AIRPLANE ?auto_27 ?auto_32 ?auto_28 )
      ( DELIVER-PKG ?auto_24 ?auto_25 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_36 - OBJ
      ?auto_37 - LOCATION
    )
    :vars
    (
      ?auto_38 - TRUCK
    )
    :precondition
    ( and ( TRUCK-AT ?auto_38 ?auto_37 ) ( IN-TRUCK ?auto_36 ?auto_38 ) )
    :subtasks
    ( ( !UNLOAD-TRUCK ?auto_36 ?auto_38 ?auto_37 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_41 - OBJ
      ?auto_42 - LOCATION
    )
    :vars
    (
      ?auto_44 - TRUCK
      ?auto_47 - LOCATION
      ?auto_48 - CITY
    )
    :precondition
    ( and ( IN-TRUCK ?auto_41 ?auto_44 ) ( TRUCK-AT ?auto_44 ?auto_47 ) ( IN-CITY ?auto_47 ?auto_48 ) ( IN-CITY ?auto_42 ?auto_48 ) ( not ( = ?auto_42 ?auto_47 ) ) )
    :subtasks
    ( ( !DRIVE-TRUCK ?auto_44 ?auto_47 ?auto_42 ?auto_48 )
      ( DELIVER-PKG ?auto_41 ?auto_42 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_50 - OBJ
      ?auto_51 - LOCATION
    )
    :vars
    (
      ?auto_54 - TRUCK
      ?auto_55 - LOCATION
      ?auto_56 - CITY
      ?auto_58 - LOCATION
    )
    :precondition
    ( and ( TRUCK-AT ?auto_54 ?auto_55 ) ( IN-CITY ?auto_55 ?auto_56 ) ( IN-CITY ?auto_51 ?auto_56 ) ( not ( = ?auto_51 ?auto_55 ) ) ( TRUCK-AT ?auto_54 ?auto_58 ) ( OBJ-AT ?auto_50 ?auto_58 ) )
    :subtasks
    ( ( !LOAD-TRUCK ?auto_50 ?auto_54 ?auto_58 )
      ( DELIVER-PKG ?auto_50 ?auto_51 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_60 - OBJ
      ?auto_61 - LOCATION
    )
    :vars
    (
      ?auto_65 - TRUCK
      ?auto_66 - LOCATION
      ?auto_64 - CITY
      ?auto_63 - LOCATION
      ?auto_70 - AIRPLANE
    )
    :precondition
    ( and ( TRUCK-AT ?auto_65 ?auto_66 ) ( IN-CITY ?auto_66 ?auto_64 ) ( IN-CITY ?auto_61 ?auto_64 ) ( not ( = ?auto_61 ?auto_66 ) ) ( TRUCK-AT ?auto_65 ?auto_63 ) ( IN-AIRPLANE ?auto_60 ?auto_70 ) ( AIRPLANE-AT ?auto_70 ?auto_63 ) )
    :subtasks
    ( ( DELIVER-PKG ?auto_60 ?auto_63 )
      ( DELIVER-PKG ?auto_60 ?auto_61 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_71 - OBJ
      ?auto_72 - LOCATION
    )
    :vars
    (
      ?auto_75 - TRUCK
      ?auto_78 - LOCATION
      ?auto_77 - CITY
      ?auto_76 - LOCATION
      ?auto_79 - AIRPLANE
      ?auto_81 - LOCATION
    )
    :precondition
    ( and ( TRUCK-AT ?auto_75 ?auto_78 ) ( IN-CITY ?auto_78 ?auto_77 ) ( IN-CITY ?auto_72 ?auto_77 ) ( not ( = ?auto_72 ?auto_78 ) ) ( TRUCK-AT ?auto_75 ?auto_76 ) ( IN-AIRPLANE ?auto_71 ?auto_79 ) ( AIRPORT ?auto_81 ) ( AIRPORT ?auto_76 ) ( AIRPLANE-AT ?auto_79 ?auto_81 ) ( not ( = ?auto_81 ?auto_76 ) ) )
    :subtasks
    ( ( !FLY-AIRPLANE ?auto_79 ?auto_81 ?auto_76 )
      ( DELIVER-PKG ?auto_71 ?auto_72 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_83 - OBJ
      ?auto_84 - LOCATION
    )
    :vars
    (
      ?auto_90 - TRUCK
      ?auto_88 - LOCATION
      ?auto_87 - CITY
      ?auto_89 - LOCATION
      ?auto_92 - LOCATION
      ?auto_91 - AIRPLANE
      ?auto_93 - LOCATION
    )
    :precondition
    ( and ( TRUCK-AT ?auto_90 ?auto_88 ) ( IN-CITY ?auto_88 ?auto_87 ) ( IN-CITY ?auto_84 ?auto_87 ) ( not ( = ?auto_84 ?auto_88 ) ) ( TRUCK-AT ?auto_90 ?auto_89 ) ( AIRPORT ?auto_92 ) ( AIRPORT ?auto_89 ) ( AIRPLANE-AT ?auto_91 ?auto_92 ) ( not ( = ?auto_92 ?auto_89 ) ) ( OBJ-AT ?auto_83 ?auto_93 ) ( AIRPLANE-AT ?auto_91 ?auto_93 ) )
    :subtasks
    ( ( !LOAD-AIRPLANE ?auto_83 ?auto_91 ?auto_93 )
      ( DELIVER-PKG ?auto_83 ?auto_84 ) )
  )

  ( :method DELIVER-PKG
    :parameters
    (
      ?auto_96 - OBJ
      ?auto_97 - LOCATION
    )
    :vars
    (
      ?auto_103 - TRUCK
      ?auto_106 - LOCATION
      ?auto_101 - CITY
      ?auto_104 - LOCATION
      ?auto_105 - LOCATION
      ?auto_108 - LOCATION
      ?auto_99 - AIRPLANE
    )
    :precondition
    ( and ( TRUCK-AT ?auto_103 ?auto_106 ) ( IN-CITY ?auto_106 ?auto_101 ) ( IN-CITY ?auto_97 ?auto_101 ) ( not ( = ?auto_97 ?auto_106 ) ) ( TRUCK-AT ?auto_103 ?auto_104 ) ( AIRPORT ?auto_105 ) ( AIRPORT ?auto_104 ) ( not ( = ?auto_105 ?auto_104 ) ) ( OBJ-AT ?auto_96 ?auto_105 ) ( AIRPORT ?auto_108 ) ( AIRPLANE-AT ?auto_99 ?auto_108 ) ( not ( = ?auto_108 ?auto_105 ) ) )
    :subtasks
    ( ( !FLY-AIRPLANE ?auto_99 ?auto_108 ?auto_105 )
      ( DELIVER-PKG ?auto_96 ?auto_97 ) )
  )

)

