from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import numpy

# Returns a QFT circuit, input is a list of qubits
def getQFT(qs):
	if len(qs) == 0:
		return QuantumCircuit(0)
	regs = QuantumRegister(bits=qs)
	n = len(qs)
	out = QuantumCircuit(regs)
	
	if n == 1:
		out.h(0)
		return out
	
	out.append(getQFT(regs[1:]), regs[1:])
	for k in range(1, n):
		out.cp(2.0 * numpy.pi / numpy.power(2.0, n) * numpy.power(2.0, k-1), 0, k)			# Conditional phase change the kth register (k = 1, ..., n-1) by 2 pi i * (2^{k-1}/2^n)
	out.h(0)
	
	# Cycle the nth register to the 1st register
	out.swap(0, n-1)
	for j in range(0, n-2):
		out.swap(j, j+1)
	return out
	
	
def getInvQFT(qs):
	if len(qs) == 0:
		return QuantumCircuit(0)
	regs = QuantumRegister(bits=qs)
	n = len(qs)
	out = QuantumCircuit(regs)
	
	if n == 1:
		out.h(0)
		return out
	
	out.append(getInvQFT(regs[1:]), regs[1:])
	for k in range(1, n):
		out.cp(-2.0 * numpy.pi / numpy.power(2.0, n) * numpy.power(2.0, k-1), 0, k)			# Conditional phase change the kth register (k = 1, ..., n-1) by 2 pi i * (2^{k-1}/2^n)
	out.h(0)
	
	# Cycle the nth register to the 1st register
	out.swap(0, n-1)
	for j in range(0, n-2):
		out.swap(j, j+1)
	return out
