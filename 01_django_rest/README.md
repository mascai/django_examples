# Example of usage with PostMan
1. Obtain token
POST http://127.0.0.1:8000/api/v1/auth_token/token/login  
Body  
username <name>  
password <my password>  


2. Change car object
PUT http://127.0.0.1:8000/api/v1/cars/car/detail/2/  

Headers  
Authorization "Token <TOKEN>"  
  
Body (new object values)  
vin 22  
color Yellow  

