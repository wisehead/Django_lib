#1.class VerifyEmailView
##1.1 post

```
post
--serializer.is_valid(raise_exception=True)//VerifyEmailSerializer
--self.kwargs['key'] = serializer.validated_data['key']
--confirmation = self.get_object()
----ConfirmEmailView.get_object
------key = self.kwargs["key"]
------emailconfirmation = EmailConfirmationHMAC.from_key(key)
--------EmailConfirmationHMAC(EmailAddress.objects.get(pk=pk, verified=False))
--confirmation.confirm(self.request)//EmailConfirmationHMAC
----email_address = self.email_address
----get_adapter(request).confirm_email(request, email_address)
------DefaultAccountAdapter.confirm_email
------email_address.verified = True                              
------email_address.set_as_primary(conditional=True)             
------email_address.save()                                       
```

