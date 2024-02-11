from qft import getQFT


from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import qiskit.quantum_info as qi		# For converting the circuit to a matrix (testing)


n = 3

registers = QuantumRegister(n, "a")
c = QuantumCircuit(registers)
c.append(getQFT(registers[:]))

print(c)
x = qi.Operator(c)
print(x)

#o = c.decompose();
#print(o)

#p = c.to_instruction()
#print(p)

from qiskit.circuit.library import QFT

d = QuantumCircuit(registers)
d.compose(QFT(n), inplace=True)

print(d)
y = qi.Operator(d)
print(y)


print(x-y)

#registers = QuantumRegister(n, "a")
#c = getQFT(registers[:], inverse=True)

#print(c)
#y = qi.Operator(c)
#print(y)

#print("This should be the identity:", x @ y)



