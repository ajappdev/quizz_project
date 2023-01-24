# DJANGO DECLARATIONS
from django.urls import path, include

# APP DECLARATIONS
import app.views as av


urlpatterns = [
    path('', av.landing_page, name='landing_page'),
    path('administrator/add-question/', av.add_question, name='add_question'),
    path('administrator/update-question/<int:pk>/', av.update_question, name='update_question'),
    path('administrator/add-country/', av.add_country, name='add_country'),
    path('administrator/update-country/<int:pk>/', av.update_country, name='update_country'),
    path('administrator/add-category/', av.add_category, name='add_category'),
    path('administrator/update-category/<int:pk>/', av.update_category, name='update_category'),
    path('administrator/add-sub-category/', av.add_sub_category, name='add_sub_category'),
    path('administrator/update-sub-category/<int:pk>/', av.update_sub_category, name='update_sub_category'),
    path('administrator/add-region/', av.add_region, name='add_region'),
    path('administrator/update-region/<int:pk>/', av.update_region, name='update_region'),
    path('questions/', av.questions, name='questions'),
    path('administrator/regions/', av.regions, name='regions'),
    path('administrator/countries/', av.countries, name='countries'),
    path('administrator/categories/', av.categories, name='categories'),
    path('administrator/sub-categories/', av.sub_categories, name='sub_categories'),
    path('auth/register/', av.register, name='register'),
    path('ajax-calls/', av.ajax_calls, name='ajax_calls'),
    path('upload-id-file/', av.upload_id_file, name='upload_id_file'),

]


urlpatterns += [
    path('auth/', include('django.contrib.auth.urls')),
]