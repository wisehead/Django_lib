#1.class LoginView

##1.1 post

```
post
--self.request = request
--self.serializer = self.get_serializer(data=self.request.data)
--self.serializer.is_valid(raise_exception=True)
----BaseSerializer.is_valid
------Serializer.run_validation
--------Serializer.run_validators
--------LoginSerializer.validate
--------LoginSerializer.get_auth_user
----------get_auth_user_using_allauth
------------_validate_email
--------------authenticate
--------------django.contrib.auth.authenticate
------------_validate_username
------------_validate_username_email
--self.login()
--self.get_response()
```

##1.2 login

```
login
--self.user = self.serializer.validated_data['user']
--get_token_model
--self.token = create_token(token_model, self.user, self.serializer)
--process_login
----login//django.contrib.auth
------request.session[SESSION_KEY] = user._meta.pk.value_to_string(user)
------request.session[BACKEND_SESSION_KEY] = backend
------request.session[HASH_SESSION_KEY] = session_auth_hash
------request.user = user
------rotate_token(request)
```
