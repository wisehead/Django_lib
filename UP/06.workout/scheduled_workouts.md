#1.ScheduledWorkoutsView

```
ScheduledWorkoutsView.get
--queryset = ScheduledWorkout.objects.filter(scheduled_time__gte=cutoff)
--if request.user.is_authenticated and hasattr(request.user, "customer"):
----dt_with_grace_p = today - timedelta(days=settings.SUB_GRACE_PERIOD_DAYS)
----orders = Order.objects.select_related("product", "product__category").filter(...)
----queryset = serializer_class.setup_eager_loading(queryset, request.user.customer)
------ScheduledWorkoutSimpleSerializer.setup_eager_loading
--------queryset = queryset.select_related("workout")
--------queryset = queryset.prefetch_related(
                Prefetch(
                    "bookings",
                    queryset=Booking.objects.select_related(
                        "scheduled_workout", "scheduled_workout__workout"
                    ).filter(active=True, owner=customer),
                ),
            )
--------bookings = queryset._prefetch_related_lookups[0].queryset//预取的第一条
--------attended_workouts = bookings.filter(attended=1)//所有的booking中，过滤一下，就是有人参加的attended_workout
--------status = self.workout_status(attended_workouts)
----------level = len(bookings.filter(Q(scheduled_workout__workout__category="CC")))
----------non_celebration_ceremonies = len(bookings.filter(~Q(scheduled_workout__workout__category="CC")))
----------ongoing_progress = non_celebration_ceremonies - 5 * level
----------status = {"ongoing_progress": ongoing_progress, "level": level}
--------allowed_workouts = self.get_allowed_workouts(orders, bookings)
--------scheduled_workouts_serialized = [
            ScheduledWorkoutSimpleSerializer(
                scheduled_workout,
                context={
                    "request": request,
                    "allowed_workouts": allowed_workouts,
                    "bookings": bookings,
                    "status": status,
                },
            ).data
            for scheduled_workout in queryset
        ]
--------return Response(scheduled_workouts_serialized)
```