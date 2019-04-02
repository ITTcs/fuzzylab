from .FuzzyInferenceSystem import FuzzyInferenceSystem

class sugfis(FuzzyInferenceSystem):
    def __init__(self, 
        Name                    = 'fis',
        AndMethod               = 'prod',
        OrMethod                = 'probor',
        ImplicationMethod       = 'prod',
        AggregationMethod       = 'sum',
        DefuzzificationMethod   = 'wtaver'):

        FuzzyInferenceSystem.__init__(self)

        self.Name                       = Name
        self.AndMethod                  = AndMethod
        self.OrMethod                   = OrMethod
        self.ImplicationMethod          = ImplicationMethod
        self.AggregationMethod          = AggregationMethod
        self.DefuzzificationMethod      = DefuzzificationMethod
    