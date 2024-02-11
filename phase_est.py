from qft import getQFT, getInvQFT


from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import qiskit.quantum_info as qi		# For converting the circuit to a matrix (testing)


# U is a gate, precision is the number of digits to estimate
def phaseEst(u, precision):
	topregs = QuantumRegister(precision)
	output = QuantumCircuit[topregs + u.qubits]
	output.h(topregs)
	poweru = u
	for i in range(0, precision):
		output.append(poweru) #????? append a UCGate?
		# errmmm
	
	
