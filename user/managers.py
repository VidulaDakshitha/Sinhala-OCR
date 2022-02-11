from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migration = True

    def _create_user(self, id, password, **extra_fields):

        if not id:
            raise ValueError('The given phone number must be set')
        id = id
        user = self.model(id=id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

