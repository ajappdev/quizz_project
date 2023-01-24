# DJANGO DECLARATIONS
from django.urls import path, include

# APP DECLARATIONS
import app.views as av


urlpatterns = [
    path('', av.landing_page, name='landing_page'),
    path('administrator/add-question/', av.add_question, name='add_question'),
    path('administrator/settings/', av.admin_settings, name='admin_settings'),
    path('administrator/update-question/<int:pk>/', av.update_question, name='update_question'),
    path('questions/', av.questions, name='questions'),
    path('auth/register/', av.register, name='register'),
    path('ajax-calls/', av.ajax_calls, name='ajax_calls'),
    path('upload-id-file/', av.upload_id_file, name='upload_id_file'),
]


urlpatterns += [
    path('auth/', include('django.contrib.auth.urls')),
]