# fuzzylab
Python Fuzzy Logic library based on Octave fuzzy-logic-toolkit

The way to use the fuzzylab functions is based on Matlab R2018b Fuzzy Logic Toolbox functions.

## Install

```
pip install -U fuzzylab
```

## Use

In the folder [notebooks](https://github.com/ITTcs/fuzzylab/tree/master/notebooks) exists notebook examples, for a starting point to the library.

In all the notebooks it is initialized installing the fuzzylab library with 

```
!pip install -U fuzzylab
```

that use `!` for execute terminal commands in the cell.

For plot in the notebook with the matplotlib library it is necessary to specify it with

```
%matplotlib inline
```

Now you can import the fuzzy library with

```
from fuzzylab import *
```

## Example

```python
import numpy as np
from matplotlib.pyplot import *
from fuzzylab import *

x = np.linspace(0, 10, 101)
y = trimf(x, [3, 6, 8])
plot(x, y)
xlabel('trimf, P = [3, 6, 8]')
show()
```

![trimf](https://raw.githubusercontent.com/ITTcs/fuzzylab/master/images/trimf.png)
