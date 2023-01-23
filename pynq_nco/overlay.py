import os
from pynq import Overlay
from .packet_generator import PacketGenerator
from .data_inspector import DataInspector
from .nco import NumericalOscillator

class NumericalOverlay(Overlay):
    
    def __init__(self, bitfile_name=None, **kwargs):
        
        if bitfile_name is None:
            this_dir = os.path.dirname(__file__)
            bitfile_name = os.path.join(this_dir, 'bitstream', 'pynq_nco.bit')
            
        super().__init__(bitfile_name, **kwargs)
