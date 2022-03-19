#registration

#1. class CustomRegisterView

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

##1.1 create
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
----if self.cleaned_data["is_company_admin"]:
------companies = Company.objects.all()
------for company in companies:
--------if self.validated_data.get("admin_id", "") == str(company.admin_id):
----DefaultAccountAdapter.save_user
------user.save() //users.CustomUser
----setup_user_email(request, user, [])
----roles = Role.objects.all()
----self.invite_code = Code.objects.filter(code=self.cleaned_data["code"]).first()
----if self.is_private_user and not self.is_company_employee:
------if self.no_code://注册未指定code
--------customer = Customer.objects.create(
                    user=user,
                    free_workouts_left=settings.NUM_FREE_WORKOUTS,
                )
------elif self.is_new_code://注册指定code
--------customer = Customer.objects.create(
                    user=user,
                    invite_code=self.invite_code,
                    customer_category=self.invite_code.customer_category,
                    free_workouts_left=self.invite_code.free_workouts,
                )
--------if not self.invite_code.linked_product == None:
----------order = Order.objects.create(
                        customer=customer,
                        product=self.invite_code.linked_product,
                        expires=timezone.now()
                        + relativedelta(months=self.invite_code.free_months),
                        completed=True,
                    )
----------order.save()
--------user.roles.add(2)
--------customer.save()
----if self.is_company_employee and self.is_private_user:
------company = self.invite_code.linked_company
------customer = Customer.objects.create(
                user=user,
                invite_code=self.invite_code,
                customer_category=self.invite_code.customer_category,
                company_new=company,
                free_workouts_left=self.invite_code.free_workouts,
            )
------order = Order.objects.create(
                customer=customer,
                product=self.invite_code.linked_product,
                expires=timezone.now()
                + relativedelta(months=self.invite_code.free_months),
                completed=True,
            )
------customer.save()
------order.save()
----if self.cleaned_data["is_company_admin"]:
------user.roles.add(4)
```

##1.2 validate_code

```
validate_code
--if code == None or code == "":
----self.is_private_user = True           
----self.is_company_employee = False      
----self.is_new_code = False              
----self.no_code = True                   
----return code                           
--else
----invite_code = Code.objects.filter(code=code).first()
----if (hasattr(invite_code, "linked_company") and not invite_code.linked_company is None):
------self.is_company_employee = True
----else
------self.is_company_employee = False
----self.is_private_user = True
----self.is_new_code = True
----self.no_code = False
```


#2 class CustomRegisterSerializer(RegisterSerializer)

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