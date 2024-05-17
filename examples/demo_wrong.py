from notebook_wrapper import NotebookWrapper

# Path: examples/demo.py
calculate = NotebookWrapper("./wrong.ipynb", ["a", "b"], ["sum", "div"])

sum, div = calculate(5, 10)

print(f"Sum: {sum}, Div: {div}")
# result: Sum: 3, Div: 0.5
# wrong.ipynb is not in the right format.