from pynq import DefaultIP

_SAMPLE_FREQUENCY = 100e6
_PHASE_WIDTH = 16

class NumericalOscillator(DefaultIP):
    """A class to control an NCO IP Core."""
    def __init__(self, description):
        """Create a Numerical Oscillator object that controls the NCO IP Core in the PL."""
        super().__init__(description=description)
        self.frequency = 1e6
        self.real_enable()
        
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
        """The output frequency of the NCO."""
        reg = self._phase*(2**-16)
        return (_SAMPLE_FREQUENCY*reg)/(2**_PHASE_WIDTH)
        
    @frequency.setter
    def frequency(self, value):
        """Sets the desired frequency of the NCO."""
        if (value > _SAMPLE_FREQUENCY/2) and (value <= 0):
            raise ValueError(''.join(['Select a frequency between 1 and ', str(_SAMPLE_FREQUENCY)]))
        reg = ((value*(2**_PHASE_WIDTH))/_SAMPLE_FREQUENCY)
        self._phase = int(reg*(2**16))
        
    @property
    def gain(self):
        """The output gain of the NCO."""
        return self._gain*(2**-30)
    
    @gain.setter
    def gain(self, value):
        """Sets the NCO gain."""
        if (value > 1) or (value < -1):
            raise ValueError('Select a gain between -1 and 1')
        self._gain = int(value*(2**30))
        
    def complex_enable(self):
        """Enables the Cosine and Sine wave output of the NCO."""
        reg = self._control
        reg |= 0x00000003
        self._control = reg
        
    def real_enable(self):
        """Enables the Cosine wave output only of the NCO."""
        reg = self._control
        reg &= 0xFFFFFFFC
        reg |= 0x00000001
        self._control = reg
        
    def disable(self):
        """Disables the Cosine and Sine wave output of the NCO."""
        reg = self._control
        reg &= 0xFFFFFFFC
        self._control = reg
        
