from pathlib import Path
from notebook_wrapper import NotebookWrapper

# Path: examples/demo.py
calculate = NotebookWrapper(
    Path(__file__).parent / "demo.ipynb", ["a", "b"], ["sum", "div"]
)

sum, div = calculate(5, 10)

print(f"Sum: {sum}, Div: {div}")
# result: Sum: 15, Div: 0.5
