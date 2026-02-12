

__all__ = [
    "typer_resolve_arg_flag_pair"
]



def __getattr__(name):
    if name == "typer_resolve_arg_flag_pair":
        from .cli_utils import typer_resolve_arg_flag_pair
        return typer_resolve_arg_flag_pair
    
    # other, placeholder 
    #if name == "typer_resolve_arg_flag_pair":
    #    from .cli_utils import typer_resolve_arg_flag_pair
    #    return typer_resolve_arg_flag_pair

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

def __dir__():
    return sorted(__all__ + [
        "__all__", "__builtins__", "__cached__", "__doc__", "__file__",
        "__getattr__", "__loader__", "__name__", "__package__", "__path__", "__spec__"
    ])

