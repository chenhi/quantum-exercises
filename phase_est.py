from qft import getQFT
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit.library import QFT

# U is a Gate, eigvec is a Statevector or List, precision is the number of digits to estimate
# Returns a circuit
def phaseEst(u, eigvec, precision):
	# Set up the registers
	topregs = QuantumRegister(precision)
	botregs = QuantumRegister(u.num_qubits)			
	meas = ClassicalRegister(precision)
	output = QuantumCircuit(topregs[:] + botregs[:] + meas[:])
	
	# Initialize the eigenvector
	output.initialize(eigvec, botregs[:], normalize=True)
	
	# Build the circuit
	output.h(topregs)
	poweru = u
	for i in range(0, precision):
		output.append(poweru.control(1), [topregs[i]] + botregs[:])
		poweru = poweru.repeat(2)						# In practice... is this what we want?
	output.append(getQFT(precision, inv=True), topregs[:])			# My implementation of QFT has some issue.  For now, use the built-in one.
	#output.append(QFT(precision, inverse=True), topregs[:])
	output.measure(topregs, meas)
	
	return output

# The registers can be recovered by taking output.qubits and output.clbits.  For the qubits, the top (first) registers are the measured ones and the bottom (last) are the eigenvector.
