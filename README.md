# Django_sample
This is a sample project in Django framework

# Set up virtual environment for Django
In terminal inside the project directory, /home/foteinip/DjangoTest/Django_sample/trydjango we type:
virtualenv -p python3 .
To activate the v.e. we type:
source bin/activate
After entering the virtual environment, we install Django. 
pip install django==2.0.7

# Directories
The main directory is /home/foteinip/DjangoTest/Django_sample/trydjango/src where the manage.py be.
In order to have the server up we type:
python manage.py runserver

# How to test
Since the server is up and running we can test the methods we created. 
How to test
1. list of all names -- 127.0.0.1:8000/names/
   *it returns a list template with the names from the csv
2. get a name by id -- 127.0.0.1:8000/names/1/
   *note that this is not exaclty what you asked beacause i faced issues with the urls. It returned Not found: The requested URL/names/1/ was not found on this server. This is the reason why i hardcoded the ids in the get_name_by_id view. It returns the right name.
3. delete name by id -- 127.0.0.1:8000/name/1/
   *i faced the same error. I hardcoded the id in order to check if the method works as i want. It does.
4. post a name: -- 127.0.0.1:8000/name/{some_name}
   *it returns an HttpResponse with a message that the {some_name} was inserted
   *it also update the csv file with {some_name} and a random id number
5. put name, id -- 127.0.0.1:8000/putname/{id}/{name}
   *it returns an HttpResponse with a message of the updated id and name
   *it updates or insered {id} and {name} in the csv file. 
 

