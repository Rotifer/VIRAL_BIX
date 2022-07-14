# Set-up Notes

Repo name: VIRAL_BIX
Ceated a venv in dir _.venv_
Installed Biopython, pandas, the SQL extension (requires SQLAlchemy)


## Installed jupyter-lab



[Using Virtual Environments in Jupyter Notebook and Python](https://janakiev.com/blog/jupyter-virtual-envs/)

I ran the following command and it worked:

```{sh}
pip install ipykernel
python -m ipykernel install --user --name=viralbix
```

When creating a new Notebook, choose the _viralbix_ kernel.
