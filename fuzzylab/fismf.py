class fismf:
    def __init__(self, *varargin, **options):
        self.Name = None
        self.Type = None
        self.Parameters = None

        nargin = len(varargin)

        if nargin == 0:
            self.Type = 'trimf'
            self.Parameters = [0, 0.5, 1]
        else:
            self.Type = varargin[0]
            if type(varargin[1]) is int or type(varargin[1]) is float:
                self.Parameters = [varargin[1]]
            else:
                self.Parameters = varargin[1]

        self.Name = options.get('Name')
        
             