from fuzzylab import sugfis, mamfis, fisvar, fismf, fisrule
import re

def readfis(filename=''):

    ## Open the input file.

    fid = open_input_file(filename)

    fis, num_inputs, num_outputs, num_rules = init_fis_struct(fid)
    read_fis_inputs(fid, fis, num_inputs)
    read_fis_outputs(fid, fis, num_outputs)
    read_rules(fid, fis, num_inputs, num_rules)

    fid.close()

    return fis


##----------------------------------------------------------------------
## Function: open_input_file
## Purpose:  Open the input file specified by the filename. If the
##           filename does not end with ".fis", then append ".fis" to
##           the filename before opening. Return an fid if successful.
##           Otherwise, print an error message and halt.
##----------------------------------------------------------------------

def open_input_file(filename):

    ##--------------------------------------------------------------------
    ## If the filename is not empty, and if the last four characters of
    ## the filename are not '.fis', append '.fis' to the filename. If the
    ## filename is empty, use a dialog to select the input file.
    ##--------------------------------------------------------------------

    if filename.endswith('.fis') is False:
        filename += '.fis'

    ##--------------------------------------------------------------------
    ## Open input file.
    ##--------------------------------------------------------------------

    fid = open(filename, 'r') 

    return fid

##----------------------------------------------------------------------
## Function: init_fis_struct
## Purpose:  Read the [System] section of the input file. Using the
##           strings read from the input file, create a new FIS. If an
##           error in the format of the input file is found, print an
##           error message and halt.
##----------------------------------------------------------------------

def init_fis_struct(fid):

    ##--------------------------------------------------------------------
    ## Read the [System] section.
    ##--------------------------------------------------------------------

    get_line(fid)
    values = get_line(fid).split('=')
    assert values[0] == 'Name', 'Name of FIS expected'
    fis_name = values[1][1:-1]

    values = get_line(fid).split('=')
    assert values[0] == 'Type', 'Type of FIS expected'
    fis_type = values[1][1:-1]

    values = get_line(fid).split('=')
    if values[0] =='Version':
        values = get_line(fid).split('=')

    assert values[0] == 'NumInputs', 'Number of inputs expected'
    num_inputs = int(values[1])

    values = get_line(fid).split('=')
    assert values[0] == 'NumOutputs', 'Number of oututs expected'
    num_outputs = int(values[1])

    values = get_line(fid).split('=')
    assert values[0] == 'NumRules', 'Number of rules expected'
    num_rules = int(values[1])

    values = get_line(fid).split('=')
    assert values[0] == 'AndMethod', 'And method  expected'
    and_method = values[1][1:-1]

    values = get_line(fid).split('=')
    assert values[0] == 'OrMethod', 'Or method expected'
    or_method = values[1][1:-1]

    values = get_line(fid).split('=')
    assert values[0] == 'ImpMethod', 'Implication method expected'
    imp_method = values[1][1:-1]

    values = get_line(fid).split('=')
    assert values[0] == 'AggMethod', 'Aggregation method expected'
    agg_method = values[1][1:-1]

    values = get_line(fid).split('=')
    assert values[0] == 'DefuzzMethod', 'Defuzzification method expected'
    defuzz_method = values[1][1:-1]

    ##--------------------------------------------------------------------
    ## Create a new FIS structure using the strings read from the
    ## input file.
    ##--------------------------------------------------------------------

    if fis_type == 'sugeno':
        fis = sugfis(fis_name)
    elif fis_type == 'mamdani':
        fis = mamfis(fis_name)

    fis.AndMethod               = and_method
    fis.OrMethod                = or_method
    fis.ImplicationMethod       = imp_method
    fis.AggregationMethod       = agg_method
    fis.DefuzzificationMethod   = defuzz_method

    return fis, num_inputs, num_outputs, num_rules


##----------------------------------------------------------------------
## Function: read_fis_inputs
## Purpose:  For each FIS input, read the [Input<number>] section from
##           file. Add each new input and its membership functions to
##           the FIS structure.
##----------------------------------------------------------------------

def read_fis_inputs (fid, fis, num_inputs):

    for i in range(num_inputs):
        next_fis_input, num_mfs = get_next_fis_io(fid, i, 'input')
        fis.Inputs.append(next_fis_input)

        ##------------------------------------------------------------------
        ## Read membership function info for the current FIS input from
        ## file. Add each new membership function to the FIS struct.
        ##------------------------------------------------------------------

        for j in range(num_mfs):
            next_mf = get_next_mf(fid, i, j, 'input')
            fis.Inputs[i].MembershipFunctions.append(next_mf)


##----------------------------------------------------------------------
## Function: read_fis_outputs
## Purpose:  For each FIS output, read the [Output<number>] section from
##           file. Add each new output and its membership functions to
##           the FIS structure.
##----------------------------------------------------------------------


def read_fis_outputs (fid, fis, num_outputs):

    for i in range(num_outputs):
        next_fis_input, num_mfs = get_next_fis_io(fid, i, 'output')
        fis.Outputs.append(next_fis_input)

        ##------------------------------------------------------------------
        ## Read membership function info for the current FIS output from
        ## file. Add each new membership function to the FIS struct.
        ##------------------------------------------------------------------

        for j in range(num_mfs):
            next_mf = get_next_mf(fid, i, j, 'output')
            fis.Outputs[i].MembershipFunctions.append(next_mf)


##----------------------------------------------------------------------
## Function: read_rules
## Purpose:  Read the [Rules] section from file, and add the rules to
##           the FIS.
##----------------------------------------------------------------------

def read_rules(fid, fis, num_inputs, num_rules):
    
    get_line(fid)
    for _ in range(num_rules):
        next_rule = get_next_rule(fid, num_inputs)
        fis.Rules.append(next_rule)


##----------------------------------------------------------------------
## Function: get_next_fis_io
## Purpose:  Read the next [Input<i>] or [Output<i>] section of the
##           input file. Using the info read from the input file, create
##           a new FIS input or output structure. If an error in the
##           format of the input file is found, print an error message
##           and halt.
##----------------------------------------------------------------------

def get_next_fis_io (fid, i, in_or_out):
    
    ##--------------------------------------------------------------------
    ## Read [Input<i>] or [Output<i>] section from file.
    ##--------------------------------------------------------------------

    values = get_line(fid).split('put')
    if in_or_out == 'input':     
        assert values[0] == '[In', 'Next input expected'
    else:
        assert values[0] == '[Out', 'Next output expected'
    io_index = int(values[1][:-1])
    assert io_index == i+1, 'Incorrect i/o index readed'
    
    values = get_line(fid).split('=')
    assert values[0] == 'Name', f'Name of {in_or_out} {i+1} expected'
    var_name = values[1][1:-1]   

    values = get_line(fid).split('=')
    assert values[0] == 'Range', f'Range for {in_or_out} {i+1} expected'
    range_values = values[1].split(' ')
    range_low = float(range_values[0][1:])
    range_high = float(range_values[1][:-1])
    assert range_low < range_high, f'Correct range for {in_or_out} {i+1} expected'

    values = get_line(fid).split('=')
    assert values[0] == 'NumMFs', f'Number of MFs for {in_or_out} {i+1} expected'
    num_mfs = int(values[1])

    ##--------------------------------------------------------------------
    ## Create a new FIS input or output structure.
    ##--------------------------------------------------------------------

    next_fis_io = fisvar([range_low, range_high], Name=var_name)

    return next_fis_io, num_mfs


##----------------------------------------------------------------------
## Function: get_next_mf
## Purpose:  Read information specifying the jth membership function for
##           Input<i> or Output<i> (if in_or_out is 'input' or 'output',
##           respectively) from the input file. Create a new membership
##           function structure using the info read. If an error in the
##           format of the input file is found, print an error message
##           and halt.
##----------------------------------------------------------------------

def get_next_mf(fid, i, j, in_or_out):
            
    ##--------------------------------------------------------------------
    ## Read membership function info for the new FIS input or output
    ## from file.
    ##--------------------------------------------------------------------

    values = re.split(r'=|:|,|]|\[| ', get_line(fid))
    assert values[0][:2] == 'MF', f'Next MF for {in_or_out} {i+1} expected'
    mf_index = int(values[0][2:])
    assert mf_index == j+1, f'Correct MF index for {in_or_out} {i+1} expected'
    mf_name = values[1][1:-1]  
    mf_type = values[2][1:-1] 
    #mf_params = float(values[4]) if mf_type == 'constant' else [float(val) for val in values[4:-1]]
    mf_params = [float(val) for val in values[4:-1]]
    #mf_params = [float(val) for val in values[4:-1]]

    next_mf = fismf(mf_type, mf_params, Name=mf_name)

    return next_mf


##----------------------------------------------------------------------
## Function: get_next_rule
## Purpose:  Read the next rule from the input file. Create a struct for
##           the new rule. If an error in the format of the input file
##           is found, print an error message and halt.
##----------------------------------------------------------------------

def get_next_rule(fid, num_inputs):

    line = get_line(fid)
    values = [val for val in re.split(r':|,|\(|\)| ', line) if val]

    for i in range(len(values) - 2):
        values[i] = int(values[i])
    
    values[-2] = int(values[-2]) if (float(values[-2])).is_integer() else float(values[-2]) 
    values[-1] = int(values[-1])

    next_rule = fisrule(values, num_inputs)
    
    return next_rule

##----------------------------------------------------------------------
## Function: get_line
## Purpose:  Read the next line of the input file (without the newline)
##           into line. Print an error message and halt on eof.
##----------------------------------------------------------------------

def get_line(fid):
    while True:
        line = fid.readline()
        if(len(line) == 0):
            break
        line = line.strip()

        if(comment_or_empty(line) is False):
            break

    return line


##----------------------------------------------------------------------
## Function: comment_or_empty
## Purpose:  Return true if the line is a comment (that is, it begins
##           with '#' or '%') or an empty line, and return false
##           otherwise. It is assumed that leading whitespace has been
##           removed from the input line.
##----------------------------------------------------------------------

def comment_or_empty(line):
    ret_val = len(line) == 0 or line[0] == '#' or line[0] == '%'
    return ret_val
