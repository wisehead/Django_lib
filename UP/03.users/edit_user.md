#1.EditUserAPIView

```
EditUserAPIView.put
--update
----serializer = self.get_serializer(instance, data=request.data, partial=partial)//EditUserSerializer
----serializer.is_valid()
------EditUserSerializer.validate
--------if "password1" in data and "password2" in data:
----------if data["password1"] != data["password2"]:
------------raise serializers.ValidationError(
                    _("The two password fields didn't match.")
                )
----self.perform_update(serializer)
------UpdateModelMixin.perform_update
--------EditUserSerializer.save
----------BaseSerializer.save
------------if self.instance is not None:
--------------self.instance = self.update(self.instance, validated_data)
----------------EditUserSerializer.update
------------------check password.....
------------------CustomUser.save//ModelClass
------------else
--------------self.instance = self.create(validated_data)
----------------ModelSerializer.create
------------------instance = ModelClass._default_manager.create(**validated_data)

```