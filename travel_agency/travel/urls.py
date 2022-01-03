from django.urls import path
from travel import views

app_name = 'travel'

urlpatterns = [
    path('hotels/', views.hotel_booking, name = 'hotels'),
    path('hotels/<int:pk>', views.make_booking, name = 'make_booking'),
    path('tours/', views.tour_reservation, name = 'tours'),
    path('tours/details/<int:pk>', views.tour_details, name = 'tour_details'),
    path('flight/', views.flight_booking, name = 'flight'),
    path('previous/', views.previous_trips, name = 'previous'),
    path('previous/<int:pk>', views.give_feedback, name = 'give_feedback'),
    path('friends/', views.friends, name = 'friends'),
    # Booking( Employee )
    path('manage_booking/', views.manage_booking, name = 'manage_booking'),
    path('manage_booking/<int:b_id>/<int:h_id>/<int:r_id>', views.booking_detail, name = 'booking_detail'),
    path('manage_booking/update', views.update_booking, name = 'update_booking'),
    # Reservation( Employee )
    path('manage_reservation/', views.manage_reservation, name = 'manage_reservation'),
    path('manage_reservation/<int:r_id>/<int:t_id>/<int:e_id>/<int:c_id>', views.reservation_detail, name = 'reservation_detail'),
    path('manage_reservation/update', views.update_reservation, name = 'update_reservation'),

    path('tours/assign/<int:pk>', views.assign_guide, name = 'assign_guide'),
    path('hotels/<int:pk>/<int:r_id>/', views.done_booking, name = 'done_booking'),
    path('profile/', views.my_profile, name = 'profile'),
    path('login/', views.login, name = 'login'),
    path('register/', views.register_c, name = 'register'),
    path('register_e_g/', views.register_e_g, name = 'register_e_g'),
    path('logout/', views.logout, name = 'logout'),
    path('statistics/', views.statistics, name = 'statistics'),
]
