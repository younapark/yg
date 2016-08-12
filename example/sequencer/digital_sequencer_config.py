class PulseBoardConfig(object):
    def __init__(self, **kwargs):
        """ defaults """
        self.bit_file = 'digital_sequencer.bit'
        self.mode_nums = {'idle': 0, 'load': 1, 'run': 2}
        self.mode = 'idle'
        self.mode_wire = 0x00
        self.pipe_wire = 0x80
        self.channel_mode_wires = [0x01, 0x03, 0x05, 0x07]
        self.channel_stateinv_wires = [0x02, 0x04, 0x06, 0x08]
        self.clk_frequency = 50e6
        
        """ non-defaults """
        for kw in kwargs:
            setattr(self, kw, kwargs[kw])
#	self.channels = {c.key: c for c in self.channels}

class PulseChannelConfig(object):
    def __init__(self, **kwargs):
        self.name = None
        self.loc = None
        self.board='1'

        """ non-defaults """
        for kw in kwargs:
            setattr(self, kw, kwargs[kw])
        
        if self.name is None:
            raise Exception('channel name is unspecified')
        if self.loc is None:
            raise Exception('channel location is unspecified')
        
        self.key = self.name+'@'+self.loc

class TimingChannelConfig(object):
    def __init__(self, **kwargs):
        self.name = 'digital@T'
        self.dt_range = (1e-6, 30)

        """ non-defaults """
        for kw in kwargs:
            setattr(self, kw, kwargs[kw])



class DigitalSequencerConfig(object):
    def __init__(self):
        self.name = '%LABRADNODE%_digital_sequencer'
	self.update_id = 698024
	self.timing_channel = TimingChannelConfig()

        self.boards = {
            '1': PulseBoardConfig(
                device_id='Sr2 dev.',
                channels=[
                    PulseChannelConfig(loc='0', name='TTL0', mode='auto', manual_state=0, invert=0),
                    PulseChannelConfig(loc='1', name='_TTL1', mode='auto', manual_state=0, invert=0),
                    PulseChannelConfig(loc='2', name='TTL2', mode='auto', manual_state=0, invert=0),
                    PulseChannelConfig(loc='3', name='TTL3', mode='auto', manual_state=0, invert=0),
                    PulseChannelConfig(loc='4', name='TTL4', mode='auto', manual_state=0, invert=0),
                    PulseChannelConfig(loc='5', name='TTL5', mode='auto', manual_state=0, invert=0),
                    PulseChannelConfig(loc='6', name='TTL6', mode='auto', manual_state=0, invert=0),
                    PulseChannelConfig(loc='7', name='TTL7', mode='auto', manual_state=0, invert=0),
                    PulseChannelConfig(loc='8', name='_TTL8', mode='auto', manual_state=0, invert=0),
                    PulseChannelConfig(loc='9', name='TTL9', mode='auto', manual_state=0, invert=0),
                    PulseChannelConfig(loc='10', name='TTL10', mode='auto', manual_state=0, invert=0),
                    PulseChannelConfig(loc='11', name='TTL11', mode='auto', manual_state=0, invert=0),
                    PulseChannelConfig(loc='12', name='TTL12', mode='auto', manual_state=0, invert=0),
                    PulseChannelConfig(loc='13', name='TTL13', mode='auto', manual_state=0, invert=0),
                    PulseChannelConfig(loc='14', name='TTL14', mode='auto', manual_state=0, invert=0),
                    PulseChannelConfig(loc='15', name='_TTL15', mode='auto', manual_state=0, invert=0),

                    PulseChannelConfig(loc='16', name='TTL16', mode='auto', manual_state=0, invert=0),
                    PulseChannelConfig(loc='17', name='TTL17', mode='auto', manual_state=0, invert=0),
                    PulseChannelConfig(loc='18', name='TTL18', mode='auto', manual_state=0, invert=0),
                    PulseChannelConfig(loc='19', name='TTL19', mode='auto', manual_state=0, invert=0),
                    PulseChannelConfig(loc='20', name='TTL20', mode='auto', manual_state=0, invert=0),
                    PulseChannelConfig(loc='21', name='TTL21', mode='auto', manual_state=0, invert=0),
                    PulseChannelConfig(loc='22', name='TTL22', mode='auto', manual_state=0, invert=0),
                    PulseChannelConfig(loc='23', name='TTL23', mode='auto', manual_state=0, invert=0),
                    PulseChannelConfig(loc='24', name='TTL24', mode='auto', manual_state=0, invert=0),
                    PulseChannelConfig(loc='25', name='TTL25', mode='auto', manual_state=0, invert=0),
                    PulseChannelConfig(loc='26', name='TTL26', mode='auto', manual_state=0, invert=0),
                    PulseChannelConfig(loc='27', name='TTL27', mode='auto', manual_state=0, invert=0),
                    PulseChannelConfig(loc='28', name='TTL28', mode='auto', manual_state=0, invert=0),
                    PulseChannelConfig(loc='29', name='TTL29', mode='auto', manual_state=0, invert=0),
                    PulseChannelConfig(loc='30', name='TTL30', mode='auto', manual_state=0, invert=0),
                    # PulseChannelConfig(loc='B15', name='Troubleshoot', mode='auto', manual_state=0, invert=0),
                    #
                    # PulseChannelConfig(loc='C00', name='Broken!', mode='auto', manual_state=0, invert=0),
                    # PulseChannelConfig(loc='C01', name='RM Gain Switch', mode='auto', manual_state=0, invert=0),
                    # PulseChannelConfig(loc='C02', name='STIRAP P Switch', mode='auto', manual_state=0, invert=0),
                    # PulseChannelConfig(loc='C03', name='STIRAP P Trigger', mode='auto', manual_state=0, invert=0),
                    # PulseChannelConfig(loc='C04', name='STIRAP S Shutter', mode='auto', manual_state=0, invert=0),
                    # PulseChannelConfig(loc='C05', name='STIRAP S Switch', mode='auto', manual_state=0, invert=1),
                    # PulseChannelConfig(loc='C06', name='STIRAP S Trigger', mode='auto', manual_state=0, invert=0),
                    # PulseChannelConfig(loc='C07', name='TTLC07', mode='auto', manual_state=0, invert=0),
                    # PulseChannelConfig(loc='C08', name='TTLC08', mode='auto', manual_state=0, invert=0),
                    # PulseChannelConfig(loc='C09', name='TTLC09', mode='auto', manual_state=0, invert=0),
                    # PulseChannelConfig(loc='C10', name='TTLC10', mode='auto', manual_state=0, invert=0),
                    # PulseChannelConfig(loc='C11', name='TTLC11', mode='auto', manual_state=0, invert=0),
                    # PulseChannelConfig(loc='C12', name='TTLC12', mode='auto', manual_state=0, invert=0),
                    # PulseChannelConfig(loc='C13', name='TTLC13', mode='auto', manual_state=0, invert=0),
                    # PulseChannelConfig(loc='C14', name='TTLC14', mode='auto', manual_state=0, invert=0),
                    # PulseChannelConfig(loc='C15', name='ODT Servo Enable', mode='manual', manual_state=1, invert=0),
                    #
                    # PulseChannelConfig(loc='D00', name='Alpha AOM', mode='auto', manual_state=0, invert=0),
                    # PulseChannelConfig(loc='D01', name='Alpha Shutter', mode='auto', manual_state=0, invert=1),
                    # PulseChannelConfig(loc='D02', name='Beta AOM', mode='auto', manual_state=0, invert=0),
                    # PulseChannelConfig(loc='D03', name='Beta Shutter', mode='auto', manual_state=0, invert=1),
                    # PulseChannelConfig(loc='D04', name='Spin Pol. AOM', mode='auto', manual_state=0, invert=1),
                    # PulseChannelConfig(loc='D05', name='Spin Pol. Shutter', mode='auto', manual_state=0, invert=1),
                    # PulseChannelConfig(loc='D06', name='679 AOM', mode='auto', manual_state=0, invert=0),
                    # PulseChannelConfig(loc='D07', name='707 AOM', mode='auto', manual_state=0, invert=0),
                    # PulseChannelConfig(loc='D08', name='Repump Shutter', mode='auto', manual_state=0, invert=1),
                    # PulseChannelConfig(loc='D09', name='RM FM Trigger', mode='auto', manual_state=0, invert=0),
                    # PulseChannelConfig(loc='D10', name='TTLD10', mode='auto', manual_state=0, invert=0),
                    # PulseChannelConfig(loc='D11', name='TTLD11', mode='auto', manual_state=0, invert=0),
                    # PulseChannelConfig(loc='D12', name='TTLD12', mode='auto', manual_state=0, invert=0),
                    # PulseChannelConfig(loc='D13', name='TTLD13', mode='auto', manual_state=0, invert=0),
                    # PulseChannelConfig(loc='D14', name='AOSense Heater Enable', mode='manual', manual_state=1, invert=0),
                    # PulseChannelConfig(loc='D15', name='Trigger', mode='auto', manual_state=1, invert=1),
                    ]
                ),
            }
