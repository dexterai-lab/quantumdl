import cirq
from quantumdl.core.engine import QDLengine

# Pick a qubit.
qubit = cirq.GridQubit(0, 0)

# Create a circuit
circuit = cirq.Circuit(
    cirq.X(qubit)**0.5,  # Square root of NOT.
    cirq.measure(qubit, key='m')  # Measurement.
)
print("Circuit:")
print(circuit)

# Simulate the circuit several times.
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=20)
print("Results:")
print(result)

class Regression(object):
    """This class defines methods for performing regression tasks."""

    def __init__(self):
        self.regression_type = None


    def Liner(self, condition):
        """Defines a Quantun Liner Regressor"""


    def main(self,__name__):
        pass

    if __name__ == '__main':
        main()