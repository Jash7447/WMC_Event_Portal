from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    # just for ref: this int and str are called path converters..
    path('<int:year>/<str:month>/', views.home, name="home"),
    path('events', views.list_events, name="list-events"),
    path('add_venue', views.add_venue, name="add-venue"),
    path('list_venues', views.list_venues, name="list-venues"),
    path('show_venues/<venue_id>', views.show_venue, name="show-venue"),
    path('search_venues', views.search_venues, name="search-venues"),
    path('update_venues/<venue_id>', views.update_venue, name="update-venue"),
    path('update_event/<event_id>', views.update_event, name="update-event"),
    path('add_event', views.add_event, name="add-event"),
    path('delete_event/<event_id>', views.delete_event, name="delete-event"),
    path('delete_venue/<venue_id>', views.delete_venue, name="delete-venue"),

]
