import pydivert

with pydivert.WinDivert() as wdiv:
    for packet in wdiv:
        print(packet)
        wdiv.send(packet)
        break