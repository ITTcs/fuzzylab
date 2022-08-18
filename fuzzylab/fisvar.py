class fisvar:
    def __init__(self, *varargin, **options):

        self.Name = None
        self.Range = None
        self.MembershipFunctions = []

        nargin = len(varargin)

        if nargin == 0:
            self.Range = [0, 1] 
        else:
            self.Range = varargin[0]

        self.Name = options.get('Name')
