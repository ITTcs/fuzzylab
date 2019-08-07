def writeFIS (fis, filename='filename.fis'):

    ## Open the output file.

    fid = open_output_file(filename)   

    ## Write the [System], [Input<number>], [Output<number>], and [Rules]
    ## sections of the output file.

    write_system_section(fid, fis)
    write_input_sections(fid, fis)
    write_output_sections(fid, fis)
    write_rules_section(fid, fis)

    ## Close the output file.

    fid.close()


##----------------------------------------------------------------------
## Function: open_output_file
## Purpose:  Open the output file. Return the fid if successful.
##           Otherwise, print an error message and halt.
##----------------------------------------------------------------------

def open_output_file(filename):

    ## If the filename is not empty, and if the last four characters of
    ## the filename are not '.fis', append '.fis' to the filename.

    if filename.endswith('.fis') is False:
        filename += '.fis'

    ## Open output file. 

    fid = open(filename, 'w') 

    return fid


##----------------------------------------------------------------------
## Function: write_system_section
## Purpose:  Write [System] section of the output file.
##----------------------------------------------------------------------

def write_system_section(fid, fis):
    fid.write("[System]\n")
    fid.write(f"Name='{fis.Name}'\n")
    fid.write(f"Type='{fis.Type}'\n")
    fid.write(f"Version=2.0\n")
    fid.write(f"NumInputs={len(fis.Inputs)}\n")
    fid.write(f"NumOutputs={len(fis.Outputs)}\n")
    fid.write(f"NumRules={len(fis.Rules)}\n")
    fid.write(f"AndMethod='{fis.AndMethod}'\n")
    fid.write(f"OrMethod='{fis.OrMethod}'\n")
    fid.write(f"ImpMethod='{fis.ImplicationMethod}'\n")
    fid.write(f"AggMethod='{fis.AggregationMethod}'\n")
    fid.write(f"DefuzzMethod='{fis.DefuzzificationMethod}'\n")

##----------------------------------------------------------------------
## Function: write_input_sections
## Purpose:  For each FIS input, write [Input<number>] section to
##           output file.
##----------------------------------------------------------------------

def write_input_sections(fid, fis):

    num_inputs = len(fis.Inputs)

    for i in range(num_inputs):
        num_mfs = len(fis.Inputs[i].MembershipFunctions)
        
        fid.write(f"\n[Input{i+1}]\n")
        fid.write(f"Name='{fis.Inputs[i].Name}'\n")
        fid.write(f"Range={str(fis.Inputs[i].Range).replace(',', '')}\n")
        fid.write(f"NumMFs={num_mfs}\n")
        for j in range(num_mfs):
            mf = fis.Inputs[i].MembershipFunctions[j]
            fid.write(f"MF{j+1}='{mf.Name}':'{mf.Type}',{str(mf.Parameters).replace(',', '')}\n")

##----------------------------------------------------------------------
## Function: write_output_sections
## Purpose:  For each FIS output, write [Output<number>] section to
##           output file.
##----------------------------------------------------------------------

def write_output_sections(fid, fis):

    num_outputs = len(fis.Outputs)

    for i in range(num_outputs):
        num_mfs = len(fis.Outputs[i].MembershipFunctions)
        
        fid.write(f"\n[Output{i+1}]\n")
        fid.write(f"Name='{fis.Outputs[i].Name}'\n")
        fid.write(f"Range={str(fis.Outputs[i].Range).replace(',', '')}\n")
        fid.write(f"NumMFs={num_mfs}\n")
        for j in range(num_mfs):
            mf = fis.Outputs[i].MembershipFunctions[j]
            fid.write(f"MF{j+1}='{mf.Name}':'{mf.Type}',{str(mf.Parameters).replace(',', '')}\n")


##----------------------------------------------------------------------
## Function: write_rules_section
## Purpose:  Write [Rules] section to output file.
##----------------------------------------------------------------------

def write_rules_section(fid, fis):

    num_inputs = len(fis.Inputs)
    num_outputs = len(fis.Outputs)
    num_rules = len(fis.Rules)

    fid.write("\n[Rules]\n")

    for i in range(num_rules):
        next_ant = fis.Rules[i].Antecedent
        next_con = fis.Rules[i].Consequent
        next_wt = fis.Rules[i].Weight
        next_connect = fis.Rules[i].Connection

        ## Print membership functions for the inputs.
        if num_inputs > 0:
            fid.write(f"{next_ant[0]}")

        for j in range(1,num_inputs):
            fid.write(f" {next_ant[j]}")
        fid.write(", ")

        ## Print membership functions for the outputs.
        for j in range(num_outputs):
            fid.write(f"{next_con[j]} ")

        ## Print the weight in parens.
        if type(next_wt) is int:
            fid.write(f"({next_wt}) : ")            
        else:
            fid.write(f"({next_wt:.4f}) : ")

        ## Print the connection and a newline.
        fid.write(f"{next_connect}\n")
      