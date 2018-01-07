# cannon_nn

## Install requirements
`pip install -r requirements.txt`

## Preparing data
The Vasa cannon Doppler radar data comes in the form of Excel workbooks, but for convenience, our scripts assume the data is in `csv` format. `mkcsv.py` will turn the files into `csv` format and normalize the data.1j

## Training
`python dnn.py`

## Usage
There is a handy widget to visualize r(t) and v(t) in `NN_Graphs.ipynb`. This can be accessed with jupyter-notebook.
