import numpy as np
from .evalmf import evalmf
from .wtaver import wtaver
from .sugfis import sugfis
from .defuzz import defuzz

def evalfis(fis, user_input):

    if type(user_input) is not np.ndarray:
        if type(user_input) is float:
            user_input = [user_input]
        
        user_input = np.asarray([user_input])

    if user_input.ndim is 1:
        user_input = np.asarray([user_input])

    m, n = user_input.shape
    num_inputs = len(fis.Inputs)

    if m is num_inputs and n is not num_inputs:
        user_input = user_input.transpose()

    output = np.zeros(user_input.shape)

    for i in range(user_input.size):
        rule_input = fuzzify_input(fis, user_input[i])

        firing_strength = eval_firing_strength (fis, rule_input)
        
        if type(fis) is sugfis:
            rule_output = eval_rules_sugeno(fis, firing_strength, user_input[i])
            # fuzzy_output = aggregate_output_sugeno (fis, rule_output)
            fuzzy_output = rule_output
            output[i] = defuzzify_output_sugeno (fis, fuzzy_output)

    return output

def fuzzify_input(fis, user_input):
    num_rules  = len(fis.Rules)
    num_inputs = len(fis.Inputs)
    rule_input = np.zeros((num_rules, num_inputs))

    # For each rule i and each input j, compute the value of mu
    # in the result. 

    for i in range(num_rules):
        antecedent = fis.Rules[i].Antecedent
        for j in range(num_inputs):
            mu = 0
            crisp_x = user_input[j]

            # Get the value of mu (with adjustment for the hedge
            # and not_flag).

            #mf_index, hedge, not_flag = get_mf_index_and_hedge(antecedent[j])
            
            #print(mf_index)

            mf_index = antecedent[j]

            #if mf_index >= 0:
            mf = fis.Inputs[j].MembershipFunctions[mf_index]
            mu = evalmf (mf, crisp_x)
            # Store the fuzzified input in rule_input.
                        
            rule_input[i, j] = mu
    
    return rule_input

#def get_mf_index_and_hedge(mf_index_and_hedge):
def get_mf_index(mf_index_and_hedge):
    ## Set flag to handle "not", indicated by a minus sign in the
    ## antecedent.    

    #if mf_index_and_hedge < 0:
        #print(13)
    #    not_flag = True
    #    mf_index_and_hedge = -mf_index_and_hedge
    #else:
        #print(14)
    #    not_flag = False

    #print('not_flag =', not_flag)

    # The membership function index is the positive whole number portion
    # of an element in the antecedent.

    mf_index = int(np.fix(mf_index_and_hedge))

    # For custom hedges and the four built-in hedges "somewhat", "very",
    # "extremely", and "very very", return the power to which the
    # membership value should be raised. The hedges are indicated by the
    # fractional part of the corresponding rule_matrix entry (rounded to
    # 2 digits). 

    #if mf_index >= 0:
        #print(15)
    #    hedge = round (100 * (mf_index_and_hedge - mf_index)) / 10
    #else:
        #print(16)
    #    hedge = 0

    #return mf_index, hedge, not_flag
    return mf_index
 

def eval_firing_strength (fis, rule_input):

    num_rules = len(fis.Rules)
    num_inputs = len(fis.Inputs)

    # Initialize output matrix to prevent inefficient resizing.
    firing_strength = np.zeros (num_rules)
 
    ## For each rule
    ##    1. Apply connection to find matching degree of the antecedent.
    ##    2. Multiply by weight of the rule to find degree of the rule.

    for i in range(num_rules):
        rule = fis.Rules[i]

        # Collect mu values for all input variables in the antecedent.
        antecedent_mus = []
        for j in range(num_inputs):
            if rule.Antecedent[j] >= 0:
                mu = rule_input[i, j]
                antecedent_mus.append(mu)

        # Compute matching degree of the rule.
        if rule.Connection is 1:
            connect = fis.AndMethod
        else:
            connect = fis.OrMethod

        if connect is 'prod':
            #print(antecedent_mus)
            firing_strength[i] = rule.Weight * np.prod(antecedent_mus)

    return firing_strength

def eval_rules_sugeno(fis, firing_strength, user_input):

    num_rules = len(fis.Rules)
    num_outputs = len(fis.Outputs)

    # Initialize output matrix to prevent inefficient resizing.
    rule_output = np.zeros ((2, num_rules * num_outputs))   

    # Compute the (location, height) of the singleton output by each
    # (rule, output) pair:
    #   1. The height is given by the firing strength of the rule, and
    #      by the hedge and the not flag for the (rule, output) pair.
    #   2. If the consequent membership function is constant, then the
    #      membership function's parameter gives the location of the
    #      singleton. If the consequent membership function is linear,
    #      then the location is the inner product of the the membership
    #      function's parameters and the vector formed by appending a 1
    #      to the user input vector.

    #print(firing_strength)
    for i in range(num_rules):
        rule = fis.Rules[i]
        rule_firing_strength = firing_strength[i]

        if rule_firing_strength is not 0:
            for j in range(num_outputs):
                
                ## Compute the singleton height for this (rule, output) pair.
                ## Note that for Sugeno FISs, the hedge and not flag are handled
                ## by adjusting the height of the singletons for each
                ## (rule, output) pair.                
    
                #mf_index, hedge, not_flag = get_mf_index_and_hedge(
                #    rule.Consequent[j])

                mf_index = rule.Consequent[j]

                height = rule_firing_strength

                # Compute the singleton location for this (rule, output) pair.

                if mf_index >= 0:
                    mf = fis.Outputs[j].MembershipFunctions[mf_index]

                    if mf.Type is 'constant':
                        location = mf.Parameters

                    # Store result in column of rule_output corresponding
                    # to the (rule, output) pair.   

                    rule_output[0, (j - 1) * num_rules + i] = location
                    rule_output[1, (j - 1) * num_rules + i] = height
    
    return rule_output

def aggregate_output_sugeno(fis, rule_output):

    fuzzy_output = []
    num_outputs = len(fis.Outputs)
    num_rules = len(fis.Rules)

    # For each FIS output, aggregate the slice of the rule_output matrix,
    # then store the result as a structure in fuzzy_output.

    for i in range(num_outputs):
        unagg_output = rule_output[:, (i-1)*num_rules+1 : i*num_rules]
        aggregated_output = aggregate_fis_output(fis.aggMethod, unagg_output)

    return fuzzy_output

#----------------------------------------------------------------------
# Function: aggregate_fis_output
# Purpose:  Aggregate the multiple singletons for one FIS output.
#----------------------------------------------------------------------

def aggregate_fis_output(fis_aggmethod, rule_output):

    # Initialize output matrix (multiple_singletons).
    mult_singletons = 0
    return mult_singletons

def defuzzify_output_sugeno(fis, aggregated_output):

    num_outputs = len(fis.Outputs)
    output = np.zeros(num_outputs)

    for i in range(num_outputs):
        next_agg_output = aggregated_output
        x = next_agg_output[0]
        y = next_agg_output[1]
        output[i] = defuzz(x, y, fis.DefuzzificationMethod)

    return output