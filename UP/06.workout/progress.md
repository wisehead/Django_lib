#1.ProgressAPIView

```
ProgressAPIView.get
--customer = self.request.user.customer
--bookings = (
            Booking.objects.select_related(
                "scheduled_workout", "scheduled_workout__workout"
            )
            .filter(
                owner=customer,
                attended=1,
                active=True,
            )
            .order_by("scheduled_workout__scheduled_time")
        )
--level = len(bookings.filter(Q(scheduled_workout__workout__category="CC")))
--non_celebration_ceremonies = len(
            bookings.filter(~Q(scheduled_workout__workout__category="CC"))
        )
--ongoing_progress = non_celebration_ceremonies - 5 * level
--progress = {
            "completed_workouts": [],
            "level": level,
            "ongoing_progress": ongoing_progress,
        }
--for booking in bookings:
----progress["completed_workouts"].append(ProgressSerializer(booking.scheduled_workout).data)
--return Response(progress)
```