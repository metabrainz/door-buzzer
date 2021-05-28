from time import sleep
import RPi.GPIO as GPIO

OPEN_DURATION_MIN = 2  # seconds
OPEN_DURATION_MAX = 10  # seconds

# GPIO pin to driver the relay, using positive logic.
pin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

def open_door(duration):
    if duration < OPEN_DURATION_MIN:
        raise DoorException("Duration is too short: %s seconds. "
                            "Minimum duration: %s seconds." %
                            (duration, OPEN_DURATION_MIN))
    if duration > OPEN_DURATION_MAX:
        raise DoorException("Duration is too long: %s seconds. "
                            "Maximum duration: %s seconds." %
                            (duration, OPEN_DURATION_MAX))

    GPIO.output(pin, GPIO.HIGH)
    sleep(duration)
    GPIO.output(pin, GPIO.LOW)

    return


class DoorException(Exception):
    pass
