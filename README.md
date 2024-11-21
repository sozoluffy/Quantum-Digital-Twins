# **Quantum Digital Twins**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)

---

## **Overview**

This is a code for generating quantum databse (or quantum digital twins) by extracting quantum machine data from IBM quantum computers (open access) and deploying your quantum circuit models on quantum digital twins. Quantum Digital Twins (QDTs) bring the power of quantum computing into the realm of real-world problems. This project leverages quantum-enhanced models to build digital twins that can simulate, optimize, and predict the behavior of complex physical systems, with potential applications in manufacturing, Earth observation, healthcare, energy, and more.

---

## **Features**

- **Technical advantages:**
1. It is local and fast for benchmarking noisy quantum computers.
2. It is versioned based on timestamp. Hence, you know your data values. IBM calibration wont affect your quantum data. 
3. It is a real quantum device database.
4. It works even if the IBM server is down.
5. There is no waiting time in the queue on IBM servers.

- **Scientific advantages:**
1. Investigate error mitigation techniques on quantum digital twins than on quantum physical systems.
2. Investigate sources of noise and decoherence and propose mitigation strategies.
3. Analyze the impact of noisy quantum computers on your use cases.
4. Analyze experimental data and draw meaningful conclusions to guide quantum system improvements.

---

## **Getting Started**

### Prerequisites
- **Python 3.8 or later**  
- **Quantum Computing Framework**: [Qiskit](https://qiskit.org/) or [PennyLane](https://pennylane.ai/)
- **Other Dependencies**: See the [environment.yml](environment.yml) for creating a conda environment and [requirements.txt](requirements.txt) files.   

---

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/sozoluffy/Quantum-Digital-Twins.git
   cd Quantum-Digital-Twins
   ```

2. Install dependencies:
   ```bash
   conda env create -f environment.yml 
   ```
Note that the code is constantly updated and improved. We are also preparing quantum databases for Ion Trap, NV Center, Neutral Atoms, and Silicon Qubits. So please regularly pull.
PS: ibm_osaka is down from IBM Quantum, but they launched ibm_kyiv. The ibm_osaka database exists in QuantumDatabase_v1 to QuantumDatabase_v5. Starting from QuantumDatabase_v6, ibm_osaka database is no longer available but ibm_kyiv.   

---

## **Applications**
**Toy Examples for Writing and Reading Quatum Device Database**
**Hybrid Quantum-Classical Models**
**Quantum Circuit Knitting**

---

## **Article**
If you use this code in your research or in your study then we would appreciate in citing the related work:
https://arxiv.org/abs/2410.23311

---

## **License**

This project is licensed under the MIT License. 
