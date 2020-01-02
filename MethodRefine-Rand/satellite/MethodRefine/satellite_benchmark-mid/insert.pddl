(define (problem satellite-4-0)
(:domain satellite)
(:objects
 sate-1 sate-2 sate-3 - satellite
 mode-1 mode-2 mode-3 - mode
 direc-1 direc-2 direc-3 direc-4 direc-5 - direction
inst-1-1 inst-1-2 inst-3-3 inst-3-2 inst-3-1 inst-3-4 inst-2-2 inst-2-3 inst-3-5 inst-2-1 - instrument)

(:init (on_board inst-1-1 sate-1) (on_board inst-1-2 sate-1) (on_board inst-3-3 sate-3) (on_board inst-3-2 sate-3) (on_board inst-3-1 sate-3) (on_board inst-3-4 sate-3) (on_board inst-2-2 sate-2) (on_board inst-2-3 sate-2) (on_board inst-3-5 sate-3) (on_board inst-2-1 sate-2) (pointing sate-1 direc-4) (pointing sate-2 direc-5) (pointing sate-3 direc-2) (power_avail sate-1) (power_avail sate-2) (is_mode inst-1-1 mode-2) (is_mode inst-1-2 mode-1) (is_mode inst-3-3 mode-1) (is_mode inst-3-2 mode-1) (is_mode inst-3-1 mode-2) (is_mode inst-3-4 mode-3) (is_mode inst-2-2 mode-3) (is_mode inst-2-3 mode-2) (is_mode inst-3-5 mode-1) (is_mode inst-2-1 mode-3) (calibrate inst-3-5) (calib_target inst-1-1 direc-4) (calib_target inst-1-2 direc-1) (calib_target inst-3-3 direc-2) (calib_target inst-3-2 direc-3) (calib_target inst-3-1 direc-1) (calib_target inst-3-4 direc-4) (calib_target inst-2-2 direc-4) (calib_target inst-2-3 direc-2) (calib_target inst-3-5 direc-2) (calib_target inst-2-1 direc-5) (power_on inst-3-5) )

(:goal (and (calibrate inst-3-5) (on_board inst-3-5 sate-3) (is_mode inst-3-5 mode-1) (power_on inst-3-5) (pointing sate-3 direc-3)))
)