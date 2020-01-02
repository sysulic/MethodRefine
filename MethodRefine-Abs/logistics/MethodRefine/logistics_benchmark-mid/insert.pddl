(define (problem logistics-4-0)
(:domain logistics)
(:objects
 plane1 - airplane
 loc11 loc21 loc31 loc41 loc51 - airport
 loc12 loc22 loc32 loc42 loc52 - location
 city2 city1 city3 city4 city5 - city
 truck2 truck1 truck3 truck4 truck5 - truck
 pkg1 pkg2 pkg3 pkg4 pkg5 pkg6 - package)

(:init (at truck5 loc51) (at truck4 loc41) (at truck1 loc11) (at plane1 loc11) (at truck3 loc31) (at truck2 loc22) (at pkg1 loc31)(at pkg2 loc22)(at pkg3 loc11)(in pkg4 plane1)(in-city loc11 city1) (in-city loc12 city1) (in-city loc21 city2) (in-city loc22 city2) (in-city loc31 city3) (in-city loc32 city3) (in-city loc41 city4) (in-city loc42 city4) (in-city loc51 city5) (in-city loc52 city5) )

(:goal (and (in pkg4 plane1)(at plane1 loc41)))
)