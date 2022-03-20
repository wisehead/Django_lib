#1.LogoutView

```
post
--logout
----request.user.auth_token.delete()
----django_logout(request)
----response = Response(
            {'detail': _('Successfully logged out.')},
            status=status.HTTP_200_OK,
        )
----unset_jwt_cookies(response)
----message = _(
                    'Neither cookies or blacklist are enabled, so the token '
                    'has not been deleted server side. Please make sure the token is deleted client side.',
                )
----response.data = {'detail': message}
----response.status_code = status.HTTP_200_OK
----return response
```