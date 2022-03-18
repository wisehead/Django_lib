#1.registration

###(1) class CustomRegisterView

```python
class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer
    queryset = CustomUser.objects.all()

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        # raise APIException("You are toast!")
        if not serializer.is_valid():
            return handle_bad_request(serializer)

        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(
            self.get_response_data(user),
            status=status.HTTP_201_CREATED,
            headers=headers,
        )
```

```
create
--RegisterView.perform_create
--CustomRegisterSerializer.save
----adapter = get_adapter()
------self._setting("ADAPTER", "allauth.account.adapter.DefaultAccountAdapter")
----DefaultAccountAdapter.new_user
------django_apps.get_model(settings.AUTH_USER_MODEL, require_ready=False)//AUTH_USER_MODEL = "users.CustomUser"
----CustomRegisterSerializer.get_cleaned_data
------RegisterSerializer.get_cleaned_data
--------return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', '')
        }
----------BaseSerializer.validated_data
------------self.run_validation(self.initial_data)        
```

###(2) class CustomRegisterSerializer(RegisterSerializer)

```
save
--adapter = get_adapter()
--user = adapter.new_user(request)
----get_user_model
------django_apps.get_model(settings.AUTH_USER_MODEL, require_ready=False)//AUTH_USER_MODEL = "users.CustomUser"
--adapter.save_user(request, user, self)
----user.save()
--self.custom_signup(request, user)
--setup_user_email(request, user, [])

```