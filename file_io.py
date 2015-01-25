"""
Module provides methods for reading and writing sim data to and from log files
"""

__author__ = 'Andy'

import shelve
from config import LOG_FILE


def read_db(sim_name):
    """
    Reads sim data from the log file

    :param sim_name: The name of the simulation as stored in the log file
    :type sim_name: str
    :return: The simulation data in dictionary form
    :rtype: dict
    """
    d = shelve.open(LOG_FILE)
    print d.keys()
    sim_dict = d[sim_name]
    d.close()
    return sim_dict


def export_dict(path_dict, sim_name):
    """
    Writes sim data to the log file

    Stored the path_dict under the key sim_name

    :param path_dict: The simulation data in dictionary form
    :type path_dict: dict
    :param sim_name: The name of the simulation
    :type sim_name: str
    :return: None
    """
    # print path_dict.keys()

    #print "Writing Sim Data to File"
    d = shelve.open(LOG_FILE)
    d[sim_name] = path_dict
    d.close()