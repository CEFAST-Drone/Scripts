import dronekit

connection_string = "/dev/ttyAMAO"   #If we are using a USB connection, we must use "/dev/ttyACMO"
bould_rate = 115200   # Colocar o mesmo bould_rate
vehicle = connect(connection_string, baud=baud_rate, wait_ready=True)     #- wait_ready flag hold the program untill all the parameters are been read (=, not .)

print("Autopilot Firmware version: ", vehicle.version)
print("Autopilot capabilities (supports ftp): ", vehicle.capabilities.ftp)
print("Global Location: ", vehicle.location.global_frame)
print("Global Location (relative altitude): " vehicle.location.global_relative_frame)
print("Local Location: " vehicle.location.local_frame)    #NED
print("Attitude: " vehicle.attitude)
print("Velocity: " vehicle.velocity)
print("GPS: " vehicle.gps_0)
print("Groundspeed: " vehicle.groundspeed)
print("Airspeed: " vehicle.airspeed)
print("Gimbal status: " vehicle.gimbal)
print("Battery: ", vehicle.battery)
print("EKF OK?: ", vehicle.ekf_ok)
print("Last Heartbeat: ", vehicle.last_heartbeat)
print("Rangefinder: ", vehicle.rangefinder)
print("Rangefinder distance: ", vehicle.rangefinder.distance)
print("Rangefinder voltage: ", vehicle.rangefinder.voltage)
print("Heading: ", vehicle.heading)
print("Is Armable?: ", vehicle.is_armable)
print("System status: ", vehicle.system_status.state)
print("Mode: ", vehicle.mode.name)    # settable
print("Armed: ", vehicle.armed)    # settable
