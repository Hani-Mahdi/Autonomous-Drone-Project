"""
Docstring for fsm.context

Stores States and data that will not reset everytick
"""
class FSMContext():
    pass

# class StateTimer():
#     def __init__(self):
#         self.start_time = None
#         self.end_time = None

context = FSMContext()

#States
context.top_state = None
context.flight_sub_state = None
context.drop_off_sub_state = None

#Mission Info 

context.mission_start_time = None
context.mission_end_time = None
context.mission_status = None
context.prev_altitudes = []

#State Specific Info

#Take off
context.takeoff_start_time = None
context.takeoff_end_time = None

#Flight
context.flight_start_time = None
context.flight_end_time = None

#Flight - Search
context.search_start_time = None
context.search_end_time = None
context.target = None

#Flight - To target
context.to_target_start_time = None
context.to_target_end_time = None

#Flight - Drop off
context.drop_off_start_time = None
context.drop_off_end_time = None

#Flight - Drop off - Descent
context.descent_start_time = None
context.descent_end_time = None

#Flight - Drop off - Release
context.release_start_time = None
context.release_end_time = None

#Flight - Drop off - Ascent
context.ascent_start_time = None
context.ascent_end_time = None