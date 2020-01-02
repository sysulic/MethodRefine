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

)

