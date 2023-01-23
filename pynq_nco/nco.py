from pynq import DefaultIP

_SAMPLE_FREQUENCY = 100e6
_PHASE_WIDTH = 16

class NumericalOscillator(DefaultIP):
    def __init__(self, description):
        super().__init__(description=description)
        self.frequency = 1e6
        
    bindto = ["strathsdr.org:pynq:nco:1.0"]
        
    @property
    def _control(self):
        return self.read(0x00)
    
    @_control.setter
    def _control(self, value):
        self.write(0x00, value)
        
    @property
    def _phase(self):
        return self.read(0x04)
    
    @_phase.setter
    def _phase(self, value):
        self.write(0x04, value)
        
    @property
    def _gain(self):
        return self.read(0x08)
        
    @_gain.setter
    def _gain(self, value):
        self.write(0x08, value)
        
    @property
    def frequency(self):
        reg = self._phase*(2**-16)
        return (_SAMPLE_FREQUENCY*reg)/(2**_PHASE_WIDTH)
        
    @frequency.setter
    def frequency(self, value):
        if (value > _SAMPLE_FREQUENCY/2) and (value <= 0):
            raise ValueError(''.join(['Select a frequency between 1 and ', str(_SAMPLE_FREQUENCY)]))
        reg = ((value*(2**_PHASE_WIDTH))/_SAMPLE_FREQUENCY)
        self._phase = int(reg*(2**16))
        
    @property
    def gain(self):
        return self._gain*(2**-30)
    
    @gain.setter
    def gain(self, value):
        if (value > 1) or (value < -1):
            raise ValueError('Select a gain between -1 and 1')
        self._gain = int(value*(2**30))
        
    def complex_enable(self):
        reg = self._control
        reg |= 0x00000003
        self._control = reg
        
    def real_enable(self):
        reg = self._control
        reg &= 0xFFFFFFFC
        reg |= 0x00000001
        self._control = reg
        
    def disable(self):
        reg = self._control
        reg &= 0xFFFFFFFC
        self._control = reg
        