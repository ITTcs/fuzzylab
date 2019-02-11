from .fisvar import fisvar
from .fismf import fismf
from .fisrule import fisrule

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
        else:
            self.Outputs.append(new_variable)
