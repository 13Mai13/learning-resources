import typer
from cmds import brute_force_cmds as BruteForce

sudoku = typer.Typer(
    no_args_is_help=True,
    add_completion=False,
    context_settings={"help_option_names": ["-h", "--help"]},
)
sudoku.add_typer(Api.api, name="api", help="Prediction model API commands")

if __name__ == "__main__":
    sudoku()
