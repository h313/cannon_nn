# cannon_nn

## Description
cannon_nn is a model for the VASA cannon that uses the Keras deep learning library for Python. This model has a verification loss on the scale of 10^-4 on verification data. `dnn.py` contains the code for the neural network and explanations of the choices made. 

### Blame
* Jesse Li: visualization, data organization, code structure
* Haoda Wang: neural network, documentation

### Sources
* [Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980v8)
* [On the Convergence of Adam and Beyond ](https://openreview.net/forum?id=ryQu7f-RZ)
* [Keras: The Python Deep Learning library](https://keras.io/)

## Running the program
### Install requirements
`pip install -r requirements.txt`

### Preparing data
The Vasa cannon Doppler radar data comes in the form of Excel workbooks, but for convenience, our scripts assume the data is in `csv` format. `mkcsv.py` will turn the files into `csv` format and normalize the data.

`python mkcsv.py`

### Training
Training should take a minute or five, depending on your computer.

`python dnn.py`

### Usage
There is a handy widget to visualize r(t) and v(t) in `NN_Graphs.ipynb`. This can be accessed with jupyter notebook.
