import pandas as pd
# import webbrowser
import os
# import sys


def easy_measures(template_file: str, sheet: str, column_name: str):
    df = pd.read_excel(template_file, sheet)

    with open("tabular editor measures.txt", "w", encoding="utf8") as f:

        for row in df[column_name]:
            if type(row) == str:
                row = row.replace("\u00A0", "")

                f.write(f'''Model.Tables["_Measures_"].AddMeasure("{row}", "\\"{row}\\"");\n''')


files_dir = os.listdir()
print("# Which file do you want to use as template?\n")
for i, files in enumerate(files_dir):
    print(f"{i:2d} - {files}")

print("\n")
file_index = int(input("Number of the file: "))
file_name = files_dir[file_index]

print("\n")
sheet_page = input("What's the name of the sheet? ")
# if sheet_page.lower() == "eric": webbrowser.open("https://drive.google.com/file/d/1NEccwIP9-bWBU9rSGbxqvjv4haGvW0b9/view?usp=sharing")
# sys.exit()
df_columns = pd.read_excel(file_name, sheet_page).columns

print("\n")
column_ID = print("What's the name of the ID Column?\n")
for i, files in enumerate(df_columns):
    print(f"{i:2d} - {files}")

column_index = int(input("Number of the file: "))
column_name = df_columns[column_index]

easy_measures(file_name, sheet_page, column_name)
