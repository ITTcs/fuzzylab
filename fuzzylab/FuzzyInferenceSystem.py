from .fisvar import fisvar
from .fismf import fismf
from .fisrule import fisrule

import numpy as np

class FuzzyInferenceSystem:
    def __init__(self):
        self.Inputs     = []
        self.Outputs    = []
        self.Rules      = []

    def addInput(self, *varargin, **options):
        self.__addVariable('input', *varargin, **options)


    def addOutput(self, *varargin, **options):
        self.__addVariable('output', *varargin, **options)


    def addMF(self, var_name, *varargin, **options):
        vars_name = [var.Name for var in self.Inputs + self.Outputs]
        var_index = vars_name.index(var_name)
        
        new_mf = fismf(*varargin, Name=options.get('Name'))

        if vars_name.index(var_name) < len(self.Inputs):
            self.Inputs[var_index].MembershipFunctions.append(new_mf)
        else:
            var_index -= len(self.Inputs)
            self.Outputs[var_index].MembershipFunctions.append(new_mf)
 

    def addRule(self, rule_matrix):
        for rule_def in rule_matrix:
            new_rule = fisrule(rule_def, len(self.Inputs))
            self.Rules.append(new_rule)


    def __addVariable(self, in_or_out, *varargin, **options):
        new_variable = fisvar(*varargin, **options)

        if in_or_out is 'input':
            self.Inputs.append(new_variable)
            if(options.get('NumMFs')):
                numMFs = options.get('NumMFs')
                var_range = new_variable.Range

                if(options.get('MFminr')):
                    mf_minr = options.get('MFminr')
                else:
                    mf_minr = var_range[0]

                if(options.get('MFmaxr')):
                    mf_maxr = options.get('MFmaxr')
                else:
                    mf_maxr = var_range[1]

                step = float(np.diff([mf_minr, mf_maxr]))/(numMFs-1)

                if(options.get('Overlap')):
                    overlap = options.get('Overlap')
                else:
                    overlap = .8

                mf_val = step/(2-overlap)
                var_name = new_variable.Name
                mf_type = options.get('MFType')

                b = mf_minr

                if(options.get('MFminr')):
                    c = mf_minr
                    params = [var_range[0]-mf_val, var_range[0], c, c+mf_val]
                    self.addMF(var_name, 'trapmf', params, Name='mf1')
                else:
                    params = [b-mf_val, b, b+mf_val]
                    self.addMF(var_name, mf_type, params, Name='mf1')

                b += step

                for i in range(1, (numMFs-1)):
                    params = [b-mf_val, b, b+mf_val]
                    self.addMF(var_name, mf_type, params, Name='mf'+str(i+1))
                    b += step

                if numMFs is 2:
                    i = 0

                if(options.get('MFmaxr')):
                    params = [b-mf_val, b, var_range[1], var_range[1]+mf_val]
                    self.addMF(var_name, 'trapmf', params, Name='mf'+str(i+2))
                else:
                    params = [b-mf_val, b, b+mf_val]
                    self.addMF(var_name, mf_type, params, Name='mf'+str(i+2))   
        else:
            self.Outputs.append(new_variable)
