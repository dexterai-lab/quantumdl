from quantumdl.core.engine import *
from quantumdl.circuits.qcircuit import *

import cirq


class Simulator(object):
    """Quantum Engine Simulator"""

    def __init__(self, **kwargs):
        self.circuit = engine

    def main(self, circuit):
        # Simulate the circuit several times.
        simulator = cirq.Simulator()
        result = simulator.run(circuit, repetitions=20)
        print("Results:")
        print(result)


if __name__ == '__main__':
    main(self, circuit)
