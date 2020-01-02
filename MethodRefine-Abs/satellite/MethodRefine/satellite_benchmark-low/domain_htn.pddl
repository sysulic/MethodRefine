(define ( domain satellite)
  (:requirements :strips :typing :equality)
  (:types direction 
	        instrument 
          mode 
          satellite)
  (:predicates (on_board ?i - instrument ?s - satellite)
    	         (pointing ?s - satellite ?d - direction)
    	         (power_avail ?s - satellite)
    	         (power_on ?i - instrument)
    	         (calibrate ?i - instrument)
    	         (have_img ?d - direction ?m - mode)
	             (is_mode ?i - instrument ?m - mode)
               (calib_target ?i - instrument ?d - direction))

  (:action TURN-TO
     :parameters (?s - satellite ?d_new - direction ?d_prev - direction)
     :precondition (and (not (= ?d_new ?d_prev)) (pointing ?s ?d_prev))
     :effect (and (pointing ?s ?d_new) (not (pointing ?s ?d_prev)))
  )

  (:action SWITCH-ON
     :parameters (?i - instrument ?s - satellite)
     :precondition (and (on_board ?i ?s) (power_avail ?s))
     :effect (and (power_on ?i) (not (calibrate ?i)) (not (power_avail ?s)))
  )

  (:action SWITCH-OFF
     :parameters (?i - instrument ?s - satellite)
     :precondition (and (on_board ?i ?s))
     :effect (and (power_avail ?s) (not (power_on ?i)))
  )

  (:action CALIBRATE
     :parameters (?i - instrument ?s - satellite ?d - direction)
     :precondition (and (on_board ?i ?s) (calib_target ?i ?d) (pointing ?s ?d) (power_on ?i) (not (calibrate ?i)))
     :effect (and (calibrate ?i))
  )

  (:action TAKE-IMAGE
     :parameters (?s - satellite ?d - direction ?i - instrument ?m - mode)
     :precondition (and (calibrate ?i) (on_board ?i ?s) (is_mode ?i ?m) (power_on ?i) (pointing ?s ?d))
     :effect (and (have_img ?d ?m))
  )
)
