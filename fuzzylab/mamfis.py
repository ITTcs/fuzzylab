from .FuzzyInferenceSystem import FuzzyInferenceSystem

class mamfis(FuzzyInferenceSystem):
    def __init__(self, 
        Name                    = 'fis',
        AndMethod               = 'min',
        OrMethod                = 'max',
        ImplicationMethod       = 'min',
        AggregationMethod       = 'max',
        DefuzzificationMethod   = 'centroid'):

        FuzzyInferenceSystem.__init__(self)

        self.Name                       = Name
        self.Type                       = 'mamdani'
        self.AndMethod                  = AndMethod
        self.OrMethod                   = OrMethod
        self.ImplicationMethod          = ImplicationMethod
        self.AggregationMethod          = AggregationMethod
        self.DefuzzificationMethod      = DefuzzificationMethod
    