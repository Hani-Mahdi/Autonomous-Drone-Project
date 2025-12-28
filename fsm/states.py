'''
Docstring for fsm.states

States = 

- diagnostics
- Takeoff
- Flight
 - Search & Detect
 - To Target
 - Drop Off
    - Descent
    - Release
    - Ascent
- Landing
- Emergency Landing


-----------------------------------------------------------------------------------------------------------------
Function: Diagnostics
Input: Battery Percentage, Camera Health, Payload Gate Check, sensor health, Motor Check

Execute: 
- Read battery percentage
- Check camera output
- Open and close payload gate to test
- Check how many sensors are picking up signal
- Quickly turn on and off motors (good speed but not fast enough to fly)

Output: {
    battery_p: [xx%, "Battery Healthy"],
    camera_health: [Bool, "Camera Operational"],
    payload-gate: [Bool, "Payload Gate: (Operational or review required) "],
    sensor_health: [Bool, "Sensors working: x/2"]
}
-----------------------------------------------------------------------------------------------------------------
Function: Takeoff
Input: Battery Percentage, altitude, take_off_start, current_time, prev5_alts

Execute:

- Activate thrust and altitude control controllers (with altitude x)
- check altitude
- is altitude the same as past few checks and = x
    - yes: state -> Flight
        break

abort if alt wasnt reached within threshold (current_time - take_off_start > threshold)
     
Output: {
    status: "Complete" | "In progress" | "Abort"
    issue : "none" | "speed issue" | "Cant reach alt" | "cant hold alt"
}
-----------------------------------------------------------------------------------------------------------------
Function: Flight
Input: Battery Percentage, altitude, flight_start_time, current_time, target, cur_loc, targ_loc

Execute:

if !target and (current_time - flight_start_time > threshold)
    - status = Complete
    - state -> Landing

Output: {
    status = "Complete" | "Running" | "Abort"

}
-----------------------------------------------------------------------------------------------------------------
Function: Search & Detect
'''
