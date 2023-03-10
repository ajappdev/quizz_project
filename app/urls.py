# DJANGO DECLARATIONS
from django.urls import path, include

# APP DECLARATIONS
import app.views as av


urlpatterns = [
    ############################## UNCLASSED PAGES ############################
    path('', av.landing_page, name='landing_page'),
    path('download-excel-template/', av.download_excel_template, name='download_excel_template'),
    ######################### ADMIN PAGES #####################################
    path('administrator/add-question/', av.add_question, name='add_question'),
    path('administrator/bulk-upload-questions/', av.bulk_upload_questions, name='bulk_upload_questions'),
    path('administrator/settings/', av.admin_settings, name='admin_settings'),
    path('administrator/update-question/<int:pk>/', av.update_question, name='update_question'),
    path('administrator/questions/', av.questions, name='questions'),
    path('administrator/initial-settings/', av.initial_settings_upload, name='initial_settings_upload'),
    path('administrator/dashboard/', av.dashboard_admin, name='dashboard_admin'),
    ######################### STUDENT PAGES ###################################
    path('student/dashboard/', av.dashboard_student, name='dashboard_student'),
    ######################### QUIZZ PAGES ###################################
    path('quizz/', av.quizz, name='quizz'),
    ######################### AUTH PAGES ######################################
    path('auth/register/', av.register, name='register'),
    ######################### AJAX PAGES ######################################
    path('ajax-calls/', av.ajax_calls, name='ajax_calls'),
    path('upload-questions-file/', av.upload_questions_file, name='upload_questions_file'),
]


urlpatterns += [
    path('auth/', include('django.contrib.auth.urls')),
]