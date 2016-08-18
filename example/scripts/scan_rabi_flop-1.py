from experiments import *

name = 'scan_rabi_flop'
sequence_name = 'ygTrabi'

clock_intensity = -5

t_start = 0.0
t_stop = 4
n_points = 2

""" should not regularly need to change stuff below here """
times = np.linspace(t_start, t_stop, n_points).tolist()[1:]
parameters = {
    'sequence': {
        '*Trabi': times,
        '*Iclk': clock_intensity,
    }}

scan = Scan(
    name=name,
    sequence=sequence_name,
    parameters=parameters,
)

scan.queue(clear_all=True)
