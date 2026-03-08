"""
Parallel experiment runner using multiprocessing.

This utility enables running multiple benchmark experiments in parallel to reduce
total execution time. It reads a shell script containing experiment commands
(one per line) and executes them concurrently using a process pool.

Useful for running the same BO solver across multiple functions, seeds, and
latent dimensions without waiting for sequential completion.

Example:
    # Create a batch.sh with multiple experiment commands
    # Then run:
    python -m hdbo_benchmark.experiments.pool batch.sh 8
    
    This will execute all commands in batch.sh using 8 parallel processes.
"""

import subprocess
from multiprocessing import Pool

import click


def run(line: str):
    """
    Execute a single command in a subprocess.
    
    Args:
        line: Shell command to execute
    """
    subprocess.run(line, shell=True)


@click.command()
@click.argument("script_file", type=click.Path(exists=True))
@click.argument("num_processes", type=int)
def run_parallel(script_file, num_processes):
    """
    Run commands from a script file in parallel using multiprocessing.
    
    Each non-empty line in the script file is treated as a separate command
    and executed in a process pool. This is useful for running multiple
    benchmark experiments concurrently.
    
    Args:
        script_file: Path to shell script containing commands (one per line)
        num_processes: Number of parallel processes to use
        
    Example:
        python pool.py experiments.sh 4
    """
    # Read the script file
    with open(script_file, "r") as file:
        script = file.read()

    # Split the script into lines and filter empty lines
    lines = [line.strip() for line in script.split("\n") if line.strip()]

    # Create a pool of processes and map run function to all lines
    with Pool(processes=num_processes) as pool:
        pool.map(run, lines)


if __name__ == "__main__":
    run_parallel()
