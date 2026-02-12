

__all__ = [
    "typer_resolve_arg_flag_pair"
    "safe_notify"
]



def __getattr__(name):
    if name == "typer_resolve_arg_flag_pair":
        from .cli_utils import typer_resolve_arg_flag_pair
        return typer_resolve_arg_flag_pair
    
    if name == "safe_notify":
        from .notifier import safe_notify
        return safe_notify

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

def __dir__():
    return sorted(__all__ + [
        "__all__", "__builtins__", "__cached__", "__doc__", "__file__",
        "__getattr__", "__loader__", "__name__", "__package__", "__path__", "__spec__"
    ])

