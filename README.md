# cannon_nn

## Install requirements
`pip install -r requirements.txt`

## Preparing data
The Vasa cannon Doppler radar data comes in the form of Excel workbooks, but for convenience, our scripts assume the data is in `csv` format. Run `convert.py` to convert the `xlsx` folders in `test/` and `train/` to `csv`.

`./convert.py test training`

For more information on `convert.py`, consult the [module docstring](https://github.com/h313/cannon_nn/blob/master/convert.py#L1-L21)

## Training
`python dnn.py`
