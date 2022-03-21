#1.PersonalBookingsAPIView

```
PersonalBookingsAPIView.get_queryset
--customer = self.request.user.customer
--bookings = Booking.objects.filter(
            scheduled_workout__scheduled_time__gte=now, owner=customer, active=True
        )
--return bookings
```