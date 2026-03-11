from pydivert import *
from json import *

with WinDivert() as wdiv:
    for packet in wdiv:
        print(packet)
        wdiv.send(packet)
        json_data = dumps(str(packet), indent=4)
        captured_packet = open("captured_packet.json", "w", encoding="utf-8") 
        captured_packet.write(json_data)
        break