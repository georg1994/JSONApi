from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from rapi.models import UserProfile
from django.contrib.auth import get_user_model, authenticate, login, logout
User = get_user_model()

#api-registration
class UserRegister(DjangoResource):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'email': 'user.email',
        'password': 'user.password',
        'user_type': 'user_type',
    })
    
    def is_authenticated(self):
        return True
    
    #Список пользователей GET /api/account/register/
    def list(self):
        return UserProfile.objects.all()

    #Создание профиля пользователя POST /api/account/register/
    def create(self):
        try:
            UserProfile.objects.create(
                user=User.objects.create_user(username=self.data['email'],
                                          email=self.data['email'],
                                          password=self.data['password']),
                user_type=self.data['user_type']
                )
        except:
            print('User already exist or invalid JSON')
            
    # Изменение профиля пользователя PUT /api/account/register/<id>/
    def update(self, pk):
        try:
            usr = UserProfile.objects.get(id=pk)
            user = User.objects.get(id=pk)
            user.password = User.objects.update(password=self.data['password'])
            usr.user_type = self.data['user_type']
            usr.save()
            
        except UserProfile.DoesNotExist:
            usr = UserProfile()
            user = User()
            user.username = User.objects.get_or_create(username=self.data['username'])
            user.email = User.objects.get_or_create(email=self.data['email'])
            user.password = User.objects.get_or_create(password=self.data['password'])
            usr.user_type = self.data['user_type']
            usr.save()
            
        return usr
    
    #Удаление профиля пользователя DELETE /api/account/register/<id>/
    def delete(self, pk):
        UserProfile.objects.get(id=pk).delete()

#api-login
class UserLogin(DjangoResource):
    preparer = FieldsPreparer(fields={
        'email': 'user.email',
        'password': 'user.password',
        'user_type': 'user_type',
    })
    
    def is_authenticated(self):
        return True

    #Выполенение входа POST /api/account/login/
    def create(self):
        username = self.data['email']
        password = self.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                print("LOGIN OK")
            else:
                print ('Troubles with login')
        else:
            print('invalidLogin')


#api-logout
class UserLogout(DjangoResource):
    preparer = FieldsPreparer(fields={
        'email': 'user.email',
        'password': 'user.password',
        'user_type': 'user_type',
    })

    def is_authenticated(self):
        return True

    #Выполенение выхода POST /api/account/logout/
    def create(self):
        logout(self.request)
        print("LOGOUT OK")

