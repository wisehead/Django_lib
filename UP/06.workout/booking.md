#1.BookingCreateAPIView

```
BookingCreateAPIView.create
--serializer_class = BookingSerializer
--owner = self.request.user.customer
--scheduled_workout_slug = self.kwargs.get("slug")
--scheduled_workout = ScheduledWorkout.objects.filter(slug=scheduled_workout_slug)
--scheduled_workout = ScheduledWorkoutSimpleSerializer.setup_eager_loading(
            scheduled_workout, request.user.customer
        ).first()
--bookings = Booking.objects.filter(active=True, owner=owner)
--if owner.free_workouts_left > 0:
----request.data["used_free_workout"] = True
--else
----request.data["used_free_workout"] = False
--request.data["scheduled_workout"] = scheduled_workout.pk
--request.data["owner"] = owner.pk 
--serializer = self.get_serializer(data=request.data)
--serializer.is_valid(raise_exception=True)
--sw_serialized = self.get_scheduled_workout_serialized(request, scheduled_workout, bookings)     
----orders = Order.objects.select_related("product", "product__category").filter(
            Q(customer=request.user.customer),
            Q(expires__gte=dt_with_grace_p) | Q(expires=None),
            Q(stripe_subscription_status="active")
            | Q(stripe_subscription_status="")
            | Q(stripe_subscription_status=None),
            Q(completed=True),
        )
----allowed_workouts = self.get_allowed_workouts(orders, bookings)
----attended_workouts = Booking.objects.filter(active=True, owner=request.user.customer, attended=1) 
----status = self.workout_status(attended_workouts)
----scheduled_workout_serialized = ScheduledWorkoutSimpleSerializer(
            scheduled_workout,
            context={
                "request": request,
                "allowed_workouts": allowed_workouts,
                "bookings": bookings,
                "status": status,
            },
        ).data
----return scheduled_workout_serialized  
--self.perform_create(serializer)
----BookingSerializer.save
------Booking.save      
```