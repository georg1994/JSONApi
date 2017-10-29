# JSONApi
JSON Api for registration, login and logout users

1. Выполнить в первой вкладке терминала:
  python3 manage.py runserver
  
2. В новой вкладке терминала:

Регистрация пользователя:

curl -X POST -H "Content-Type: application/json" -d '{"email":"testemail@example.ru", "password":"asd1234", "user_type": false}' http://127.0.0.1:8000/api/account/register/

Login:

curl -X POST -H "Content-Type: application/json" -d '{"email":"testemail@example.ru", "password":"asd1234", "user_type": false}' http://127.0.0.1:8000/api/account/login/

Logout:

curl -X POST -H "Content-Type: application/json" -d '{"email":"testemail@example.ru", "password":"asd1234", "user_type": false}' http://127.0.0.1:8000/api/account/logout/

Изменение данных пользователя (возможно привязать к другому урлу, но пока так):

curl -X PUT -H "Content-Type: application/json" -d '{"email":"testemail@example.ru", "password":"asd123", "user_type": true}' http://127.0.0.1:8000/api/account/register/id/
  
Вместо id - пишем айди пользователя :)
Таким образом изменили тип пользователя на True
 
Удалить пользователя: 

curl -X DELETE http://127.0.0.1:8000/api/account/register/id/
  
Вместо id - пишем айди пользователя :)
  
Вывести список пользователей (опять же для теста привязал к register, в продакшн такое пускать нельзя :)):

curl -X GET http://127.0.0.1:8000/api/account/register/
