( define ( domain logistics )
  ( :requirements :strips :typing :equality :htn )
  ( :types airplane city location obj truck )
  ( :predicates
    ( obj-at ?a - obj ?b - location )
    ( truck-at ?c - truck ?d - location )
    ( airplane-at ?e - airplane ?f - location )
    ( in-truck ?g - obj ?h - truck )
    ( in-airplane ?i - obj ?j - airplane )
    ( in-city ?k - location ?l - city )
    ( airport ?o - location )
  )

  ( :action !LOAD-TRUCK
    :parameters
    (
      ?obj - obj
      ?truck - truck
      ?loc - location
    )
    :precondition
    ( and
      ( truck-at ?truck ?loc )
      ( obj-at ?obj ?loc )
    )
    :effect
    ( and
      ( not ( obj-at ?obj ?loc ) )
      ( in-truck ?obj ?truck )
    )
  )

  ( :action !LOAD-AIRPLANE
    :parameters
    (
      ?obj - obj
      ?airplane - airplane
      ?loc - location
    )
    :precondition
    ( and
      ( obj-at ?obj ?loc )
      ( airplane-at ?airplane ?loc )
    )
    :effect
    ( and
      ( not ( obj-at ?obj ?loc ) )
      ( in-airplane ?obj ?airplane )
    )
  )

  ( :action !UNLOAD-TRUCK
    :parameters
    (
      ?obj - obj
      ?truck - truck
      ?loc - location
    )
    :precondition
    ( and
      ( truck-at ?truck ?loc )
      ( in-truck ?obj ?truck )
    )
    :effect
    ( and
      ( not ( in-truck ?obj ?truck ) )
      ( obj-at ?obj ?loc )
    )
  )

  ( :action !UNLOAD-AIRPLANE
    :parameters
    (
      ?obj - obj
      ?airplane - airplane
      ?loc - location
    )
    :precondition
    ( and
      ( in-airplane ?obj ?airplane )
      ( airplane-at ?airplane ?loc )
    )
    :effect
    ( and
      ( not ( in-airplane ?obj ?airplane ) )
      ( obj-at ?obj ?loc ) )
  )

  ( :action !DRIVE-TRUCK
    :parameters
    (
      ?truck - truck
      ?loc-from - location
      ?loc-to - location
      ?city - city
    )
    :precondition
    ( and
      ( truck-at ?truck ?loc-from )
      ( in-city ?loc-from ?city )
      ( in-city ?loc-to ?city )
      ( not ( = ?loc-from ?loc-to ) )
    )
    :effect
    ( and
      ( not ( truck-at ?truck ?loc-from ) )
      ( truck-at ?truck ?loc-to )
    )
  )

  ( :action !FLY-AIRPLANE
    :parameters
    (
      ?airplane - airplane
      ?loc-from - location
      ?loc-to - location
    )
    :precondition
    ( and
      ( airport ?loc-from )
      ( airport ?loc-to )
      ( airplane-at ?airplane ?loc-from )
      ( not ( = ?loc-from ?loc-to ) )
    )
    :effect
    ( and
      ( not ( airplane-at ?airplane ?loc-from ) )
      ( airplane-at ?airplane ?loc-to )
    )
  )

  ( :method DELIVER-PKG
    :parameters ( ?obj - obj ?dst - location )
    :precondition
    ( and
      ( obj-at ?obj ?dst )
    )
    :subtasks
    (
    )
  )

  ( :method DELIVER-PKG
    :parameters ( ?obj - obj ?dst - location )
    :vars ( ?truck - truck )
    :precondition
    ( and
      ( truck-at ?truck ?dst )
      ( in-truck ?obj ?truck )
    )
    :subtasks
    (
      ( !UNLOAD-TRUCK ?obj ?truck ?dst )
    )
  )

  ( :method DELIVER-PKG
    :parameters ( ?obj - obj ?dst - location )
    :vars ( ?truck - truck ?src - location ?city - city )
    :precondition
    ( and
      ( not ( = ?src ?dst ) )
      ( truck-at ?truck ?src )
      ( in-truck ?obj ?truck )
      ( in-city ?src ?city )
      ( in-city ?dst ?city )
    )
    :subtasks
    (
      ( !DRIVE-TRUCK ?truck ?src ?dst ?city )
      ( DELIVER-PKG ?obj ?dst )
    )
  )

  ( :method DELIVER-PKG
    :parameters (  ?obj - obj ?dst - location )
    :vars ( ?src - location ?city - city ?truck - truck )
    :precondition
    ( and
      ( obj-at ?obj ?src )
      ( not ( = ?dst ?src ) )
      ( in-city ?src ?city )
      ( in-city ?dst ?city )
      ( truck-at ?truck ?src )
    )
    :subtasks
    (
      ( !LOAD-TRUCK ?obj ?truck ?src )
      ( DELIVER-PKG ?obj ?dst )
    )
  )

  ( :method DELIVER-PKG
    :parameters ( ?obj - obj ?dst - location )
    :vars ( ?src - location ?city - city ?garage - location ?truck - truck )
    :precondition
    ( and
      ( obj-at ?obj ?src )
      ( not ( = ?src ?dst ) )
      ( in-city ?src ?city )
      ( in-city ?dst ?city )
      ( in-city ?garage ?city )
      ( not ( = ?garage ?src ) )
      ( truck-at ?truck ?garage )
    )
    :subtasks
    (
      ( !DRIVE-TRUCK ?truck ?garage ?src ?city )
      ( DELIVER-PKG ?obj ?dst )
    )
  )

  ( :method DELIVER-PKG
    :parameters ( ?obj - obj ?dst - location )
    :vars ( ?plane - airplane )
    :precondition
    ( and
      ( airplane-at ?plane ?dst )
      ( in-airplane ?obj ?plane )
    )
    :subtasks
    (
      ( !UNLOAD-AIRPLANE ?obj ?plane ?dst )
    )
  )

  ( :method DELIVER-PKG
    :parameters ( ?obj - obj ?dst - location )
    :vars ( ?src - location ?plane - airplane )
    :precondition
    ( and
      ( airport ?dst )
      ( airport ?src )
      ( not ( = ?src ?dst ) )
      ( airplane-at ?plane ?src )
      ( in-airplane ?obj ?plane )
    )
    :subtasks
    (
      ( !FLY-AIRPLANE ?plane ?src ?dst )
      ( DELIVER-PKG ?obj ?dst )
    )
  )

  ( :method DELIVER-PKG
    :parameters ( ?obj - obj ?dst - location )
    :vars ( ?src - location ?plane - airplane )
    :precondition
    ( and
      ( airport ?dst )
      ( airport ?src )
      ( not ( = ?src ?dst ) )
      ( airplane-at ?plane ?src )
      ( obj-at ?obj ?src )
    )
    :subtasks
    (
      ( !LOAD-AIRPLANE ?obj ?plane ?src )
      ( DELIVER-PKG ?obj ?dst )
    )
  )

  ( :method DELIVER-PKG
    :parameters ( ?obj - obj ?dst - location )
    :vars ( ?src - location ?hangar - location ?plane - airplane )
    :precondition
    ( and
      ( airport ?dst )
      ( airport ?src )
      ( not ( = ?src ?dst ) )
      ( airport ?hangar )
      ( not ( = ?src ?hangar ) )
      ( airplane-at ?plane ?hangar )
      ( obj-at ?obj ?src )
    )
    :subtasks
    (
      ( !FLY-AIRPLANE ?plane ?hangar ?src )
      ( DELIVER-PKG ?obj ?dst )
    )
  )

  ( :method DELIVER-PKG
    :parameters ( ?obj - obj ?dst - location )
    :vars ( ?src - location ?dst_port - location ?dst_city - city )
    :precondition
    ( and
      ( obj-at ?obj ?src )
      ( airport ?dst_port )
      ( airport ?src )
      ( in-city ?dst ?dst_city )
      ( in-city ?dst_port ?dst_city )
      ( not ( = ?dst ?src ) )
      ( not ( = ?src ?dst_port ) )
    )
    :subtasks
    (
      ( DELIVER-PKG ?obj ?dst_port )
      ( DELIVER-PKG ?obj ?dst )
    )
  )

  ( :method DELIVER-PKG
    :parameters ( ?obj - obj ?dst - location )
    :vars ( ?src - location ?dst_port - location ?src_port - location ?dst_city - city ?src_city - city )
    :precondition
    ( and
      ( obj-at ?obj ?src )
      ( airport ?dst_port )
      ( airport ?src_port )
      ( in-city ?dst ?dst_city )
      ( in-city ?dst_port ?dst_city )
      ( in-city ?src ?src_city )
      ( in-city ?src_port ?src_city )
      ( not ( = ?src ?dst ) )
      ( not ( = ?src_port ?dst_port ) )
      ( not ( = ?src ?src_port ) )
    )
    :subtasks
    (
      ( DELIVER-PKG ?obj ?src_port )
      ( DELIVER-PKG ?obj ?dst )
    )
  )

)

