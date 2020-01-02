( define ( problem probname )
	( :domain logistics )
	( :requirements :strips :typing :equality )
	( :objects
		a1 - airplane
		c1 - city
		t1 - truck
		l11 - location
		l12 - location
		c2 - city
		t2 - truck
		l21 - location
		l22 - location
		c3 - city
		t3 - truck
		l31 - location
		l32 - location
		c4 - city
		t4 - truck
		l41 - location
		l42 - location
		c5 - city
		t5 - truck
		l51 - location
		l52 - location
		p1 - obj
		p2 - obj
		p3 - obj
	)

	( :init
		(airport l11)
		(in-city l11 c1)
		(in-city l12 c1)
		(airport l21)
		(in-city l21 c2)
		(in-city l22 c2)
		(airport l31)
		(in-city l31 c3)
		(in-city l32 c3)
		(airport l41)
		(in-city l41 c4)
		(in-city l42 c4)
		(airport l51)
		(in-city l51 c5)
		(in-city l52 c5)
		(truck-at t1 l12)
		(truck-at t2 l22)
		(truck-at t3 l32)
		(truck-at t4 l41)
		(truck-at t5 l51)
		(airplane-at a1 l41)
		(obj-at p1 l32)
		(obj-at p2 l31)
		(obj-at p3 l51)
	)

	( :goal
		( and
			(obj-at p1 l42)
			(obj-at p2 l52)
			(obj-at p3 l42)
		)
	)
)