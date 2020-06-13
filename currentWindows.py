from AppKit import NSWorkspace
import time

awn = ""

while True:
        nwn = (NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'])

        if awn != nwn:
            awn = nwn
            print(awn)

        time.sleep(10)
