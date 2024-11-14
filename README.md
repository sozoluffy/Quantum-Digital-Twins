# Quantum-Digital-Twins

This is a code for generating quantum databse (or quantum digital twins) by extracting quantum machine data from IBM quantum computers (open access) and deploying your quantum circuit models on quantum digital twins. There are several advantages:

Technical advantages:
1. It is local and fast for benchmarking noisy quantum computers.
2. It is versioned based on timestamp. Hence, you know your data values. IBM calibration wont affect your quantum data. 
3. It is a real quantum device database.
4. It works even if the IBM server is down.
5. There is no waiting time in the queue on IBM servers.

Scientific advantages:
1. Investigate error mitigation techniques on quantum digital twins than on quantum physical systems.
2. Investigate sources of noise and decoherence and propose mitigation strategies.
3. Analyze the impact of noisy quantum computers on your use cases.
4. Analyze experimental data and draw meaningful conclusions to guide quantum system improvements.
   
To use use this code, you can install the python environment: conda env create -f environment.yml (see official conda documentation). Note that the code is constantly updated and improved. We are also preparing quantum databases for Ion Trap, NV Center, Neutral Atoms, and Silicon Qubits. So please regularly pull.

Note that: ibm_osaka is down from IBM Quantum, but they launched ibm_kyiv. The ibm_osaka database exists in QuantumDatabase_v1 to QuantumDatabase_v5. Starting from QuantumDatabase_v6, ibm_osaka database is no longer available but ibm_kyiv.   

If you use this code in your research or in your study then we would appreciate in citing some of our works:
https://arxiv.org/abs/2410.23311

