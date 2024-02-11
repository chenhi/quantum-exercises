from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import qiskit.quantum_info as qi		# For converting the circuit to a matrix (testing)
import qiskit.circuit.library as qlib


from qiskit.primitives import Sampler
from qiskit.visualization import plot_histogram, plot_distribution

import matplotlib.pyplot as plt
import math

from qft import getQFT
from phase_est import phaseEst


def testQFT(n):
	r = QuantumRegister(n)
	c = QuantumCircuit(r)
	c.append(getQFT(n), r)
	x = qi.Operator(c)
	print("My QFT circuit:\n", c)
	c1 = c.decompose()
	print("Decomposed:\n", c1)
	c2 = c1.decompose()
	print("Decomposed:\n", c2)
	
	print("Matrix:\n", x)

	#o = c.decompose();
	#print(o)

	#p = c.to_instruction()
	#print(p)

	from qiskit.circuit.library import QFT

	d = QuantumCircuit(r)
	d.compose(QFT(n), inplace=True)
	y = qi.Operator(d)

#	print("Library QFT:\n", d)
	print("Library QFT:\n", y)

	print("\nCHECK!\nDifference should be 0:\n", x-y)

	s = QuantumRegister(n)
	d = QuantumCircuit(s)
	d.append(getQFT(n, inv=True), s)
	
	

	print("My inverse QFT:\n", d)
	y = qi.Operator(d)
	print("Matrix:\n", y)

	d = QuantumCircuit(r)
	d.compose(QFT(n, inverse=True), inplace=True)
	z = qi.Operator(d)

#	print("Library inverse QFT:\n", d)
	print("Library inverse QFT:\n", z)

	print("\nCHECK!\nDifference should be 0:\n", y - z)


	print("\nCHECK!\nThis should be the identity: \n", x @ y)
	

def testPhaseEst():
	# Test Hadamard gate
	print("\n\nTesting estimator on Hadamard gate:")
	op = qlib.HGate()
	c = phaseEst(op, [1,1*math.sqrt(2)-1], 3)
	print(c)
	results = Sampler().run(c).result()
	statistics = results.quasi_dists[0].binary_probabilities()
	print("\nCHECK!\nThis should be 000:", statistics)

	c = phaseEst(op, [1,-1*math.sqrt(2)-1], 3)
	print(c)
	results = Sampler().run(c).result()
	statistics = results.quasi_dists[0].binary_probabilities()
	print("\nCHECK!\nThis should be 100:", statistics)			# I.e. eigenvalue -1, so tau * 1/2, and note the digits are reversed
	
	# Test phase gate
	print("\n\nTesting estimator on phase gate: ")
	#m  = 7
	#n = 3
	n = int(input("Input denominator power of 2: "))
	m = float(input("Input numerator:"))
	th=m/2.0**n								# Set the phase in [0, 1)
	print("Theta:", th, "=", str(m)+"/2^"+str(n))
	op = qlib.PhaseGate(math.tau * th)
	
	c = phaseEst(op, [0,1], n)
	print(c)

	results = Sampler().run(c).result()
	statistics = results.quasi_dists[0].binary_probabilities()
	print("\nCHECK:\nThis should be", m, "mod 2^" + str(n), "in binary:", statistics)

	# To show the plots; not needed	
	#plot_distribution(statistics)
	#plt.show()

#testQFT(3)

testPhaseEst()




