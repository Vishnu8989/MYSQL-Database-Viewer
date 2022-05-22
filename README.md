# MYSQL-Database-Viewer <img src='./mysql.png'  alt="MYSQL" width="30" height="25">

It is a simple tool to view the content of a MySQL-Database.
<br>
The app let you view your tables from database depending on the user configuration.
<br>
It was build using <a href="https://docs.python.org/3/library/tkinter.html" target = "_blank">TKinter</a> and <a href="https://docs.python.org/3/" target = "_blank">Python</a>.

<hr style="border-top: 1px dashed white;border-bottom: 1px dashed white;">

![GitHub last commit](https://img.shields.io/github/last-commit/vishnu8989/MYSQL-Database-Viewer)
[![GitHub issues](https://img.shields.io/github/issues/Vishnu8989/MYSQL-Database-Viewer)](https://github.com/Vishnu8989/MYSQL-Database-Viewer/issues)
[![GitHub forks](https://img.shields.io/github/forks/Vishnu8989/MYSQL-Database-Viewer)](https://github.com/Vishnu8989/MYSQL-Database-Viewer/network)
[![GitHub stars](https://img.shields.io/github/stars/Vishnu8989/MYSQL-Database-Viewer)](https://github.com/Vishnu8989/MYSQL-Database-Viewer/stargazers)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/vishnu8989/MYSQL-Database-Viewer?style=plastic)
[![GitHub license](https://img.shields.io/github/license/Vishnu8989/MYSQL-Database-Viewer)](https://github.com/Vishnu8989/MYSQL-Database-Viewer)
[![Twitter](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2FVishnu__Rajawat)](https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2FVishnu8989%2FMYSQL-Database-Viewer)

<hr style="border-top: 1px dashed white;border-bottom: 1px dashed white;">

## How to Install and Run the Project

<hr style="border-top: 1px dashed white;border-bottom: 1px dashed white;">

### Required Libraries

1. <a href="https://docs.python.org/3/library/tkinter.html" target = "_blank">TKinter</a>
2. <a href="https://www.python.org/downloads/" target = "_blank">Python</a>
3. <a href="https://www.mysql.com/" target = "_blank">MySQL</a>
4. <a href="https://pandas.pydata.org/" target = "_blank">Pandas</a>

First, you can install the required libraries by running the following command in your command prompt:

```
pip install tk
pip install mysql
pip install pandas
```

You can get more information abut getting code from here:<br>
<a href="https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository" target = "_blank">Cloning a repository</a>
<br>
<br>
Now you can run the app by running the following command:

```
python mysql_database_viewer.py
```

<hr style="border-top: 1px dashed white;border-bottom: 1px dashed white;">

## How to Use the Project

<hr style="border-top: 1px dashed white;border-bottom: 1px dashed white;">

Before Running the code for first time you need to change the folling line of code in mysql_database_viewer.py file:

```
database = "sakila"
table = "sales_by_film_category"
// Above details are predefined databse,table in MySQL so no need to change it
host = "localhost"          //Most likely remain the same
user = "studentadmin"       //Change this to your username
password = "8989"           //Change this to your password
```

You are good to go from here

<hr style="border-top: 1px dashed white;border-bottom: 1px dashed white;">

## Future Plan

<hr style="border-top: 1px dashed white;border-bottom: 1px dashed white;">

This was just a simple project to view the content of a MySQL-Database.
But actual plan was to make a database management system which can be used to manage the database.
Lets see if we can make it or not :).
<br>

<br>
