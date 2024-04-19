# Getting Started with Jupyter Notebooks in Visual Studio Code

Visual Studio Code (VS Code) provides support for Jupyter Notebooks, allowing you to write and execute Python code in an interactive environment. If you are familiar with R, this environment can make it easier to transition to Python.

## Extensions

First, you need to install the necessary extensions, search for and add these two extensions  in VS Code to work with Python and Jupyter notebooks:

- **Python Extension**: Adds rich support for the Python language to VS Code.
- **Jupyter Extension**: Enables Jupyter notebook support within VS Code.

## Selecting the Python Interpreter (If you haven't already)

VS Code needs to know which Python interpreter to use:

1. Open the command palette with `Ctrl + Shift + P`.
2. Type `Python: Select Interpreter` and choose the version you installed earlier.

## Preparing the Environment

Before running any Jupyter notebooks, make sure to install `ipykernel`, we'll also use `matplotlib` and `numpy`:

```bash
pip install -U ipykernel, matplotlib, numpy
```

## Creating a Project

1. **Create a new folder** for your demo project to keep your workspace organized.

## Creating and Running a Jupyter Notebook

1. Open the command palette with `Ctrl + Shift + P`.
2. Type `Jupyter: Create New Blank Notebook` — this will open a new notebook in VS Code.
3. In the top right corner, select the kernel (Python version) you installed earlier.

## Working with Notebooks

- **Add Cells**: Use cells to write and execute Python code in small, manageable chunks.
- **Data Visualization**: With matplotlib you can even generate visualizations within the notebook itself

## Converting Notebook to Python Script

To transition from an experimental phase to a more structured Python script:

1. Click the `...` in the notebook's top toolbar.
2. Select `Export` and then `Export to Python Script`.

## Conclusion

By following these steps, you can leverage the power of Jupyter notebooks within VS Code for data analysis and then transition smoothly to a standard Python script for more structured projects. This workflow supports both exploratory data analysis and production-ready code development.
