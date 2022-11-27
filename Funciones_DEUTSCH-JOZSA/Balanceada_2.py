from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
import matplotlib.pyplot as plt

"========================= Funciones Deutsch - Jozsa (Balanceada 2) ========================="

simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(5, 5)

circuit.cx(2, 4)


circuit.measure([0,1,2,3,4], [4,3,2,1,0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
M=[]
for i in range(32):
    M.append([0]*32)
n=0
for j in M:
    M[n][n]=1
    print(M[n])
    n+=1
print("\nTotal count for 00 and 11 are:", counts)
print(circuit)
plot_histogram(counts)
plt.show()

"Prueba con 01000"
simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(5, 5)
circuit.x(1)

circuit.cx(2, 4)


circuit.measure([0,1,2,3,4], [4,3,2,1,0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:", counts)
print(circuit)
plot_histogram(counts)
plt.show()

"Prueba con 00100"
simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(5, 5)
circuit.x(2)

circuit.cx(2, 4)


circuit.measure([0,1,2,3,4], [4,3,2,1,0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:", counts)
print(circuit)
plot_histogram(counts)
plt.show()

"Prueba con 00010"
simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(5, 5)
circuit.x(3)

circuit.cx(2, 4)


circuit.measure([0,1,2,3,4], [4,3,2,1,0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:", counts)
print(circuit)
plot_histogram(counts)
plt.show()

"Prueba con 00001"
simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(5, 5)
circuit.x(4)

circuit.cx(2, 4)


circuit.measure([0,1,2,3,4], [4,3,2,1,0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:", counts)
print(circuit)
plot_histogram(counts)
plt.show()