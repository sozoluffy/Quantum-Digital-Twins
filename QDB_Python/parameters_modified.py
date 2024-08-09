# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

#this is the code altered from the originals. author: Soronzonbold Otgonbaatar

"""
Functions to extract device error parameters from backend properties.
"""

from numpy import inf
import csv

import datetime

# Time and frequency unit conversions
_NANOSECOND_UNITS = {"s": 1e9, "ms": 1e6, "µs": 1e3, "us": 1e3, "ns": 1}
_GHZ_UNITS = {"Hz": 1e-9, "KHz": 1e-6, "MHz": 1e-3, "GHz": 1, "THz": 1e3}

def coupling_map_list(backend, backendName, path):
    # Get coupling map from backend
    coupling_map = backend.configuration().coupling_map

    # write into a csv file
    date_string = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    file_name = str(backendName)+'_'+date_string+'_'+'coupling_map.csv'
    dir_name = path/file_name
    with open(dir_name, 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        writer.writerows([coupling_map])

    return dir_name

def basis_gates_list(backend, backendName, path):
    basis_gates = backend.operation_names
    # write into a csv file
    date_string = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    file_name = str(backendName)+'_'+date_string+'_'+'basis_gates.csv'
    dir_name = path/file_name
    with open(dir_name, 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        writer.writerows([basis_gates])

    return dir_name

def gate_param_values(properties, backendName, path):
    """
    Return parameter error values from a devices BackendProperties.

    Args:
        properties (BackendProperties): device backend properties

    Returns:
        list: A list of tuples ``(name, qubits, time, error)``. If gate
        error or gate_length information is not available ``None``
        will be returned for value.
    """
    values = []
    for gate in properties.gates:
        name = gate.gate
        qubits = gate.qubits
        # Check for gate time information
        gate_length = None  # default value
        time_param = _check_for_item(gate.parameters, "gate_length")
        if hasattr(time_param, "value"):
            gate_length = time_param.value
            if hasattr(time_param, "unit"):
                # Convert gate time to ns
                gate_length *= _NANOSECOND_UNITS.get(time_param.unit, 1)
        # Check for gate error information
        gate_error = None  # default value
        error_param = _check_for_item(gate.parameters, "gate_error")
        if hasattr(error_param, "value"):
            gate_error = error_param.value
        values.append((name, qubits, gate_length, gate_error))
     
    # write into a csv file
    date_string = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    file_name = str(backendName)+'_'+date_string+'_'+'gate_param_values.csv'
    dir_name = path/file_name
    with open(dir_name, 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        writer.writerows(values)

    return dir_name


def gate_error_values(properties, backendName, path):
    """
    Return gate error values from a devices BackendProperties.

    Args:
        properties (BackendProperties): device backend properties

    Returns:
        list: A list of tuples ``(name, qubits, value)``. If gate
        error information is not available ``None`` will be returned
        for value.
    """
    values = []
    for gate in properties.gates:
        name = gate.gate
        qubits = gate.qubits
        value = None  # default value
        params = _check_for_item(gate.parameters, "gate_error")
        if hasattr(params, "value"):
            value = params.value
        values.append((name, qubits, value))
        
    # write into a csv file
    date_string = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    file_name = str(backendName)+'_'+date_string+'_'+'gate_error_values.csv'
    dir_name = path/file_name
    with open(dir_name, 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        writer.writerows(values)
        
    return dir_name


def gate_length_values(properties, backendName, path):
    """
    Return gate length values from a devices BackendProperties.

    Args:
        properties (BackendProperties): device backend properties

    Returns:
        list: A list of tuples ``(name, qubits, value)``. If gate length
        information is not available ``None`` will be returned for value.

    Additional Information:
        Gate length values are returned in nanosecond (ns) units.
    """
    values = []
    for gate in properties.gates:
        name = gate.gate
        qubits = gate.qubits
        value = None  # default value
        params = _check_for_item(gate.parameters, "gate_length")
        if hasattr(params, "value"):
            value = params.value
            if hasattr(params, "unit"):
                # Convert gate time to ns
                value *= _NANOSECOND_UNITS.get(params.unit, 1)
        values.append((name, qubits, value))
        
    # write into a csv file
    date_string = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    file_name = str(backendName)+'_'+date_string+'_'+'gate_length_values.csv'
    dir_name = path/file_name
    with open(dir_name, 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        writer.writerows(values)
        
    return dir_name


def readout_error_values(properties, backendName, path):
    """
    Return readout error values from a devices BackendProperties.

    Args:
        properties (BackendProperties): device backend properties

    Returns:
        list: A list of readout error values for qubits. If readout
        error information is not available None will be returned
        for value.
    """
    values = []
    for qubit_props in properties.qubits:
        value = None  # default value

        params_roerror = _check_for_item(qubit_props, "readout_error")
        params_m1p0 = _check_for_item(qubit_props, "prob_meas1_prep0")
        params_m0p1 = _check_for_item(qubit_props, "prob_meas0_prep1")

        if hasattr(params_m1p0, "value") and hasattr(params_m0p1, "value"):
            value = [params_m1p0.value, params_m0p1.value]
        elif hasattr(params_roerror, "value"):
            value = [params_roerror.value, params_roerror.value]
        values.append(value)
        
    # write into a csv file
    date_string = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    file_name = str(backendName)+'_'+date_string+'_'+'readout_error_values.csv'
    dir_name = path/file_name
    with open(dir_name, 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        writer.writerows(values)
        
    return dir_name


def thermal_relaxation_values(properties, backendName, path):
    """
    Return  T1, T2 and frequency values from a devices BackendProperties.

    Args:
        properties (BackendProperties): device backend properties

    Returns:
        list: A list of tuples ``(T1, T2, freq)`` for each qubit in the device.
        If :math:`T_1`, :math:`T_2`, or frequency cannot be found for qubit a
        value of ``Numpy.inf`` will be used.

    Additional Information:
        :math:`T_1` and :math:`T_2` values are returned in nanosecond
        (ns) units and frequency is returned in gigahertz (GHz) units
        if ``unit`` for each ``value`` is provided in ``properties``.
        Otherwise, the raw values (in unknown original units) are returned.
    """
    values = []
    for qubit_props in properties.qubits:
        # pylint: disable=invalid-name
        # Default values
        t1, t2, freq = inf, inf, inf

        # Get the readout error value
        t1_params = _check_for_item(qubit_props, "T1")
        t2_params = _check_for_item(qubit_props, "T2")
        freq_params = _check_for_item(qubit_props, "frequency")

        # Load values from parameters
        if hasattr(t1_params, "value"):
            t1 = t1_params.value
            if hasattr(t1_params, "unit"):
                # Convert to nanoseconds
                t1 *= _NANOSECOND_UNITS.get(t1_params.unit, 1)
        if hasattr(t2_params, "value"):
            t2 = t2_params.value
            if hasattr(t2_params, "unit"):
                # Convert to nanoseconds
                t2 *= _NANOSECOND_UNITS.get(t2_params.unit, 1)
        if hasattr(freq_params, "value"):
            freq = freq_params.value
            if hasattr(freq_params, "unit"):
                # Convert to Gigahertz
                freq *= _GHZ_UNITS.get(freq_params.unit, 1)

        values.append((t1, t2, freq))
    #write into a csv file
    date_string = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    file_name = str(backendName)+'_'+date_string+'_'+'thermal_relaxation_values.csv'
    dir_name = path/file_name
    with open(dir_name, 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        writer.writerows(values)
        
    return dir_name

def _check_for_item(lst, name):
    """Search list for item with given name."""
    filtered = [item for item in lst if item.name == name]
    if not filtered:
        return None
    else:
        return filtered[0]
