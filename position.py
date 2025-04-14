from gii_bluerov import gii_bluerov
import dronekit
from time import sleep


connection_string="192.168.3.20:14552"
print("Connecting to vehicle on: %s" % (connection_string,))
autopilot = dronekit.connect(connection_string, wait_ready=True)
autopilot.armed = True
home_location = autopilot.location.global_relative_frame
print(f"Marked Home Location: {home_location.lat}, {home_location.lon}, {home_location.alt}")

gii_bluerov.move_rov(autopilot, "x","displacement", 10)
sleep(5)
location = autopilot.location.global_relative_frame
print(f"Current Location: {location.lat}, {location.lon}, {location.alt}")

print("Depth: ", autopilot.location.global_relative_frame.alt)
print("Heading: ", autopilot.heading)

if autopilot.location.local_frame:
    print("Local Position: NED",
          autopilot.location.local_frame.north,
          autopilot.location.local_frame.east,
          autopilot.location.local_frame.down)
else:
    print("No local NED data available.")


