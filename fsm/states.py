"""
Docstring for fsm.states

States =

- Diagnostics
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
Input: Battery Percentage, Camera Health, Payload Gate Check, Sensor Health, Motor Check

Execute:
- Read battery percentage
- Check camera output
- Open and close payload gate to test
- Check how many sensors are picking up signal
- Quickly turn motors on/off (spin-up check, non-flight speed)

Output: {
    battery_p: [xx%, "Battery Healthy"],
    camera_health: [Bool, "Camera Operational"],
    payload_gate: [Bool, "Payload Gate Operational"],
    sensor_health: [Bool, "Sensors working x/2"],
    motors: [Bool, "Motors Responsive"]
}


-----------------------------------------------------------------------------------------------------------------
Function: Takeoff
Input: Battery Percentage, altitude, takeoff_start_time, current_time, prev5_alts

Execute:
- Activate thrust controller
- Activate altitude controller (target = TAKEOFF_ALT)
- Check altitude stability using prev5_alts
- If altitude == TAKEOFF_ALT and stable:
    - state -> Flight
- If (current_time - takeoff_start_time) > threshold:
    - state -> Emergency Landing

Output: {
    status: "Complete" | "In Progress" | "Abort",
    issue: "None" | "Speed Issue" | "Cannot Reach Altitude" | "Cannot Hold Altitude"
}


-----------------------------------------------------------------------------------------------------------------
Function: Flight
Input: Battery Percentage, altitude, flight_start_time, current_time

Execute:
- If no active target AND (current_time - flight_start_time) > threshold:
    - state -> Landing
- Otherwise:
    - remain in Flight
    - delegate control to active Flight sub-state

Output: {
    status: "Running" | "Complete" | "Abort"
}


-----------------------------------------------------------------------------------------------------------------
Function: Search & Detect
Input: Battery Percentage, altitude, search_start_time, current_time, target

Execute:
- Activate position stabilizers
- Activate search algorithm
- If target detected:
    - state -> To Target
- If (current_time - search_start_time) > threshold:
    - state -> Flight

Output: {
    status: "Searching" | "Target Found" | "Abort"
}


-----------------------------------------------------------------------------------------------------------------
Function: To Target
Input: Battery Percentage, altitude, cur_loc, targ_loc

Execute:
- Activate navigation controller toward targ_loc
- If distance(cur_loc, targ_loc) <= tolerance:
    - state -> Drop Off -> Descent
- If target lost:
    - state -> Search & Detect

Output: {
    status: "Navigating" | "Reached Target" | "Target Lost" | "Abort"
}


-----------------------------------------------------------------------------------------------------------------
Function: Drop Off - Descent
Input: Battery Percentage, altitude, descent_start_time, current_time

Execute:
- Activate altitude controller (target = DROP_ALT)
- If altitude stable at DROP_ALT:
    - state -> Release
- If (current_time - descent_start_time) > threshold:
    - state -> Emergency Landing

Output: {
    status: "Descending" | "At Drop Altitude" | "Abort"
}


-----------------------------------------------------------------------------------------------------------------
Function: Drop Off - Release
Input: Payload Gate Status, release_start_time, current_time

Execute:
- Activate payload gate
- If payload released:
    - state -> Ascent
- If (current_time - release_start_time) > threshold:
    - state -> Emergency Landing

Output: {
    status: "Releasing" | "Released" | "Abort"
}


-----------------------------------------------------------------------------------------------------------------
Function: Drop Off - Ascent
Input: Battery Percentage, altitude

Execute:
- Activate altitude controller (target = TAKEOFF_ALT)
- If altitude stable:
    - state -> Search & Detect

Output: {
    status: "Ascending" | "Recovered" | "Abort"
}


-----------------------------------------------------------------------------------------------------------------
Function: Landing
Input: Battery Percentage, altitude

Execute:
- Activate landing controller (target = GROUND_ALT)
- If altitude == ground AND motors disarmed:
    - state -> Complete

Output: {
    status: "Landing" | "Complete" | "Abort"
}


-----------------------------------------------------------------------------------------------------------------
Function: Emergency Landing
Input: Battery Percentage, altitude

Execute:
- Override all active states
- Activate emergency landing controller
- Reduce altitude aggressively but safely
- If on ground:
    - motors off
    - state -> Complete

Output: {
    status: "Emergency Landing" | "Complete"
}
"""