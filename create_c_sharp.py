

def create_c_sharp(first_name_of_measure):

    part1 = '" + \u0027\u0022\u0027 + m.Name + \u0027\u0022\u0027 + "'

    c_sharp_code = None
    with open("dax.txt", "r+", encoding="utf8") as f:

        # count number of ' or "
        dax_code = f.read().replace('"', '\\"').replace("\n", "")

        c_sharp_code = \
    f"""
    var i = 1;
    foreach (var m in Selected.Measures)

    \u007B
        m.Table.AddMeasure ("{first_name_of_measure} " + i, "{dax_code.replace("[NAME_HERE]", part1)}");
        i++;
    \u007D
    """
        
    with open("c_sharp.txt", "w", encoding="utf8") as f:
        f.write(c_sharp_code)


print("What is the first name of the measure?\n")
print("     Ex.: Sales is the first name of the measures; Sales MTD, Sales QTD, ...\n")
first_name_of_measure = input("Write the name: ")

create_c_sharp(first_name_of_measure)