# WR-pageing





## API Doucmentation
- /login  <br>
  method: POST <br>
  parameter = username, password;<br> 
  returns: status, message, (token)<br><br>
  
- /createUser <br>
  method: POST <br>
  parameter: access_token, token_owner, user_info {name, vorname, klasse, schluessel, ausbildungen, aufgaben, password}
  returns: status, message<br><br>
  
- /editUser <br>
  method: PATCH <br>
  parameter: access_token, token_owner, user, category, value
  returns: status, message<br><br>
  
- /addTask <br>
  method: POST <br>
  parameter: access_token, token_owner, name, aufgabe, (date), (treffpunkt)<br>
  returns: status, message <br><br>
  
- /acceptTask <br>
  method: PATCH <br>
  parameter: access_token, token_owner, auftragsID <br>
  returns: status, message <br> <br>
  
- /listAllTasksForTechniker <br>
  method: POST <br>
  parameter: access_token, token_owner
  returns: status, (message), (aufgaben)<br><br>
  
- /closeTask <br>
  method: DELETE <br>
  parameter: access_token, token_owner <br>
  returns: status, message <br> <br>
  
- /getOnlineTechniker <br>
  method: POST <br>
  parameter: access_token, token_owner <br>
  returns: status, (message), (techniker) <br> <br>
  
- /getOnlineTechnikerWithoutTask <br>
  method: POST <br>
  parameter: access_token, token_owner <br>
  returns: status, (message), (techniker) <br> <br>
  
- /fastpageing <br>
  method: POST <br>
  parameter: access_token, token_owner, call_type, call_name
  returns: status, message <br> <br>
  
- /logout <br>
  method: POST <br>
  parameter: access_token, token_owner <br>
  returns: status, message <br> <br>
  
- /addAusbildungToTechniker <br>
  method: PATCH <br>
  parameter: access_token, token_owner, username, ausbildung <br>
  returns: status, message <br> <br>
  
- /addAufgabeToTechniker <br>
  method: PATCH <br>
  parameter: access_token, token_owner, username, aufgabe <br>
  returns: status, message <br> <br>
  
