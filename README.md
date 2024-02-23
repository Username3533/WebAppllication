#Web Journal Web Application using Django  

#Overview:  
This project is a web journal application developed using Django, a high-level Python web framework. The application allows users to log topics of interest, create entries, and manage their journal content.  
  
#Functionality:  
-User Authentication: Users can register or log in to access the application.  
-Topic Management: Users can create, read, and edit topics.  
-Entry Creation: Users can create entries for their topics, each entry can be edited and managed.  
-Security: Private journals ensure that only the creator can view and edit their entries.  

#Current Bugs:  
Logout Error: Users encounter a 405 error when logging out. Fixed by implementing a POST request for logout.  

#Features to Add:  
Delete Functionality: Allow users to delete entries and topics.  
Profile Picture Upload: Enable users to upload a profile picture.  
Friend System: Implement a friend system to connect with other users.  
Friend's Topics Viewing: Allow users to view topics created by their friends.  

#Lessons Learned:  
Django Setup: Installation and initialization of Django, including setting up a virtual environment.  
Model Management: Creating and migrating model classes to update database changes.  
User Management: Setting up user authentication, registration, and login using Django forms.  
Page Creation: Mapping URLs, writing view functions, and creating page templates.  
Form Handling: Implementing forms for adding new topics and entries.  
Security Measures: Utilizing CSRF tokens and implementing private journals.  
Bootstrap Styling: Styling the application using Bootstrap 4, including navigation bars and form styling.  

#Styling:  
Navigation Bar: Collapsible navigation bar with dynamic buttons based on user login status.  
Home Page: Styled using Bootstrap Jumbotron for an attractive display.  
Login Page: Bootstrap forms used for a clean and user-friendly login interface.  
Topic Pages: Styling applied to topic and topics pages for improved readability and aesthetics.  
-Styled login page using boostrap forms  
-Styled topic and topics html pages  
