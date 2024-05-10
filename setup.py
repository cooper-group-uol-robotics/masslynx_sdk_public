#!/usr/bin/env python
"""Install MassLynx SDK package."""

import setuptools

from pathlib import Path
from shutil import copy

init_file = """import os
import importlib
import sys
from pathlib import Path

_is_64bits = sys.maxsize > 2**32
if _is_64bits:
    _dll_path = os.path.join(os.path.dirname(__file__), "dlls", "x64")
else:
    _dll_path = os.path.join(os.path.dirname(__file__), "dlls", "Win32")
os.add_dll_directory(_dll_path)

__all__ = []

for module in Path(__file__).parent.glob("*.py"):
    if module.stem != "__init__":
        m = importlib.import_module(f"masslynx.{module.stem}")
        names = [x for x in m.__dict__ if x.startswith("MassLynx")]
        globals().update({k: getattr(m, k) for k in names})
        __all__.extend(names)

"""


if __name__ == "__main__":
    src_path = Path.cwd() / "src" / "masslynx"
    sdk_path = Path("WatersRawSDKRedist")
    src_path.mkdir(exist_ok=True, parents=True)
    dll_path_32bit = src_path / "dlls/Win32"
    dll_path_64bit = src_path / "dlls/x64"

    # Copy DLLs to a project subfolder
    dll_path_32bit.mkdir(exist_ok=True, parents=True)
    dll_path_64bit.mkdir(exist_ok=True, parents=True)
    for dll in (sdk_path / "Win32").glob("*"):
        copy(dll, dll_path_32bit / dll.name)
    for dll in (sdk_path / "x64").glob("*"):
        copy(dll, dll_path_64bit / dll.name)

    for python_file in sdk_path.glob("Python/*.py"):
        filedata = python_file.read_text()

        (src_path / python_file.name).write_text(
            filedata.replace("from MassLynx", "from .MassLynx")
        )

    (src_path / "__init__.py").write_text(init_file)

    setuptools.setup()
