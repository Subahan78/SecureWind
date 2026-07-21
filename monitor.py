import random
def monitor_turbine():

    temperature = random.randint(35, 95)
    wind_speed = random.randint(5, 30)
    rotor_speed = random.randint(8, 22)

    print("\n===================================")
    print("      TURBINE MONITOR")
    print("===================================")

    print("Temperature :", temperature, "°C")
    print("Wind Speed  :", wind_speed, "m/s")
    print("Rotor Speed :", rotor_speed, "RPM")

    print("-----------------------------------")

    if temperature > 80:
        print("ALERT : High Temperature!")

    if wind_speed > 25:
        print("ALERT : High Wind Speed!")

    if rotor_speed > 20:
        print("ALERT : Rotor Overspeed!")

    if (
        temperature <= 80
        and wind_speed <= 25
        and rotor_speed <= 20
    ):
        print("System Status : NORMAL")

    print("===================================")
