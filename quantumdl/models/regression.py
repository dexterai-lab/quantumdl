import cirq
from quantumdl.core.engine import QDLengine

class Regression(object):
    """This class defines methods for performing regression tasks."""

    def __init__(self):
        self.regression_type = None


    def Liner(self, qbits=None):
        """Defines a Quantun Liner Regressor"""
        # Pick a qubit.

        qubit = cirq.GridQubit(0, 0)

        cirq.append([cirq.H(qbits[0]), cirq.CNOT(qbits[0], qbits[1])])
        cirq.append([cirq.measure(qbits[0]), cirq.measure(qbits[1])])

        # Create a circuit
        circuit = cirq.Circuit(
            cirq.X(qubit) ** 0.5,  # Square root of NOT.
            cirq.measure(qubit, key='m')  # Measurement.
        )
        print("Circuit:")
        print(circuit)

    def main(self,__name__):
        pass

    if __name__ == '__main':
        main()