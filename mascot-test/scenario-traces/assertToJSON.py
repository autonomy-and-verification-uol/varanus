import json

scen1 = "<system_init, foot_pedal_pressed. true, enter_hands_on_mode, speed.100, speed_ok, speed.100, speed_ok, speed.1000, speed_ok, speed.100, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.750, speed_ok, speed.500, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.750, speed_ok, speed.500, speed_ok, speed.1000, speed_ok, speed.750, speed_ok, speed.750, speed_ok, speed.1000, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.1000, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.1000, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.1000, speed_ok, speed.750, speed_ok, speed.1000, speed_ok, speed.750, speed_ok, speed.750, speed_ok, speed.750, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.750, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.100, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.1000, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.1000, speed_ok, speed.750, speed_ok, speed.750, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.500, speed_ok, speed.1000, speed_ok, speed.750, speed_ok, speed.500, speed_ok, speed.750, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.1000, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.100, speed_ok>"

scen2 = "<system_init, foot_pedal_pressed. true, enter_hands_on_mode, speed.500, speed_ok, speed.500, speed_ok, speed.1000, speed_ok, speed.100, speed_ok, speed.1000, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.500, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.500, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.100, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.750, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.100, speed_ok, speed.1000, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.1000, speed_ok, speed.1250, speed_ok, speed.1250, speed_ok, speed.500, speed_ok, speed.1000, speed_ok, speed.1250, speed_ok, speed.1250, speed_ok, speed.1250, speed_ok, speed.750, speed_ok, speed.1000, speed_ok, speed.100, speed_ok, speed.1250, speed_ok, speed.100, speed_ok, speed.750, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.1000, speed_ok, speed.1250, speed_ok, speed.1250, speed_ok, speed.1250, speed_ok, speed.1000, speed_ok, speed.750, speed_ok, speed.1250, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.1250, speed_ok, speed.1250, speed_ok, speed.100, speed_ok, speed.750, speed_ok, speed.750, speed_ok, speed.750, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.1000, speed_ok, speed.1250, speed_ok, speed.100, speed_ok, speed.1250, speed_ok, speed.1000, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.1250, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.1250, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.100, speed_ok>"

scen2a =  "<system_init, foot_pedal_pressed. true, enter_hands_on_mode, speed.500, speed_ok, speed.500, speed_ok, speed.1000, speed_ok, speed.100, speed_ok, speed.1000, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.500, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.500, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.100, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.750, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.100, speed_ok, speed.1000, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.1000, speed_ok, speed.1250, protective_stop, safe_stop_cat1, enter_safe_state, reset, get_mcmState.false, restart, leave_safe_state, speed.1000, speed_ok, speed.750, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.750, speed_ok, speed.750, speed_ok, speed.750, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.1000, speed_ok, speed.750, speed_ok,  speed.100, speed_ok, speed.750, speed_ok, speed.1000, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.750, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.100, speed_ok>"

scen2b = " <system_init, foot_pedal_pressed. true, enter_hands_on_mode, speed.500, speed_ok, speed.500, speed_ok, speed.1000, speed_ok, speed.100, speed_ok, speed.1000, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.500, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.500, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.100, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.750, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.100, speed_ok, speed.1000, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.1000, speed_ok, speed.1250, protective_stop, safe_stop_cat1, enter_safe_state, safe_state_key.Removed, getState.Safe, safe_state_key.Replaced, reset, get_mcmState.false, restart, leave_safe_state, speed.1000, speed_ok, speed.750, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.750, speed_ok, speed.750, speed_ok, speed.750, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.1000, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.750, speed_ok, speed.1000, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.750, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.100, speed_ok>"

scen3 = "<system_init, foot_pedal_pressed. true, enter_hands_on_mode, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, foot_pedal_pressed. false, enter_autonomous_mode, speed.500, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.100, speed_ok, foot_pedal_pressed. true, enter_hands_on_mode, speed.500, speed_ok, speed.750, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, foot_pedal_pressed. false, enter_autonomous_mode, speed.100, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.100, speed_ok, foot_pedal_pressed. true, enter_hands_on_mode, speed.500, speed_ok, speed.100, speed_ok, speed.750, speed_ok, speed.1000, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, foot_pedal_pressed. false, enter_autonomous_mode, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.500, speed_ok, foot_pedal_pressed. true, enter_hands_on_mode, speed.500, speed_ok, speed.1000, speed_ok, speed.500, speed_ok, speed.750, speed_ok, foot_pedal_pressed. false, enter_autonomous_mode, speed.500, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.500, speed_ok, foot_pedal_pressed. true, enter_hands_on_mode, speed.750, speed_ok, speed.500, speed_ok, speed.1000, speed_ok, speed.750, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, foot_pedal_pressed. false, enter_autonomous_mode, speed.100, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.500, speed_ok, foot_pedal_pressed. true, enter_hands_on_mode, speed.1000, speed_ok, speed.1000, speed_ok, speed.750, speed_ok, speed.1000, speed_ok, foot_pedal_pressed. false, enter_autonomous_mode, speed.500, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.500, speed_ok, foot_pedal_pressed. true, enter_hands_on_mode, speed.1000, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.750, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.750, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok>"

scen4 = "<system_init, foot_pedal_pressed. true, enter_hands_on_mode, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, foot_pedal_pressed. false, enter_autonomous_mode, speed.100, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.100, speed_ok, foot_pedal_pressed. true, enter_hands_on_mode, speed.500, speed_ok, speed.500, speed_ok, speed.750, speed_ok, speed.1000, speed_ok, foot_pedal_pressed. false, enter_autonomous_mode, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, foot_pedal_pressed. true, enter_hands_on_mode, speed.1250, speed_ok, speed.1250, speed_ok, speed.1250, speed_ok, speed.1000, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, foot_pedal_pressed. false, enter_autonomous_mode, speed.750, speed_ok, speed.100, speed_ok, speed.750, speed_ok, speed.750, speed_ok, foot_pedal_pressed. true, enter_hands_on_mode, speed.1250, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.1250, speed_ok, foot_pedal_pressed. false, enter_autonomous_mode, speed.100, speed_ok, speed.750, speed_ok, speed.750, speed_ok, speed.100, speed_ok, foot_pedal_pressed. true, enter_hands_on_mode, speed.1000, speed_ok, speed.1250, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.750, speed_ok, foot_pedal_pressed. false, enter_autonomous_mode, speed.500, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, foot_pedal_pressed. true, enter_hands_on_mode, speed.1000, speed_ok, speed.1250, speed_ok, speed.500, speed_ok, speed.1000, speed_ok, foot_pedal_pressed. false, enter_autonomous_mode, speed.750, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.100, speed_ok, foot_pedal_pressed. true, enter_hands_on_mode, speed.100, speed_ok, speed.1250, speed_ok, speed.1250, speed_ok, speed.1250, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok> "

scen4a = "<system_init, foot_pedal_pressed. true, enter_hands_on_mode, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, foot_pedal_pressed.false, enter_autonomous_mode, speed.100, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.750, protective_stop, safe_stop_cat1, enter_safe_state, reset, get_mcmState.false, restart, leave_safe_state, foot_pedal_pressed. true, enter_hands_on_mode, speed.500, speed_ok, speed.500, speed_ok, speed.750, speed_ok, speed.1000, speed_ok, foot_pedal_pressed. false, enter_autonomous_mode, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, foot_pedal_pressed. true, enter_hands_on_mode, speed.750, speed_ok,speed.750, speed_ok, speed.750, speed_ok, speed.1000, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, foot_pedal_pressed. false, enter_autonomous_mode, speed.500, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, foot_pedal_pressed. true, enter_hands_on_mode, speed.750, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.750, speed_ok, foot_pedal_pressed. false, enter_autonomous_mode, speed.100, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.100, speed_ok, foot_pedal_pressed. true, enter_hands_on_mode, speed.1000, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.750, speed_ok, foot_pedal_pressed. false, enter_autonomous_mode, speed.500, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, foot_pedal_pressed. true, enter_hands_on_mode, speed.1000, speed_ok, speed.750, speed_ok, speed.500, speed_ok, speed.1000, speed_ok, foot_pedal_pressed. false, enter_autonomous_mode, speed.500, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.100, speed_ok, foot_pedal_pressed. true, enter_hands_on_mode, speed.100, speed_ok, speed.750, speed_ok, speed.750, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok> "

scen4b =  "<system_init, foot_pedal_pressed. true, enter_hands_on_mode, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, foot_pedal_pressed.false, enter_autonomous_mode, speed.100, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.750, protective_stop, safe_stop_cat1, enter_safe_state, safe_state_key.Removed, getState.Safe, safe_state_key.Replaced, reset, get_mcmState.false, restart, leave_safe_state, foot_pedal_pressed. true, enter_hands_on_mode, speed.500, speed_ok, speed.500, speed_ok, speed.750, speed_ok, speed.1000, speed_ok, foot_pedal_pressed. false, enter_autonomous_mode, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, foot_pedal_pressed. true, enter_hands_on_mode, speed.750, speed_ok,speed.750, speed_ok, speed.750, speed_ok, speed.1000, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, foot_pedal_pressed. false, enter_autonomous_mode, speed.500, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, foot_pedal_pressed. true, enter_hands_on_mode, speed.750, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.750, speed_ok, foot_pedal_pressed.false, enter_autonomous_mode, speed.100, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.100, speed_ok, foot_pedal_pressed. true, enter_hands_on_mode, speed.1000, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.750, speed_ok, foot_pedal_pressed. false, enter_autonomous_mode, speed.500, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, foot_pedal_pressed. true, enter_hands_on_mode, speed.1000, speed_ok, speed.750, speed_ok, speed.500, speed_ok, speed.1000, speed_ok, foot_pedal_pressed. false, enter_autonomous_mode, speed.500, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.100, speed_ok, foot_pedal_pressed. true, enter_hands_on_mode, speed.100, speed_ok, speed.750, speed_ok, speed.750, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok>"

scen5 = "<system_init, foot_pedal_pressed. true, enter_hands_on_mode, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, foot_pedal_pressed. false, enter_autonomous_mode, speed.100, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.100, speed_ok, foot_pedal_pressed. true, enter_hands_on_mode, speed.100, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.1000, speed_ok, foot_pedal_pressed. false, enter_autonomous_mode, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.500, speed_ok, foot_pedal_pressed. true, enter_hands_on_mode, speed.750, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, safe_state_key.PresentOn, emergency_stop, safe_stop_cat1, enter_safe_state, reset, get_mcmState.false, restart, leave_safe_state, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.100, speed_ok, foot_pedal_pressed. false, enter_autonomous_mode, speed.100, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, foot_pedal_pressed. true, enter_hands_on_mode, speed.1000, speed_ok, speed.500, speed_ok, speed.750, speed_ok, speed.500, speed_ok, foot_pedal_pressed. false, enter_autonomous_mode, speed.100, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.500, speed_ok, foot_pedal_pressed. true, enter_hands_on_mode, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.1000, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, foot_pedal_pressed. false, enter_autonomous_mode, speed.100, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.500, speed_ok, foot_pedal_pressed. true, enter_hands_on_mode, speed.1000, speed_ok, speed.750, speed_ok, speed.100, speed_ok, speed.750, speed_ok, foot_pedal_pressed. false, enter_autonomous_mode, speed.500, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.100, speed_ok, foot_pedal_pressed. true, enter_hands_on_mode, speed.500, speed_ok, speed.1000, speed_ok, speed.750, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok>"

scen6 = "<system_init, master_commissioning_switch.MCM_On, safe_state_key.PresentOn, emergency_stop, safe_stop_cat1, enter_safe_state, reset, get_mcmState.true, enter_master_commissioning_state, leave_safe_state, speed.1000, speed_ok, speed.100, speed_ok, speed.100, speed_ok, speed.1000, speed_ok, speed.1000, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.100, speed_ok, speed.500, speed_ok, speed.500, speed_ok, speed.1250, speed_ok, safe_state_key.PresentOn,  emergency_stop, safe_stop_cat1, enter_safe_state, leave_master_commissioning_state, reset, get_mcmState.false, restart, leave_safe_state, speed.100, speed_ok,  speed.1250, protective_stop >"

scen7 = "<system_init, slave_commissioning_switch.SCM_On, safe_stop_cat1, enter_slave_commissioning_state, slave_commissioning_switch.SCM_Off, leave_slave_commissioning_state, speed.100, speed_ok, speed.1250, protective_stop >"

def MakeJSON(name, line):
    print("+++ Processing line: "+name+" +++")
    line = line.strip("<")
    line = line.strip(">")
    line = line.strip()
    elems = line.split(", ")



    print("+++ Writing "+name+" to file +++")

    outputFile = file(name+"-trace.json", "w")

    outputFile.write(json.dumps(elems))


#MakeJSON( "scenario1", scen1)
#MakeJSON( "scenario2", scen2)
#MakeJSON( "scenario2a", scen2a)
#MakeJSON( "scenario2b", scen2b)
#MakeJSON( "scenario3", scen3)
#MakeJSON( "scenario4", scen4)
#MakeJSON( "scenario4a", scen4a)
#MakeJSON( "scenario4b", scen4b)
#MakeJSON( "scenario5", scen5)
#MakeJSON( "scenario6", scen6)
#MakeJSON( "scenario7", scen7)
print("+++ You Commented Them All Out, Dufus +++")