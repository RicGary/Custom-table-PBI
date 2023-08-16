""" 
I'm not aiming on performance so don't mind if I create some 
variables two times and etc.

Enjoy right in C# !!

Model.Tables["_Measures_"].AddMeasure(
    "Test",
    @"SWITCH(
  SELECTEDVALUE(template_weekly[Program MGT]),
   "+'"'+@"Program MGT 1"+'"'+@", FORMAT([Program MGT 1], "+'"'+@"#,#;(#,#);0"+'"'+@"))"
    );


Model.Tables["_Measures_"].AddMeasure(
    "Test",
    "Var % Total 3 = [Var % 9]+[Var % 10]+[Var % 11]+[Var % 12]"
    );
"""
import pandas as pd
import os


def create_switch_measures(
    template_dir: str, 
    sheet_name: str, 
    name_of_template: str, 
    format_style: str = """\"#,#;(#,#);0\""""
    ) -> None: 
    """
    Function to create Switch measures easily with the help of Tabular Editor.
    Read the documentation for more.
    """

    substitute = """\"+'"'+@\""""

    df = pd.read_excel(template_dir, sheet_name)
    df_columns = df.columns[2:-1]

    dax_each_column = []
    switch = "SWITCH(\n"
    for column in df_columns:
        selected_value = f"  SELECTEDVALUE({name_of_template}[{column}]),\n"
        row_values = ""
        for i, row in enumerate(df[column]):
            if type(row) == str:
                if i != len(df[column]) - 1:
                    row_values += f"""  "{row}", FORMAT([{row}], {format_style}),\n"""
                else:
                    row_values += f"""  "{row}", FORMAT([{row}], {format_style})\n"""

        final_dax = switch + selected_value + row_values + "\n  //Enjoy your measure :) \n)"
        final_dax = final_dax.replace('"', substitute)
        
        c_sharp_code = \
        f"""Model.Tables["_Measures_"].AddMeasure(
            "{column} Switch",
            @"{final_dax}"
    );
        """

        dax_each_column.append(c_sharp_code)

    full_code = "\n".join(dax_each_column)

    with open("All switch measures.txt", "w", encoding="utf8") as f:
        f.write(full_code)


files_dir = os.listdir()
print("# Which file do you want to use as template?\n")
for i, files in enumerate(files_dir):
    print(f"{i:2d} - {files}")

print("\n")
file_index = int(input("Number of the file: "))
file_name = files_dir[file_index]

print("\n")
sheet_name = input("What's the name of the sheet? ")

print("\n")
name_of_template = input("What's the name of the template inside PowerBI? ")

create_switch_measures(file_name, sheet_name, name_of_template)

df = pd.read_excel(file_name, sheet_name)
df_columns = df.columns[2:-1]

with open("All switch measures.txt", "a", encoding="utf8") as f:
    for column in df_columns:
        total_index = 1
        subtotal_index_final = 1
        subtotal_index_start = 1

        row_sum = ""
        for row in df[column]:
            if type(row) is str:
                if "Total" not in row:
                    row_sum += f"[{column} {subtotal_index_final}]+"

                if "Total" in row:
                    sum_dax = f"{column} Total {total_index} = {row_sum[:-1]}"

                    create_measure = \
    f"""Model.Tables["_Measures_"].AddMeasure(
        "{column} Total {total_index}",
        "{row_sum[:-1]}"
    );\n
    """

                    f.write(create_measure)
                    
                    row_sum = ""

                    total_index += 1
                    subtotal_index_start = subtotal_index_final
                
                
                subtotal_index_final += 1
            else:
                subtotal_index_final -= 1

        

            