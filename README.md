# fuzzylab
Python Fuzzy Logic library based on Octave Fuzzy Logic Toolkit, considered as a mostly MATLAB-compatible fuzzy logic toolkit for Octave.

The way to use the fuzzylab functions is based on Matlab R2019a Fuzzy Logic Toolbox functions.


## Research work

[Fuzzy Logic Controller with Fuzzylab Python Library and the Robot Operating System for Autonomous Robot Navigation: A Practical Approach](https://doi.org/10.1007/978-3-030-35445-9_27)

## Installation

```
pip install fuzzylab
```

## Usage

In the folder [notebooks](https://github.com/ITTcs/fuzzylab/tree/master/notebooks) there are notebook examples, for a starting point of the library.

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

## Citing fuzzylab

    @Inbook{Avelar2020,
      author="Avelar, Eduardo
      and Castillo, Oscar
      and Soria, Jos{\'e}",
      editor="Castillo, Oscar
      and Melin, Patricia
      and Kacprzyk, Janusz",
      title="Fuzzy Logic Controller with Fuzzylab Python Library and the Robot Operating System for Autonomous Robot Navigation: A Practical Approach",
      bookTitle="Intuitionistic and Type-2 Fuzzy Logic Enhancements in Neural and Optimization Algorithms: Theory and Applications",
      year="2020",
      publisher="Springer International Publishing",
      address="Cham",
      pages="355--369",
      isbn="978-3-030-35445-9",
      doi="10.1007/978-3-030-35445-9_27",
      url="https://doi.org/10.1007/978-3-030-35445-9_27"
    }
