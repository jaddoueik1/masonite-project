***Hello and welcome to our project!***
This is a Masonite based website that is actually a Corona Virus Tracker

in order to run smoothly our project you need the following lib:
NB: it is better to create a virtual environment for the project

1-Setting up our virtual environment:
    1- download virtualenv lib pip install virtualenv
        if you are a mac or linux user its better to run python3 -m pip install virtualenv 
    2- run virtualenv <name of the virtualenv>
    3-to activate it go to <name>/scripts/activate

So now that we have downloaded and activated our virtual environment we can proceed to download the libraries needed:
    1.Pandas
    2.Folium
    3.Geoip2.database
    4.Requests
    5.Covid
    6.Geopy
    7.PyMySQL
    8.mysql.connector
    9.Masonite

so now we are almost done 

all what we need to do left is to create our database and run the following files:
    Go to: storage/public/database

    1.run the file get-data.py
    2.go to your database management application create a database called masonite 
    3.inside your terminal run the command "craft migrate"
    4.open the file data-to-db.py:
        1.configure your database 
        2.run the file
    
Perfect now we have our virtual environment and our database table created we can proceed to the final step

open your terminal again go to the project and run craft install 

now go your newly ceated .env file and configure the database and your host to run the website

run craft serve and access to the website from your browser

Thank you for sticking with us during this long setup we hope that you will love the website which is only one part of our project!

The second part is a GUI Tkinter version of the system you can leave this folder now and go to the app folder open the only file there 
while you're still in your virtual environment and run it 

For further code documentation please check the files all of them are actually commented in order to understand every line 
***Thanks for sticking with us***
