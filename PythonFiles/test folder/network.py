import json

class Switch:
    interface_names = ["Eth0/1", "Eth0/2", "Eth0/3", "Eth0/4", "Eth0/5", "Eth0/6", "Eth0/7", "Eth0/8"]

    mac_table = {}

    def __init__(self, hostname = "switch"):
        self.hostname = hostname

    def forward_frame(self, dst_mac, egress_port, size):
        print(f" ⏭ Frame with destination {dst_mac} forwarded to {egress_port}")

    def flood_frame(self, dst_mac, ingress_port, size):
        print ("    💦 Flooding to all other ports")
        for egress_port in self.interface_names:
            if egress_port != ingress_port:
                self.forward_frame(dst_mac, egress_port, size)

    def incoming_frame(self, src_mac, dst_mac, ingress_port, size):
        print(f"⚠ Receied frame on {ingress_port} from {src_mac} to {dst_mac}")
        if src_mac not in self.mac_table:
            print(f"    👁 Learning {src_mac} on {ingress_port}")
            self.mac_table[src_mac] = ingress_port
            with open("self.mac_table.json", "w") as f:
                json.dump(self.mac_table, f)
        
        if dst_mac in self.mac_table:
            egress_port = self.mac_table[dst_mac]
            print(f"🟢 Dest address {dst_mac} found in MAC table on {egress_port}")
            self.forward_frame(dst_mac, egress_port, size)
        elif dst_mac == "FF:FF:FF:FF:FF:FF":
            print(f"🟡 Destination is Broadcast")
            self.flood_frame(dst_mac, ingress_port, size)
        else:
            print(f"🔴 Dest address {dst_mac} NOT found in MAC table")
            self.flood_frame(dst_mac, ingress_port, size)
        print()

    def show_mac_address_table(self):
        print()
        print("           Mac Address Table")
        print("----------------------------------------")
        print()
        print("Mac Address          Type         Ports")
        print("-----------------    -------      ------")

        with open("self.mac_table.json") as f:
            self.mac_table = json.load(f)
        for mac_address, intf_mame in self.mac_table.items():
            print(f"{mac_address}    DYNAMIC      {intf_mame}")