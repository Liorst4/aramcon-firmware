from arambadge import badge
import time
import microcontroller
import digitalio
from pulseio import PWMOut

badge.show_bitmap('assets/speaker.bmp')
 
SAO_GPIO1 = microcontroller.pin.P0_04
SAO_GPIO2 = microcontroller.pin.P0_05

audio = PWMOut(SAO_GPIO1, duty_cycle=0, frequency=440, variable_frequency=True)
led = digitalio.DigitalInOut(SAO_GPIO2)
led.switch_to_output(True)

def note(name):
    octave = int(name[-1])
    PITCHES = "c,c#,d,d#,e,f,f#,g,g#,a,a#,b".split(",")
    pitch = PITCHES.index(name[:-1].lower())
    return 440 * 2 ** ((octave - 4) + (pitch - 9) / 12.)

sequence = [
  ("e5", 2), ("e5", 2), ("e5", 4), ("e5", 2), ("e5", 2), ("e5", 4),
  ("e5", 2), ("g5", 2), ("c5", 4), ("d5", 1), ("e5", 6), (None, 2),
  ("f5", 2), ("f5", 2), ("f5", 3), ("f5", 1), ("f5", 2), ("e5", 2),
  ("e5", 2), ("e5", 1), ("e5", 1), ("e5", 2), ("d5", 2), ("d5", 2),
  ("e5", 2), ("d5", 4), ("g5", 2), (None, 2),
  ("e5", 2), ("e5", 2), ("e5", 4), ("e5", 2), ("e5", 2), ("e5", 4),
  ("e5", 2), ("g5", 2), ("c5", 4), ("d5", 1), ("e5", 6), (None, 2),
  ("f5", 2), ("f5", 2), ("f5", 3), ("f5", 1), ("f5", 2), ("e5", 2),
  ("e5", 2), ("e5", 1), ("e5", 1), ("g5", 2), ("g5", 2), ("f5", 2),
  ("d5", 2), ("c5", 6), (None, 2)
]

for (notename, eigths) in sequence:
    length = eigths * 0.1
    if notename:
        led.value = False
        audio.frequency = round(note(notename))
        audio.duty_cycle = 0x8000
    time.sleep(length)
    led.value = True
    audio.duty_cycle = 0
    time.sleep(0.025)

time.sleep(3)
