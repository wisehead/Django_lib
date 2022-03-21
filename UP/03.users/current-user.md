#1.CurrentUserAPIView

```
CurrentUserAPIView.get
--serializer = UserDisplaySerializer(request.user)
----customer = CustomerDisplaySerializer(many=False, read_only=True)
------bookings = BookingSerializer(many=True, read_only=True)
--------class Meta:model = Booking
------level = serializers.ReadOnlyField()
------class Meta: model = Customer
----role = RoleSerializer(many=True, read_only=True)
------class Meta:model = Role
----class Meta:model = CustomUser
--return Response(serializer.data)


```