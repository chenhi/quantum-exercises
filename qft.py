from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import numpy
from math import tau

# Returns a QFT gate, input is a list of qubits
# It's better to return a gate than a circuit, since then we can build a controlled gate, etc.
def getQFT(n, inv=False):
	namestr = str(n)+"-QFT" + ("-inv" if inv==True else "")		# Just the name of the output
	
	regs = QuantumRegister(n)				# I think to build the gate, the only way is still to build a circuit then convert it?
	out = QuantumCircuit(regs)
	if n == 0:
		return out.to_gate(label=namestr)
	if n == 1:
		out.h(0)
		return out.to_gate(label=namestr)
	
	out.append(getQFT(n-1, inv), regs[1:])
	for k in range(1, n):
		out.cp(((-1.0) ** inv) *  tau / numpy.power(2.0, n) * numpy.power(2.0, k-1), 0, k)	# Conditional phase change the kth register (k = 1, ..., n-1) by 2 pi i * (2^{k-1}/2^n)
	out.h(0)
	
	# Cycle the nth register to the 1st register
	out.swap(0, n-1)
	for j in range(0, n-2):
		out.swap(j, j+1)
	#return out
	return out.to_gate(label=namestr)
