import keyboard
import time
#import gii_bluerov
import dronekit

from gii_bluerov import gii_bluerov


def main_control_loop(autopilot):
    print("ROV Control Started. Use arrow keys and U/D/L/R to control.")

    try:
        while True:
            if keyboard.is_pressed('up'):
                gii_bluerov.move_rov(autopilot, "x", "displacement", 15)
                print("Moving forward")
                time.sleep(5)

            elif keyboard.is_pressed('down'):
                gii_bluerov.move_rov(autopilot, "x", "displacement", -15)
                print("Moving backward")
                time.sleep(1)

            elif keyboard.is_pressed('right'):
                gii_bluerov.move_rov(autopilot, "y", "displacement", 15)
                print("Moving right")
                time.sleep(1)

            elif keyboard.is_pressed('left'):
                gii_bluerov.move_rov(autopilot, "y", "displacement", -15)
                print("Moving left")
                time.sleep(1)

            elif keyboard.is_pressed('u'):
                gii_bluerov.move_rov(autopilot, "z", "displacement", 15)
                print("Moving up")
                time.sleep(1)

            elif keyboard.is_pressed('d'):
                gii_bluerov.move_rov(autopilot, "z", "displacement", -15)
                print("Moving down")
                time.sleep(1)

            elif keyboard.is_pressed('l'):
                gii_bluerov.move_rov(autopilot, "z", "rotation", -15)
                print("Rotating left")
                time.sleep(1)

            elif keyboard.is_pressed('r'):
                gii_bluerov.move_rov(autopilot, "z", "rotation", 15)
                print("Rotating right")
                time.sleep(1)

    except KeyboardInterrupt:
        print("Control stopped by user.")
        # Disarm after using it


if __name__ == "__main__":
    connection_string="192.168.3.20:14552"
    print("Connecting to vehicle on: %s" % (connection_string,))
    autopilot = dronekit.connect(connection_string, wait_ready=True)
    # Get some vehicle attributes (state)
    print (" Battery: %s" % autopilot.battery)
    autopilot.armed=True
    print ("%s" % autopilot.armed)
    print(autopilot.location.global_relative_frame.alt)
    #gii_bluerov = gii_bluerov.gii_bluerov

    #gii_bluerov.move_rov(autopilot, "z","rotation", -15)
    main_control_loop(autopilot)
    
    autopilot.armed=False
    print ("%s" % autopilot.armed)