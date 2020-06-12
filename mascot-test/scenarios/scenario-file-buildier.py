import random
import json
from trace_representation import *

def to_assertion(scenarioName, trace):
    """ Converts a Trace object into an assertion and writes it to a file """

    assert_start = "assert MASCOT_SAFETY_SYSTEM  :[has trace]: <"
    assert_end = ">"

    assert_check = assert_start
    trace_list = trace.to_list()
    print "trace_list", trace_list

    for i in range(len(trace_list)):
    # the str is key here. My editor produced unicode which became
    # a unicode object, not a str object so the assertion parsing broke.
        event = str(trace_list[i])
        print "event", event
        print "event type" , type(event)
        assert_check = assert_check + event
        if i < len(trace_list)-1:
            assert_check = assert_check + ", "
        elif i == len(trace_list)-1:
            assert_check = assert_check + assert_end

    f = open(scenarioName+"-assertion.csp", "w")

    f.write(assert_check)
    f.close()

def _split_and_convert_event(eventStr):
    """Takes an event string, splits it on the : and converts the event from
    system to model"""

    print(eventStr)
    eventList = eventStr.split(":")

    system_event = eventList[0]
    #This gets rid of the extra quotes around the event name
    system_event = system_event.strip("\"")
    print(system_event)
    print(type(system_event))
    fdr_event =  str(eventMap[str(system_event)])

    param = eventList[1]

    return fdr_event, param


def build_scenario_0(traceLength):
    """Builds a stress-test trace out of just speed 100 or 500 events.
    Trace is traceLength long """

    velocity_events = ['"velocity":100', '"velocity":500']

    trace = Trace(Event("system_init"))

    f = open("scenario0-"+str(traceLength)+"-stress.json", "w")

    footswitch_bool = False
    velocity_num = 0


#traceLength/10 because each of these loops produces 10 events (+ system_init for the csp file)
    for i in range(0,traceLength/10):
#This loop produces 10 events in the trace
#Both in the json file and in the csp file.
        footswitch_bool = not footswitch_bool
        footswitch = footswitch_events[footswitch_bool]

        fsEvent, fsParam = _split_and_convert_event(footswitch_events[footswitch_bool])
        newFSEvent = Event(fsEvent, fsParam)
        trace.add_event(newFSEvent)

        velocity = velocity_events[velocity_num]

        f.write("{"+ velocity +" , "+ footswitch +"}\n")


        for j in range(0,4):
            velocity_num = random.randint(-1, 1)
            velocity = velocity_events[velocity_num]

            velEvent, velParam = _split_and_convert_event(velocity)
            newVelEvent = Event(velEvent, velParam)
            trace.add_event(newVelEvent)
            speed_ok_event = Event("speed_ok", None)
            trace.add_event(speed_ok_event)

            f.write("{"+ velocity +" , "+ footswitch +"}\n")
            f.write("{"+ velocity +" , "+ footswitch +"}\n")

        footswitch_bool = not footswitch_bool
        footswitch = footswitch_events[footswitch_bool]

        fsEvent, fsParam = _split_and_convert_event(footswitch_events[footswitch_bool])
        newFSEvent = Event(fsEvent, fsParam)
        trace.add_event(newFSEvent)

        velocity = velocity_events[velocity_num]

        f.write("{"+ velocity +" , "+ footswitch +"}\n")


    f.close()

    to_assertion("scenario0-"+str(traceLength), trace)

def build_collecting_or_replaceing_tools_section(trace, fileHandle, velocity_events, add_footswitch_event = False):
    """builds a trace of 20 low-speed, 'speed_ok' pairs with the footswitch set to true """

    footswitch = footswitch_events[1]
    if add_footswitch_event:
        fsEvent, fsParam = _split_and_convert_event(footswitch)
        newFSEvent = Event(fsEvent, fsParam)
        trace.add_event(newFSEvent)
        fs_reply_event = Event("enter_hands_on_mode", None)
        trace.add_event(fs_reply_event)

    for i in range(0,10):
        velocity_num = random.randint(-1, 1)
        velocity = velocity_events[velocity_num]

        velEvent, velParam = _split_and_convert_event(velocity)
        newVelEvent = Event(velEvent, velParam)
        trace.add_event(newVelEvent)
        speed_ok_event = Event("speed_ok", None)
        trace.add_event(speed_ok_event)

        fileHandle.write("{"+ velocity +" , "+ footswitch +"}\n")
        fileHandle.write("{"+ velocity +" , "+ footswitch +"}\n")

    return trace

def build_tiles_or_bolts_section(trace, fileHandle, velocity_events, starting_footswitch=None, footswitch_used=False, unsafe_velocity_events=None):
    """ builds a trace of 50 events including velocity, 'speed_ok', and potentially footswitch changes.
        unsafeSpeeds says wether we might generate a speed too fast for the mode"""

    if starting_footswitch == None or not starting_footswitch:
        footswitch = footswitch_events[0]
        footswitch_bool = False
    elif starting_footswitch:
        footswitch = footswitch_events[1]
        footswitch_bool = True

    if unsafe_velocity_events != None and footswitch_used == False:
        print("If")
        assert(type(unsafe_velocity_events) == type([]))

        for i in range(0,5):
            velocity_num = random.randint(-1, (len(velocity_events)-1))
            velocity = velocity_events[velocity_num]

            velEvent, velParam = _split_and_convert_event(velocity)
            newVelEvent = Event(velEvent, velParam)
            trace.add_event(newVelEvent)
            speed_ok_event = Event("speed_ok", None)
            trace.add_event(speed_ok_event)

            fileHandle.write("{"+ velocity +" , "+ footswitch +"}\n")
            fileHandle.write("{"+ velocity +" , "+ footswitch +"}\n")

        joined_velocity_events =  velocity_events.extend(unsafe_velocity_events)
        for j in range(0,20):
                velocity_num = random.randint(-1, (len(velocity_events)-1))
                velocity = velocity_events[velocity_num]

                velEvent, velParam = _split_and_convert_event(velocity)
                newVelEvent = Event(velEvent, velParam)
                trace.add_event(newVelEvent)
                speed_ok_event = Event("speed_ok", None)
                trace.add_event(speed_ok_event)

                fileHandle.write("{"+ velocity +" , "+ footswitch +"}\n")
                fileHandle.write("{"+ velocity +" , "+ footswitch +"}\n")

    elif footswitch_used == True:
        print("First elif")
        print(velocity_events)
        for i in range(0,5):
            velocity_num = random.randint(0, (len(velocity_events)/2)-1)
            print("Velocity Num", velocity_num)
            velocity = velocity_events[velocity_num]

            velEvent, velParam = _split_and_convert_event(velocity)
            newVelEvent = Event(velEvent, velParam)
            trace.add_event(newVelEvent)
            speed_ok_event = Event("speed_ok", None)
            trace.add_event(speed_ok_event)

            fileHandle.write("{"+ velocity +" , "+ footswitch +"}\n")
            fileHandle.write("{"+ velocity +" , "+ footswitch +"}\n")


        if unsafe_velocity_events != None:
            velocity_events.extend(unsafe_velocity_events)
            for j in range(0,20):

                if j % 5 == 0:
                    footswitch_bool = not footswitch_bool
                    footswitch = footswitch_events[footswitch_bool]

                    fsEvent, fsParam = _split_and_convert_event(footswitch_events[footswitch_bool])
                    newFSEvent = Event(fsEvent, fsParam)
                    trace.add_event(newFSEvent)

                    if footswitch_bool:
                        fs_reply_event = Event("enter_hands_on_mode", None)
                    else:
                        fs_reply_event = Event("enter_autonomous_mode", None)

                    trace.add_event(fs_reply_event)

                else:

                    if footswitch_bool:
                        velocity_num = random.randint(0, (len(velocity_events)-1))
                    else:
                        velocity_num = random.randint(0, (len(velocity_events)/2)-1)
                    velocity = velocity_events[velocity_num]

                    velEvent, velParam = _split_and_convert_event(velocity)
                    newVelEvent = Event(velEvent, velParam)
                    trace.add_event(newVelEvent)
                    speed_ok_event = Event("speed_ok", None)
                    trace.add_event(speed_ok_event)
        else:
            print("Else")

            for j in range(0,20):

                if j % 5 == 0:
                    footswitch_bool = not footswitch_bool
                    footswitch = footswitch_events[footswitch_bool]

                    fsEvent, fsParam = _split_and_convert_event(footswitch_events[footswitch_bool])
                    newFSEvent = Event(fsEvent, fsParam)
                    trace.add_event(newFSEvent)

                    if footswitch_bool:
                        fs_reply_event = Event("enter_hands_on_mode", None)
                    else:
                        fs_reply_event = Event("enter_autonomous_mode", None)

                    trace.add_event(fs_reply_event)

                else:

                    if footswitch_bool:
                        velocity_num = random.randint(0, (len(velocity_events)-1))
                    else:
                        velocity_num = random.randint(0, (len(velocity_events)/2)-1)
                    velocity = velocity_events[velocity_num]

                    velEvent, velParam = _split_and_convert_event(velocity)
                    newVelEvent = Event(velEvent, velParam)
                    trace.add_event(newVelEvent)
                    speed_ok_event = Event("speed_ok", None)
                    trace.add_event(speed_ok_event)

                fileHandle.write("{"+ velocity +" , "+ footswitch +"}\n")
                fileHandle.write("{"+ velocity +" , "+ footswitch +"}\n")


    else:
        print("Outer else?")
        for i in range(0,25):
            velocity_num = random.randint(-1, (len(velocity_events)-1))
            velocity = velocity_events[velocity_num]

            velEvent, velParam = _split_and_convert_event(velocity)
            newVelEvent = Event(velEvent, velParam)
            trace.add_event(newVelEvent)
            speed_ok_event = Event("speed_ok", None)
            trace.add_event(speed_ok_event)

            fileHandle.write("{"+ velocity +" , "+ footswitch +"}\n")
            fileHandle.write("{"+ velocity +" , "+ footswitch +"}\n")

    return (velocity, footswitch)

def build_scenario_1():
    """ Builds Scenario 1, where the Operator enters and stays in hands on mode
    and the speed is under the limit """

    velocity_events = ['"velocity":100', '"velocity":500','"velocity":750', '"velocity":1000']
    trace = Trace(Event("system_init"))
    f = open("scenario1.json", "w")

    build_collecting_or_replaceing_tools_section(trace, f, velocity_events, add_footswitch_event = True)

    build_tiles_or_bolts_section(trace, f, velocity_events, starting_footswitch=True)
    build_tiles_or_bolts_section(trace, f, velocity_events, starting_footswitch=True)
    build_tiles_or_bolts_section(trace, f, velocity_events, starting_footswitch=True)

    build_collecting_or_replaceing_tools_section(trace, f, velocity_events)

    f.close()

    to_assertion("scenario1", trace)

def build_scenario_2():
    """ Builds Scenario 2, where the Operator enters and stays in hands on mode,
    but speed exceeds limit after completing some of the mission's tasks. """

    velocity_events = ['"velocity":100', '"velocity":500', '"velocity":750', '"velocity":1000']

    trace = Trace(Event("system_init"))
    f = open("scenario2.json", "w")

    build_collecting_or_replaceing_tools_section(trace, f, velocity_events, add_footswitch_event = True)

    build_tiles_or_bolts_section(trace, f, velocity_events,  starting_footswitch=True)
    build_tiles_or_bolts_section(trace, f, velocity_events,  starting_footswitch=True, unsafe_velocity_events=['"velocity":1250'] )
    build_tiles_or_bolts_section(trace, f, velocity_events,  starting_footswitch=True)

    build_collecting_or_replaceing_tools_section(trace, f, velocity_events)

    f.close()

    to_assertion("scenario2", trace)


def build_scenario_3():
    """ Builds Scenario 3, where the Operator switches to autonomous mode after
     completing some of the mission's tasks and the speed is fine """

    autonomous_velocicities = ['"velocity":100', '"velocity":500']
    hands_on_velocities = [ '"velocity":750', '"velocity":1000']
    velocity_events = autonomous_velocicities + hands_on_velocities

    trace = Trace(Event("system_init"))
    f = open("scenario3.json", "w")

    build_collecting_or_replaceing_tools_section(trace, f, autonomous_velocicities, add_footswitch_event = True)

    build_tiles_or_bolts_section(trace, f, velocity_events, starting_footswitch=True, footswitch_used=True)
    build_tiles_or_bolts_section(trace, f, velocity_events, starting_footswitch=True, footswitch_used=True)
    build_tiles_or_bolts_section(trace, f, velocity_events, starting_footswitch=True, footswitch_used=True)

    build_collecting_or_replaceing_tools_section(trace, f, hands_on_velocities)

    f.close()

    to_assertion("scenario3", trace)

def build_scenario_4():
    """ Builds Scenario 4, where the Operator switches to autonomous mode after
     completing some of the mission's tasks and speed exceeds limit"""

    autonomous_velocicities = ['"velocity":100', '"velocity":500']
    hands_on_velocities = [ '"velocity":750', '"velocity":1000']
    velocity_events = autonomous_velocicities + hands_on_velocities

    trace = Trace(Event("system_init"))
    f = open("scenario4.json", "w")

    build_collecting_or_replaceing_tools_section(trace, f, autonomous_velocicities, add_footswitch_event = True)

    #Technically the autonomous velocities are unsafe too, for the hands on
    #mode, but this scenario specifically wants the higher speed limit to be broken
    build_tiles_or_bolts_section(trace, f, velocity_events, starting_footswitch=True, footswitch_used=True, unsafe_velocity_events=['"velocity":1250'])
    build_tiles_or_bolts_section(trace, f, velocity_events, starting_footswitch=True, footswitch_used=True, unsafe_velocity_events=['"velocity":1250'])
    build_tiles_or_bolts_section(trace, f, velocity_events, starting_footswitch=True, footswitch_used=True, unsafe_velocity_events=['"velocity":1250'])

    build_collecting_or_replaceing_tools_section(trace, f, autonomous_velocicities)

    f.close()

    to_assertion("scenario4", trace)

def build_safe_state_key_usage(trace, fileHandle, lastTelegram):
    """Builds part of a trace where the safe state key is use to trigger an emergency stop"""
    #safe_state_key.PresentOn -> emergency_stop -> safe_stop_cat1-> enter_safe_state
    assert(isinstance(lastTelegram, tuple) )

    #ss_key" :"safe_state_key" , "em_stop" : "emergency_stop" , "cat_1_stop" : "safe_stop_cat1" ,
    #"safe_state" : "enter_safe_state"

    velocity = lastTelegram[0]
    footswitch = lastTelegram[1]

    safeStateEvent = Event("safe_state_key", "PresentOn")
    trace.add_event(safeStateEvent)

    ssKey = '\"ss_key\":\"PresentOn\"'

    fileHandle.write("{"+ velocity +" , "+ footswitch + ", " + ssKey + "}\n")

    emStopEvent = Event("emergency_stop")
    trace.add_event(emStopEvent)

    safeStopEvent = Event("safe_stop_cat1")
    trace.add_event(safeStopEvent)

    # I'm assuming that the telegram wont need either emergency stop or safet stop

    entSafeStateEvent = Event("enter_safe_state")
    trace.add_event(entSafeStateEvent)

    safeState = ' \"safe_state\" : true'
    fileHandle.write("{"+ velocity +" , "+ footswitch + ", " + safeState + "}\n")


def build_reset_and_restart_usage(trace, fileHandle, lastTelegram):
    """Builds part of a trace where the system is reset and restarted """

    assert(isinstance(lastTelegram, tuple))

    velocity = lastTelegram[0]
    footswitch = lastTelegram[1]

    safeStateEvent = Event("reset")
    trace.add_event(safeStateEvent)

    safeStateEvent = Event("restart")
    trace.add_event(safeStateEvent)

    #Assuming that the telegram wont need with reset or restart.

    safeStateEvent = Event("leave_safe_state")
    trace.add_event(safeStateEvent)

    safeState = ' \"safe_state\" : false'
    fileHandle.write("{"+ velocity +" , "+ footswitch + ", " + safeState + "}\n")


def build_scenario_5():
    """ Builds Scenario 5, where the Safe State Key is used to trigger an
    emHMM1 = foot_pedal_pressed.True -> enter_hands_on_mode -> HMM1ergancy stop, during the mission. Then the system is reset, restarted,
    and the mission continues to completion."""

    autonomous_velocicities = ['"velocity":100', '"velocity":500']
    hands_on_velocities = [ '"velocity":750', '"velocity":1000']
    velocity_events = autonomous_velocicities + hands_on_velocities

    trace = Trace(Event("system_init"))
    f = open("scenario5.json", "w")

    build_collecting_or_replaceing_tools_section(trace, f, autonomous_velocicities, add_footswitch_event = True)

    lastTelegram = build_tiles_or_bolts_section(trace, f, velocity_events, starting_footswitch=True, footswitch_used=True)

    print("Entering safe state key usage with ", lastTelegram)
    build_safe_state_key_usage(trace, f, lastTelegram)

    build_reset_and_restart_usage(trace, f, lastTelegram)

    footswitch = lastTelegram[1]

    fsList = footswitch.split(":")

    lastTelegram = build_tiles_or_bolts_section(trace, f, velocity_events, starting_footswitch=fsList[1],footswitch_used=True)

    footswitch = lastTelegram[1]

    fsList = footswitch.split(":")

    build_tiles_or_bolts_section(trace, f, velocity_events, starting_footswitch=fsList[1], footswitch_used=True)

    build_collecting_or_replaceing_tools_section(trace, f, autonomous_velocicities)

    f.close()

    to_assertion("scenario5", trace)

def build_master_commissioning_mode_on(trace, fileHandle, lastTelegram):
    """ Builds part of a trace where the master Commissioning mode is entered """

    assert(isinstance(lastTelegram, tuple))

    velocity = lastTelegram[0]
    footswitch = lastTelegram[1]


    mcmSwitchEvent = Event("master_commissioning_switch", "MCM_On")
    trace.add_event(mcmSwitchEvent)

    mcmTelegram = '\"mcm_switch\":true'
    fileHandle.write("{"+ velocity +" , "+ footswitch + ", " + mcmTelegram + "}\n")

    resetEvent = Event("reset")
    trace.add_event(resetEvent)

    enterMCSEvent = Event("enter_master_commissioning_state")
    trace.add_event(enterMCSEvent)


def build_scenario_6():
    """Build a trace where the system is reset with the Master Commissioning Mode Key set to 'On'. Some movements occur that are unmoniotred (so don't trigger the protective stop), then the safe state key is used to enter the safe state (and so exit the Master Commissioning State). Then the system is reset.
    """

    autonomous_velocicities = ['"velocity":100', '"velocity":500']
    hands_on_velocities = [ '"velocity":750', '"velocity":1000']
    velocity_events = autonomous_velocicities + hands_on_velocities

    trace = Trace(Event("system_init"))
    f = open("scenario6.json", "w")

    velocity = '"velocity":0'
    footswitch = footswitch_events[0]

    firstTelegram = (velocity, footswitch)

    build_safe_state_key_usage(trace, f, firstTelegram)

    build_master_commissioning_mode_on(trace, f, firstTelegram)

    build_collecting_or_replaceing_tools_section(trace, f, velocity_events, add_footswitch_event = True)

    midTelegram = (velocity, footswitch[1])

    build_safe_state_key_usage(trace, f, midTelegram)

    build_reset_and_restart_usage(trace, f, midTelegram)

    f.close()

    to_assertion("scenario6", trace)

def build_slave_commissioning_mode_on(trace, fileHandle, lastTelegram):
    pass

def build_slave_commissioning_mode_off(trace, fileHandle, lastTelegram):
    pass

def build_scenario_7():
    """ Builds a trace where the Slave commisioning mode switch is used to put
    the system into the Slave Commissioning Mode. Some movements are performed
    for troubleshooting. Then slave commissioning mode is disabled, again using
    the Slave Commissioning mode switch."""

    autonomous_velocicities = ['"velocity":100', '"velocity":500']
    hands_on_velocities = [ '"velocity":750', '"velocity":1000']
    velocity_events = autonomous_velocicities + hands_on_velocities

    trace = Trace(Event("system_init"))
    f = open("scenario7.json", "w")

    velocity = '"velocity":0'
    footswitch = footswitch_events[0]

    firstTelegram = (velocity, footswitch)

    build_safe_state_key_usage(trace, f, firstTelegram)

    build_slave_commissioning_mode_on(trace, f, firstTelegram)

    build_collecting_or_replaceing_tools_section(trace, f, velocity_events, add_footswitch_event = True)

    midTelegram = (velocity, footswitch[1])

    build_slave_commissioning_mode_off(trace, f, firstTelegram)

    f.close()

    to_assertion("scenario7", trace)




if __name__ == '__main__':

    eventMap = {"velocity": "speed", "footswitch": "foot_pedal_pressed", "system_init" : "system_init",
    "ss_key" :"safe_state_key" , "em_stop" : "emergency_stop" , "cat_1_stop" : "safe_stop_cat1" ,
    "safe_state" : "enter_safe_state", "mcm_switch":"master_commissioning_switch"}

    footswitch_events = ['"footswitch": false', '"footswitch": true']

    print("+++ You Commented Them All Out, Dufus +++")

    #Parameter is the trace length
    #build_scenario_0(10)

    #build_scenario_0(10)
    #build_scenario_0(100)
    #build_scenario_0(1000)
    #build_scenario_0(10000)
    #build_scenario_0(100000)

    #build_scenario_1()

    #build_scenario_2()

    #build_scenario_3()

    #build_scenario_4()

    #build_scenario_5()

    #build_scenario_6()

    #build_scenario_7()
