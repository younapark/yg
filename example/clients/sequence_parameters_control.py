from PyQt4 import QtGui, QtCore, Qt
from PyQt4.QtCore import pyqtSignal
from connection import connection
from twisted.internet.defer import inlineCallbacks
import numpy as np
import json
from client_tools import NeatSpinBox

class ParameterRow(QtGui.QWidget):
    def __init__(self, configuration):
        QtGui.QDialog.__init__(self)
        self.loadControlConfiguration(configuration)
        self.populateGUI()

    def loadControlConfiguration(self, configuration):
        for key, value in configuration.__dict__.items():
            setattr(self, key, value)
    
    def populateGUI(self):
        self.nameBox = QtGui.QLineEdit()
        self.nameBox.setFixedSize(self.boxWidth, self.boxHeight)
        self.valueBox = NeatSpinBox()
        self.valueBox.setFixedSize(self.boxWidth, self.boxHeight)
        self.valueBox.display(0)


        self.layout = QtGui.QHBoxLayout()
        self.layout.addWidget(self.nameBox)
        self.layout.addWidget(self.valueBox)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

class ParameterControl(QtGui.QGroupBox):
    hasNewValue = False
    free = True

    def __init__(self, configuration, reactor, cxn=None):
        QtGui.QDialog.__init__(self)
        self.reactor = reactor
        self.cxn = cxn
        self.loadControlConfiguration(configuration)
        self.connect()

    def loadControlConfiguration(self, configuration):
        self.configuration = configuration
        for key, value in configuration.__dict__.items():
            setattr(self, key, value)

    @inlineCallbacks
    def connect(self):
        if self.cxn is None:
            self.cxn = connection()
            yield self.cxn.connect()
        self.context = yield self.cxn.context()
        try:
            self.populateGUI()
            yield self.connectSignals()
        except Exception, e:
            print e
            self.setDisabled(True)

    @inlineCallbacks
    def getServerConfiguratiom(self):
        yield None

    def populateGUI(self):
        self.parameterRows = [ParameterRow(self.configuration) 
                for i in range(self.numRows)]

        self.layout = QtGui.QVBoxLayout()
        for pr in self.parameterRows:
            self.layout.addWidget(pr)
        self.layout.setSpacing(1)
        self.layout.setContentsMargins(0, 0, 0, 0)
        
        self.setFixedSize(2*(self.boxWidth+2), self.numRows*(self.boxHeight+2))
        self.setLayout(self.layout)

    @inlineCallbacks
    def connectSignals(self):
        server = yield self.cxn.get_server(self.servername)
        yield server.signal__parameters_updated(self.update_id)
        yield server.addListener(listener=self.receive_update, source=None,
                                 ID=self.update_id)
        yield self.cxn.add_on_connect(self.servername, self.reinit)
        yield self.cxn.add_on_disconnect(self.servername, self.disable)

        for pr in self.parameterRows:
            pr.nameBox.returnPressed.connect(self.do_update)
            pr.valueBox.returnPressed.connect(self.writeValue(pr))
    
    @inlineCallbacks
    def receive_update(self, c, signal):
        if signal:
            yield self.do_update()

    @inlineCallbacks
    def do_update(self):
            server = yield self.cxn.get_server(self.servername)
#            parameters_json = yield server.get_current_sequence_parameters()
            parameters_json = yield server.set_parameters()
            parameters = json.loads(parameters_json)[self.device]
            for pr in self.parameterRows:
                parameterName = str(pr.nameBox.text())
                if parameterName in parameters.keys():
                    pr.valueBox.display(parameters[parameterName])

    def writeValue(self, parameterRow):
        @inlineCallbacks
        def wv():
            name = str(parameterRow.nameBox.text())
            value = float(parameterRow.valueBox.value())
            server = yield self.cxn.get_server(self.servername)
            #yield server.update_sequence_parameters(json.dumps({name: value}))
            yield server.update_parameters(json.dumps({self.device: {name: value}}))
            parameterRow.valueBox.display(value)
        return wv

    @inlineCallbacks	
    def reinit(self): 
        self.setDisabled(False)
        server = yield self.cxn.get_server(self.servername)
        yield server.signal__parameters_updated(self.update_id, context=self.context)
        yield server.addListener(listener=self.receive_update, source=None,
                                 ID=self.update_id, context=self.context)

    def disable(self):
        print 'oh no!'
        self.setDisabled(True)


    def closeEvent(self, x):
        self.reactor.stop()

if __name__ == '__main__':
    import sys
    a = QtGui.QApplication([])
    import qt4reactor
    qt4reactor.install()
    from twisted.internet import reactor
    from sequence_parameters_config import ControlConfig
    widget = ParameterControl(ControlConfig(), reactor)
    widget.show()
    reactor.run()
