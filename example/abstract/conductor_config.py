import os
import time

node = os.getenv('LABRADNODE')
sep = os.path.sep

class ConductorConfig(object):
    def __init__(self):
        self.name = '%LABRADNODE%_conductor'
        self.update_id = '689989'
        self.db_write_period = 0 # [s]
        self.data_delay = 10
        self.db_query_str = 'SELECT value FROM "experiment parameters" WHERE \
                "device" = \'sequence\' AND "parameter" = \'{}\' ORDER BY time \
                DESC LIMIT 1'
        self.sequencers = [
                '{}_analog_sequencer'.format(node), 
                '{}_digital_sequencer'.format(node),
        ]
        self.default_sequence = {'digital@T': [1, 5, 1]}
        self.default_devices = {}
        self.data_directory = lambda: '..{}data{}'.format(sep, sep) + time.strftime('%Y%m%d')+sep


        self.digital_servername = '{}_digital_sequencer'.format(node)
        self.analog_servername = '{}_analog_sequencer'.format(node)
