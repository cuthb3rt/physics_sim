import os

N_DIMS = 3
DELTA_T = 5

OUTPUT_DIR = os.path.abspath("%s/log" % os.path.dirname(__file__))
LOG_FILE = "%s/sim_log.txt" % OUTPUT_DIR