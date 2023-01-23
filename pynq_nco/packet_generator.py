from pynq import DefaultIP

_MAX_TRANSFER = 4096

class PacketGenerator(DefaultIP):
        
    def __init__(self, description):
        super().__init__(description=description)
        self.packetsize = 1024
        
    @property
    def reset(self):
        return self.read(0x00)
    
    @property
    def enable(self):
        return self.read(0x04)
    
    @property
    def packetsize(self):
        return self.read(0x08)
    
    @reset.setter
    def reset(self, value):
        self.write(0x00, value)
        
    @enable.setter
    def enable(self, value):
        self.write(0x04, value)
        
    @packetsize.setter
    def packetsize(self, value):
        if (value > _MAX_TRANSFER) or (value < 16):
            raise ValueError(''.join(['Packet size must be between 16 and ', str(_MAX_TRANSFER)]))
        self.write(0x08, value)
            
    bindto = ['strathsdr.org:PYNQ-SDR:axis_packet_controller:1.0']
    