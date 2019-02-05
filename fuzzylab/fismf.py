class fismf:
    def __init__(self, *varargin, **options):
        self.Name = None
        self.Type = None
        self.Parameters = None

        nargin = len(varargin)

        if nargin is 0:
            self.Type = 'trimf'
            self.Parameters = [0, 0.5, 1]
        else:
            self.Type = varargin[0]
            self.Parameters = varargin[1]

        self.Name = options.get('Name')
        
             