# src/memphisdrip/cli_utils.py
from __future__ import annotations

def typer_resolve_arg_flag_pairs(pos: Optional[str], flag: Optional[str], default: str = None) -> str:
    """Generic resolver for any argument that can be a flag or positional."""
    try:
        import typer
    except:
        warn_missing_typer()
    val = flag or pos or default
    if val is None:
        raise typer.BadParameter("Value must be provided as an argument or flag.")
    return val

def warn_missing_typer():
    print("typer is not installed. Run: pip install 'memphisdrip[typer]'")
