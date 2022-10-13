from simulation.runner import SimulationRunner
from simulation.utils.io import export_configuration, read_configuration
from simulation.configuration import Config 



import time 


if __name__ == "__main__":

    config = Config()
    sim = SimulationRunner(config)
    _start = time.time()
    sim()
    _end = time.time()
    print("Computational time: ", round(_end - _start, 3), "s")
    print("Total trips started: ", sim.total_trips)
    print("Vehicles not arrived to destination: ", sim.failed_trips)
    print("Graph topology problems: ", sim.nx_failed_trips)
    

    