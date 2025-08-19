from django.urls import path
from .views import job_list_view, job_detail_view, apply_for_job, JobUpdateView, JobDeleteView, JobCreateView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'jobs'

urlpatterns = [
    path('', job_list_view, name='job_list'),
    path('create/', JobCreateView.as_view(), name='job_create'),
    path('<int:pk>/', job_detail_view, name='job_detail'),
    path('<int:pk>/update/', JobUpdateView.as_view(), name='job_update'),
    path('<int:pk>/delete/', JobDeleteView.as_view(), name='job_delete'),
    path('<int:pk>/apply/', apply_for_job, name='apply_for_job'),
    path('accounts/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
]