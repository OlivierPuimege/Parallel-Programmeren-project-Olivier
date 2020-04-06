# -*- coding: utf-8 -*-
"""
Package parallel_programmeren_project_olivier
=======================================

A 'hello world' example.
"""
__version__ = "0.4.0"

try:
    import parallel_programmeren_project_olivier.lva
except ModuleNotFoundError as e:
    # Try to build this binary extension:
    from pathlib import Path
    import click
    from et_micc_build.cli_micc_build import auto_build_binary_extension
    msg = auto_build_binary_extension(Path(__file__).parent, 'lva')
    if not msg:
        import parallel_programmeren_project_olivier.lva
    else:
        click.secho(msg, fg='bright_red')

try:
    import parallel_programmeren_project_olivier.lijstvanatomen
except ModuleNotFoundError as e:
    # Try to build this binary extension:
    from pathlib import Path
    import click
    from et_micc_build.cli_micc_build import auto_build_binary_extension
    msg = auto_build_binary_extension(Path(__file__).parent, 'lijstvanatomen')
    if not msg:
        import parallel_programmeren_project_olivier.lijstvanatomen
    else:
        click.secho(msg, fg='bright_red')



try:
    import parallel_programmeren_project_olivier.bar
except ModuleNotFoundError as e:
    # Try to build this binary extension:
    from pathlib import Path
    import click
    from et_micc_build.cli_micc_build import auto_build_binary_extension
    msg = auto_build_binary_extension(Path(__file__).parent, 'bar')
    if not msg:
        import parallel_programmeren_project_olivier.bar
    else:
        click.secho(msg, fg='bright_red')

try:
    import parallel_programmeren_project_olivier.foo
except ModuleNotFoundError as e:
    # Try to build this binary extension:
    from pathlib import Path
    import click
    from et_micc_build.cli_micc_build import auto_build_binary_extension
    msg = auto_build_binary_extension(Path(__file__).parent, 'foo')
    if not msg:
        import parallel_programmeren_project_olivier.foo
    else:
        click.secho(msg, fg='bright_red')


def hello(who='world'): #Laten staan voor debug
    """'Hello world' method.

    :param str who: whom to say hello to
    :returns: a string
    """
    result = "Hello " + who
    return result


# eof
