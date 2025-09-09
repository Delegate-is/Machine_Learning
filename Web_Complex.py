# To create project eithher run {django-admin createproject} or {python -m django startproject}
# django-admin startproject Web_Complex
# python -m django startapp {Std_Info}
# use this either#C:\Users\Juma\AppData\Roaming\Python\Python313\Scripts\django-admin.exe startproject school
# Running app#python manage.py runserver
# add app name to settings.py
# python manage.py startapp teacher
# add app name to settings.py INSTALLED_APPS list 
# python manage.py makemigrations === to create migration file (store in migrations folder)
# python manage.py migrate   === make tables in merging created sql file to database
# python manage.py createsuperuser === to create admin user 

# create view in views.py
# create url in urls.py (from calculation.views import index)
# add path in urlpatterns list (path('', index),)
# add url to main urls.py 
# create template folder in app folder (calculation)
# create html file in template folder(add another folder with app name(calculation) inside template folder and store html file there(index.html))
# create folder static in app folder(calculation)
# create folder css in static folder
# create css file in css folder(style.css)
# link css file to html file
#####python manage.py runserver

#Prob 10. Create a web app to create a database table to store student details (name, age, email, phone number, address)
# and display the details in a web page using Django framework.
# Create a model in models.py
# Create a form in forms.py
# Create a view in views.py
# Create a template in templates folder
# Create a url in urls.py
# Migrate the model to create a table in the database
# python manage.py makemigrations
# python manage.py migrate
# Create a superuser to access the admin panel
# python manage.py createsuperuser
# Run the server
# python manage.py runserver
# Access the admin panel
# http://
#
# Add student details in the admin panel
# http://
# Access the web page to display the student details
# http://