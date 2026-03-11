from network import Switch

my_switch = Switch("devnet-switch")

my_switch.incoming_frame("00:11:22:33:44:55", "66:77:88:99:AA:01", ingress_port="Eth0/1", size="1500")
my_switch.incoming_frame("DE:AD:BE:EF:00:03", "00:11:22:33:44:55", ingress_port="Eth0/2", size="64")
my_switch.incoming_frame("DE:AD:BE:EF:00:03", "FF:FF:FF:FF:FF:FF", ingress_port="Eth0/2", size="1500")
my_switch.incoming_frame("00:11:22:33:44:55", "DE:AD:BE:EF:00:03", ingress_port="Eth0/1", size="1500")
my_switch.incoming_frame("00:11:22:33:44:55", "66:77:88:99:AA:01", ingress_port="Eth0/1", size="950")
