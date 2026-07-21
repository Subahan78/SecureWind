turbine_running = False
def start_turbine():
    global turbine_running
    if turbine_running:
        print("\nTurbine is already running.")
    else:
        turbine_running = True
        print("\nTurbine Started Successfully.")
def stop_turbine():
    global turbine_running
    if not turbine_running:
        print("\nTurbine is already stopped.")
    else:
        turbine_running = False
        print("\nTurbine Stopped Successfully.")
def turbine_status():
    if turbine_running:
        print("\nStatus : RUNNING")
    else:
        print("\nStatus : STOPPED")
