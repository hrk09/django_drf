from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views


schema_view = get_schema_view(
    openapi.Info(
        title = 'Music API',
        default_version = 'v1',
        description = '음악 관련 API 서비스입니다',
    )
)

app_name = 'musics'

urlpatterns = [
    path('docs/', schema_view.with_ui('redoc'), name='api_docs'),
    path('swagger/', schema_view.with_ui('swagger'), name='api_swagger'),
    
    # comment 하나만 가져오는 url
    path('comments/<int:music_pk>/', views.comment_detail, name='comment_detail'),

    # artist 하나만 가져오는 url
    path('artists/<int:music_pk>/', views.artist_detail, name='artist_detail'),

    # 음악 하나만 가져오는 url
    path('musics/<int:music_pk>/', views.music_detail, name='music_detail'),
    
    path('comments/', views.comment_list, name='comment_list'),
    path('artists/',views.artist_list, name='artist_list'),

    # api/v1/musics/
    path('musics/', views.music_list, name='music_list'),  # 모든 음악 가져오는 url    
]
