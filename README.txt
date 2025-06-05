Stroke Prediction and Support System
Overview
This system; 
  -predict the likelihood of a stroke based on patient health history.
  -offers educational support on stroke using a chatbot.
  -offers an emotional support be allowing users to interact in a web based group chat application.
  -offers a platform for recording of data on stroke. This helps in enhancing research on stroke and also helps in training of the model.
  -The data collected is encrypted

Requirements
VScode
-python 3.10
-Django
-SQlite/MYSQL

Setup instructions
all the requirements are available at the requirements.txt file
on the terminal run the following command:
  pip install -r requirements.txt

 setup database
  run the following command;
  python manage.py makemigrations
  python manage.py migrate

Run the project:
run the following command:
  python manage.py runserver


on the browser now navigate through 127.0.0.1:8000