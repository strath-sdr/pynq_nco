from pynq import DefaultHierarchy
from pynq import allocate
import numpy as np

_MAX_TRANSFER = 4096

class DataInspector(DefaultHierarchy):
    """A class to control the Data Inspector hierarchy."""

    @staticmethod
    def checkhierarchy(description):
        """The DataInspector class must contain an AXI DMA and Packet Generator."""
        if 'axi_dma' in description['ip'] \
           and 'packet_generator' in description['ip']:
            return True
        return False 
    
    def __init__(self, description):
        """Class constructor for the DataInspector hierarchy."""
        super().__init__(description=description)
        self._recv_buffer = allocate(shape=(_MAX_TRANSFER*2), dtype=np.int16)
        temp = self.transfer(_MAX_TRANSFER)
        
    def transfer(self, packetsize):
        """Transfer samples from the FPGA logic fabric to the Processing System.
        
        Parameters
        ----------
            packetsize : int
                number of samples to transfer
        """
        self.packet_generator.packetsize = int(packetsize)
        self.packet_generator.reset = 0
        self.axi_dma.recvchannel.transfer(self._recv_buffer)
        self.packet_generator.enable = 1
        self.axi_dma.recvchannel.wait()
        self.packet_generator.enable = 0
        self.packet_generator.reset = 1
        t_data = np.array(self._recv_buffer[0:packetsize*2]) * 2**-15
        c_data = t_data[::2] + 1j * t_data[1::2]
        return c_data
        
