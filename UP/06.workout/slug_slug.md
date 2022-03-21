#1.ScheduledWorkoutDetailAPIView

```
ScheduledWorkoutDetailAPIView.get
--serializer_class = ScheduledWorkoutSimpleSerializer
--queryset = ScheduledWorkout.objects.filter(slug=self.kwargs["slug"])//过滤特定的schedule
--if request.user.is_authenticated and hasattr(request.user, "customer"):
--dt_with_grace_p = today - timedelta(days=settings.SUB_GRACE_PERIOD_DAYS)
--orders = Order.objects.select_related(
                "product", "product__category"
            ).filter(
                Q(customer=request.user.customer),
                Q(expires__gte=dt_with_grace_p) | Q(expires=None),
                Q(stripe_subscription_status="active")
                | Q(stripe_subscription_status="")
                | Q(stripe_subscription_status=None),
                Q(completed=True),
            )
--queryset = serializer_class.setup_eager_loading(
                queryset, request.user.customer
            )
--bookings = queryset._prefetch_related_lookups[0].queryset         
--attended_workouts = bookings.filter(attended=1)                   
--status = self.workout_status(attended_workouts)                   
--allowed_workouts = self.get_allowed_workouts(orders, bookings)    
--return Response(
            ScheduledWorkoutSimpleSerializer(
                queryset.first(),
                context={
                    "request": request,
                    "allowed_workouts": allowed_workouts,
                    "bookings": bookings,
                    "status": status,
                },
            ).data
        )                                                                    
```