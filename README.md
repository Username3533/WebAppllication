# WebAppllication  
Web Journal using Django  

Functionality:  

  -Allows users to log topics they are interested in  
  -Home page will describe the site and invite users to register or log in  
  -Users can creat topics, entries, read and edit existing entries  

Things Learned:  
Installed Django, pip, initalized virtual environment and a local server ('py -3 -m venv .venv' -and- '.venv\scripts\activate')  
Created model classes and 'py manage.py makemigration app_name' + 'py manage.py migrate' to tell django to update changes  
Created superuser as admin and made topics based on the models made and migrated  
Made a many-to-one entry model so multiple entries can be linked to one topic  
Mapped urls using django.url and webapp.url and made a template for a home page  
