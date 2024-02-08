from qft import getQFT, getInvQFT


from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import qiskit.quantum_info as qi		# For converting the circuit to a matrix (testing)


n = 2

registers = QuantumRegister(n, "a")
c = getQFT(registers[:])

print(c)
x = qi.Operator(c)
print(x)


registers = QuantumRegister(n, "a")
c = getInvQFT(registers[:])

print(c)
y = qi.Operator(c)
print(y)

print(x @ y)

print("This was a test.")



