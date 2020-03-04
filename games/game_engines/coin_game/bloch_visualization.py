from qiskit.visualization import plot_bloch_multivector
from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit
from qiskit import execute, BasicAer

def auto_bloch():
# Graphical representation of the Bloch Spheres for the game sequence HXH
    qc = QuantumCircuit(4, 1)
    # Prepare each qubit to visualize the states after each step
    # qc.x(1) would change the initial position of q1 and results in different superposition
    qc.h(1) # Qubit 1 - superposition after H gate
    qc.h(2)
    qc.x(2) # Qubit 2 - superposition after H and X gate (similar after H and iden)
    qc.h(3)
    qc.x(3)
    qc.h(3) # Qubit 3 - result head after H, X and H
    qc.measure([3], [0]) # Measure qubit 3 - would colapse if in s#perposition 
    backend = BasicAer.get_backend('statevector_simulator')
    job = execute(qc, backend).result()
    print ("qubit0: initial position, qubit1: applying H, qubit2: applying X (after H), qubit3: applying H (after X and H)")
    return plot_bloch_multivector(job.get_statevector(qc)) # Visualize quantum states
    
def personal_bloch(moveA1, moveB1, moveA2):
    # Graphical representation of the Bloch Spheres for the game sequence of the player
    qc = QuantumCircuit(4, 1)
    # Prepare each qubit to visualize the states after the according moves
    # 1. move of A
    if   moveA1 == 0 : 
        qc.iden(1)
        qc.iden(2)
        qc.iden(3)
    elif moveA1 == 1 : 
        qc.x(1)
        qc.x(2)
        qc.x(3)
    elif moveA1 == 2 : 
        qc.h(1)
        qc.h(2)
        qc.h(3)
    
    # 1. move of B 
    if   moveB1 == 0 : 
        qc.iden(2)
        qc.iden(3)
    elif moveB1 == 1 : 
        qc.x(2)     
        qc.x(3)
    # 2. move of A
    if   moveA2 == 0 : 
        qc.iden(3)
    elif moveA2 == 1 : 
        qc.x(3) 
    elif moveA2 == 2 : 
        qc.h(3) 
    backend = BasicAer.get_backend('statevector_simulator')
    job = execute(qc, backend).result()
    print('Your moves were: ',moveA1, moveB1, moveA2)
    print('The states of the qubits for this game sequence can be visualized as follows:')
    return plot_bloch_multivector(job.get_statevector(qc)) # Visualize quantum states