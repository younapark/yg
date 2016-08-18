from experiments import *

name = 'scan_rabi_flop'
sequence_name = 'rabi_flop2'

clock_intensity = -5

t_start = 0.0
t_stop = 0.8
n_points = 20

""" should not regularly need to change stuff below here """
times = np.linspace(t_start, t_stop, n_points).tolist()[1:]
parameters = {
    'sequence': {
        '*Trabi': times,
        '*Iclk': clock_intensity,
    },
}

""" set sequence """
import os
import labrad
cxn = labrad.connect()
node = os.getenv('LABRADNODE')
c = getattr(cxn, node + '_conductor')
c.set_sequence(sequence_name)
""" end set sequence """

scan = Scan(
    name=name,
    parameters=parameters,
)

scan.queue(clear_all=True)
