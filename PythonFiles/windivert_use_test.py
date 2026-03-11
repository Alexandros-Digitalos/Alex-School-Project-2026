import pydivert

with pydivert.WinDivert("tcp.DstPort == 1234 or tcp.SrcPort == 80") as w:
    for packet in w:
        if packet.dst_port == 1234:
            print(">") # packet to the server
            packet.dst_port = 80
        if packet.src_port == 80:
            print("<") # reply from the server
            packet.src_port = 1234
        w.send(packet)