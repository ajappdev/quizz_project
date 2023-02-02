# DJANGO DECLARATIONS
from django.urls import path, include

# APP DECLARATIONS
import app.views as av


urlpatterns = [
    path('', av.landing_page, name='landing_page'),
    path('administrator/add-question/', av.add_question, name='add_question'),
    path('administrator/bulk-upload-questions/', av.bulk_upload_questions, name='bulk_upload_questions'),
    path('administrator/settings/', av.admin_settings, name='admin_settings'),
    path('administrator/update-question/<int:pk>/', av.update_question, name='update_question'),
    path('administrator/questions/', av.questions, name='questions'),
    path('auth/register/', av.register, name='register'),
    path('ajax-calls/', av.ajax_calls, name='ajax_calls'),
    path('upload-questions-file/', av.upload_questions_file, name='upload_questions_file'),
]


urlpatterns += [
    path('auth/', include('django.contrib.auth.urls')),
]