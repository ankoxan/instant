from django.urls import path
from . import views
from .views import (
	ShareListView,
	ShareDetailView,
	SearchShareListView,
	# TransportPaperListView,
	# BankPaperListView,
	# share_createview
	)


urlpatterns = [
    path('category/', ShareListView.as_view()),
    path('<pk>/', ShareDetailView.as_view()),
    path('category/<slug>/', SearchShareListView.as_view()),
    # path('create/', views.share_createview),
    # path('category/transport/', TransportPaperListView.as_view()),
    # path('category/bank/', BankPaperListView.as_view()),
]
