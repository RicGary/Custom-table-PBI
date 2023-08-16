<h1 align="center">Fast custom table PBI!</h1>
<p align="center" >by: <em>Eric Naiber</em></p>

<p align="center">
<a href="https://ericnaiber.com">Visit my site here!</a>
</p>

<p align="center" >
    <img src="img/custom table.png">
</p>

<p align="center"><b>Figure:</b> <a href="https://www.youtube.com/watch?v=J4317R5BvsA&ab_channel=HowtoPowerBI">How to Build a Financial Report in Power BI</a></p>

 <h4>
    <i>🚧 This code isn't clean nor optimal, I just did something fast to don't spend much time doing the same thing over and over again. 🚧</i>
</h4>

<hr>

<h2>
    <b>How it works?</b>
</h2>

Basically the scripts reads your template and your Dax code to create new scripts in C# to be used on tabular editor. The process is very tricky, so follow the steps.

 <h2>
    <b>Installation:</b>
</h2>

* Clone the repository:

    ```
    git clone https://github.com/RicGary/Custom-table-PBI.git
    ```

* Install requirements:

    ```
    pip install -r [PATH]/requirements.txt
    ```

* Install the tabular editor to your PBI, there is a free option and that's the one I'm using.

<br>
 <h2>
    <b>How to use?</b>
</h2>

 <h3>
    <b> 👽 Creating the template</b>
</h3>

<b>WARNING: Learn first how to create custom tables first watching this video: <a href="https://www.youtube.com/watch?v=J4317R5BvsA&ab_channel=HowtoPowerBI">How to Build a Financial Report in Power BI</a></b>

* You need to create a template on excel/google sheets and put it in the same directory of the code. The template have to follow some rules:

1. All the column names MUST be different

2. The values inside the template should be the same, the only thing can change is the number. Ex: Sales 1, Sales 2, ..., Sales n

3. For the total of a specific section use the same name and in the end "Total n". Ex: Sales Total 1, Sales Total 2, ..., Sales Total n.

 <h3>
    <b> 👽 Creating the DAX Code</b>
</h3>

1. As you can see, there are a dax.txt file inside the repo, just paste your code there and replace the part that should have the ID with `[NAME_HERE]`. Ex:

```
We have this on the template_test.xlsx:

Territory (column name)
    Global Sales 1 (ID 1)
    Global Sales 2 (ID 2)

I have a column on my database that is Territory, and there is a Global Sales 1 in there, so to filter I'm going to use:

CALCULATE(
    SUM([SALES-COLUMN]),
   [Territory-COLUMN] = "Global Sales 1"
)

So inside the dax.txt you put:

CALCULATE(
    SUM([SALES-COLUMN]),
   [Territory-COLUMN] = [NAME_HERE]
)
```

<br>

 <h3>
    <b>Running the code 👽 </b>
</h3>

There are some steps that can be done more than one time, I'm going to warn when it's the case.
Close the template before running the codes or it won't work.



1. First double click on `create_id_measures.py`, follow the instructions and one .txt file should appear in the directory.

2. Copy this code, open tabular editor, paste on advance editor or C# Script and run it. It will create some measures that you are going to use.

You can do this step more than one time, for each column you have to change the dax.txt file.

3. Double click on `create_c_sharp.py`, follow the instructions and one .txt file should appear in the directory.

4. Copy the code inside it and paste on tabular editor (same place as before). Select all the IDs holding `ctrl` <b>ATTENTION, DON'T SELECT THE TOTAL ID's !!!</b> and run the script. If everything went fine you should have now a bunch of new measures.

This you just need to do one time.

5. Double click on `create_switch.py`, follow the instructions and one .txt file should appear in the directory.

6. Copy this code, open tabular editor, paste it and run it. It will create some switch and total measures.

7. From here you just put the switch measures inside the table/matrix you are goping to use.


If you have any questions please contact me.<br>
ericnaiber@gmail.com