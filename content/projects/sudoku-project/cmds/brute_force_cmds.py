from lib.typer_cli import TyperCLI
from lib.brute_force import BruteForce


brute_force = TyperCLI.new()


@brute_force.command()
def start():
    """
    Starts the sudoku solver with the Brute Force strategy.
    """
    BruteForce().start()
