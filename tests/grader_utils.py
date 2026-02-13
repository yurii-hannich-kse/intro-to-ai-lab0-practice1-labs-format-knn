import nbformat
from types import ModuleType

def load_notebook_functions(path):
    with open(path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    mod = ModuleType("homework")
    for cell in nb.cells:
        if cell.cell_type == 'code':
            try:
                exec(cell.source, mod.__dict__)
            except Exception:
                continue
    return mod