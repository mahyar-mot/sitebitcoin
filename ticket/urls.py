from django.urls import path
from . import views

app_name = 'ticketapp'

urlpatterns = [
    path('', views.SupportView.as_view(), name='support'),
    path('newticket/', views.NewTicketView.as_view(), name='newticket'),
    path('ticketslistopen/', views.TicketsListViewOpen.as_view(), name='ticketslistopen'),
    path('ticketslistclose/', views.TicketsListViewClose.as_view(), name='ticketslistclose'),
    path('ticketslist/', views.TicketsListView.as_view(), name='ticketslist'),
    path('ticket/<str:category>/<int:pk>/', views.TicketDetailView.as_view(), name='ticketdetail'),
]