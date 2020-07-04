User Activity Period Tracker

The project is focussed to deliver the activity time period of users along with their respective timezone.

Getting Started:
  
  Requirements:
    Python: 3+
    Django Rest framework
  
  Usage:
    
    All the functionalities are coded in class based views.
    
    ListUsers class is used to view all users activity as json response. Registered users can login and view the datas.
      url: hostaddress/login
      
    Register class allows the user to register.
      url : hostaddress/register
      
    Logout class allows the user to logout if logged in.
      url : hostaddress/logout
    
    Models:
    
      Created a new model and manager for managing the datas.
      "username" is configured as its primary key.
    
      
