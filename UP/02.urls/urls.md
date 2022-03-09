#1.urls

```python
	path("admin/", admin.site.urls),
	path("api/rest-auth/password-reset/", PasswordResetView.as_view()),
    path(
        "api/rest-auth/password-reset-confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),	
    path("api/", include("users.api.urls")),
    path("api/", include("mental_workouts.api.urls")),
    path("api/", include("ratings.api.urls")),
    path("api/", include("store.api.urls")),
    path("webhook", WebhookCreateAPIView.as_view(), name="webhook"),
    path("api-auth/", include("rest_framework.urls")),
    path("account-confirm-email/<str:key>/", ConfirmEmailView.as_view()),
    path(
        "api/rest-auth/registration/", ensure_csrf_cookie(CustomRegisterView.as_view())
    ),
    path("verify-email/", VerifyEmailView.as_view(), name="rest_verify_email"),
    path(
        "account-confirm-email/",
        VerifyEmailView.as_view(),
        name="account_email_verification_sent",
    ),
    re_path(
        r"^account-confirm-email/(?P<key>[-:\w]+)/$",
        VerifyEmailView.as_view(),
        name="account_confirm_email",
    ),
    path("api/rest-auth/login/", LoginView.as_view()),
    path("api/rest-auth/logout/", LogoutView.as_view()),
    re_path(
        r"^.*$",
        RedirectView.as_view(url="https://upotential.se", permanent=False),
        name="entry-point",
    ),            
```

#2.api

```python
    path("api/", include("users.api.urls")),
    path("api/", include("mental_workouts.api.urls")),
    path("api/", include("ratings.api.urls")),
    path("api/", include("store.api.urls")),
```

#3.api/user
```python
    path("user/", CurrentUserAPIView.as_view(), name="current-user"),
    path("edit_user/<int:pk>/", EditUserAPIView.as_view(), name="edit-user"),
```

#4.api/mental_workouts

```python
    path("", include(router.urls)),
    path("<int:pk>/", fsv.WorkoutDetailAPIView.as_view(), name="workout-detail"),
    path(
        "mental_workouts/",
        fsv.WorkoutListAPIView.as_view(),
        name="mental-workouts",
    ),
    path(
        "scheduled_workouts/",
        fsv.ScheduledWorkoutsView.as_view(),
        name="scheduled-workouts",
    ),
    path(
        "recommended_workouts/",
        fsv.RecommendedWorkoutsView.as_view(),
        name="recommended-workouts",
    ),
    path(
        "scheduled_workouts/personal_bookings/",
        fsv.PersonalBookingsAPIView.as_view(),
        name="personal-bookings",
    ),
    path(
        "progress/",
        fsv.ProgressAPIView.as_view(),
        name="progress-2",
    ),
    path(
        "scheduled_workouts/<slug:slug>/",
        fsv.ScheduledWorkoutDetailAPIView.as_view(),
        name="scheduled-workout-detail",
    ),
    path(
        "scheduled_workouts/<slug:slug>/booking/",
        fsv.BookingCreateAPIView.as_view(),
        name="scheduled-workout-booking",
    ),
    path(
        "scheduled_workouts/<slug:slug>/booking/<int:pk>/",
        csrf_exempt(fsv.BookingDetailAPIView.as_view()),
        name="scheduled-workout-booking-detail",
    ),
```

