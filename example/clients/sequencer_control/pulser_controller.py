from yesrgang.example.clients.sequencer_control.sequencer_control.py

    @inlineCallbacks
    def runPulserSeq(self,c,sequence):


        durations = sequence[self.timing_channel]
        channelKeys = self.digital_channels
        # durations= self.durations
        durationSize = len(durations)
        print 'timing_channel in runPulserSeeq', self.timing_channel
        print [sequence[channelKey] for channelKey in channelKeys]
        print sequence[self.timing_channel]
        print self.durations
        pserver = yield self.cxn.get_server('pulser')
        from labrad.units import WithUnit as U
        yield pserver.stop_sequence()
        yield pserver.new_sequence()

        start = 0
        oldDuration = 0.0
        duration = 0

        # print 'dict', [{channelKey:{'order':i,'duration':sequence[channelKey][i]}} for channelKey in channelKeys for i in range(0,durationSize) if sequence[channelKey][i] != 0]
        for i in range(0, durationSize):
            for channelKey in channelKeys:
                if sequence[channelKey][i] != 0:
                    channelName =  self.get_name(channelKey)
                    duration = durations[i] #duration in seconds
                    print 'channelName, start, duration:', channelName, start, duration
                    yield pserver.add_ttl_pulse(channelName,U(float(start),'s'),U(float(duration),'s'))
            start = start + durations[i]


        yield pserver.program_sequence()
        yield pserver.start_number(10)


if __name__ == '__main__':
    from sequencer_config import SequencerConfig
    a = QtGui.QApplication([])
    import qt4reactor
    qt4reactor.install()
    from twisted.internet import reactor
    widget = Sequencer(SequencerConfig(), reactor)
    widget.show()
    reactor.run()
