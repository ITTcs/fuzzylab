import numpy as np

class fisrule:
    def __init__(self, rule_def, *varargin):
        numInputs = varargin[0]

        self.Description = 'description no available'
        self.Antecedent = rule_def[:numInputs]
        self.Consequent = rule_def[numInputs:-2]
        self.Weight = rule_def[-2]
        self.Connection = rule_def[-1]

        assert np.count_nonzero(self.Antecedent) > 0, 'Rule antecedent must have at least one nonzero membership function index.'
        assert np.count_nonzero(self.Consequent) > 0, 'Rule consequent must have at least one nonzero membership function index.'
