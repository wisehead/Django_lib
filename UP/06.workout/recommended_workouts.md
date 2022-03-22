#1.RecommendedWorkoutsView

```
RecommendedWorkoutsView.get
--queryset = ScheduledWorkout.objects.filter(scheduled_time__gte=cutoff)
--//获取属于某个customer的订单
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
--//和workout连接，然后预取该用户的booking相关联的数据
--queryset = serializer_class.setup_eager_loading(
                queryset, request.user.customer
            )
--bookings = queryset._prefetch_related_lookups[0].queryset
--attended_workouts = bookings.filter(attended=1)
--status = self.workout_status(attended_workouts)
--//金牌，银牌课程没有预订限制，其它课程，如果booking过了，则不会出现在allowed_workouts中
--allowed_workouts = self.get_allowed_workouts(orders, bookings)
--scheduled_workouts_serialized = [
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
--recommended_workouts = self.filter_scheduled_workouts(
            scheduled_workouts_serialized
        )
----for scheduled_workout in scheduled_workouts:
------if scheduled_workout["is_bookable"]:
--------recommended_workouts.append(scheduled_workout)        
```