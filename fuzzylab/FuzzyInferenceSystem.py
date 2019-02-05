from .fisvar import fisvar
from .fismf import fismf
from .fisrule import fisrule

class FuzzyInferenceSystem:
    def addInput(self, *varargin, **options):
        self.__addVariable('input', *varargin, **options)


    def addOutput(self, *varargin, **options):
        self.__addVariable('output', *varargin, **options)


    def addMF(self, varName, *varargin, **options):
        varsName = [var.Name for var in self.Inputs + self.Outputs]
        var_index = varsName.index(varName)
        
        new_mf = fismf(*varargin, Name=options.get('Name'))

        if varsName.index(varName) < len(self.Inputs):
            self.Inputs[var_index].MembershipFunctions.append(new_mf)
        else:
            var_index -= len(self.Inputs)
            self.Outputs[var_index].MembershipFunctions.append(new_mf)
 
    def addRule(self, rule_matrix):
        for rule_def in rule_matrix:
            new_rule = fisrule(rule_def, len(self.Inputs))
            self.Rules.append(new_rule)

    def __addVariable(self, varType, *varargin, **options):
        new_variable = fisvar(*varargin, **options)

        if varType is 'input':
            self.Inputs.append(new_variable)
        else:
            self.Outputs.append(new_variable)
