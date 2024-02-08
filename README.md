Web Journal Web Appllication using Django  

Functionality:  

  -Allows users to log topics they are interested in  
  -Home page will describe the site and invite users to register or log in  
  -Users can creat topics, entries, read and edit existing entries  

Things Learned:  

-Installed Django, pip, initalized virtual environment and a local server ('py -3 -m venv .venv' -and- '.venv\scripts\activate')  
-Created model classes and 'py manage.py makemigration app_name' + 'py manage.py migrate' to tell django to update changes  
-Created superuser as admin and made topics based on the models made and migrated  
-Made a many-to-one entry model so multiple entries can be linked to one topic and will cascade delete  
-Mapped urls using django.url and app.url and made a template for a home page  
-Making pages: specify url pattern, write view function, write template  
-Created page templates and other pages that inherit from the base.html template  
-Created form for adding new topics by users  
-Added ability to edit posts
