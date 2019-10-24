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

    # COMMENT 
    path('musics/<int:music_pk>/comments/', views.comments_create, name='comments_create'),
    path('comments/', views.comment_list, name='comment_list'),
    path('comments/<int:comment_pk>/', views.comment_update_delete_detail, name='comment_update_delete_detail'),

    # ARTIST
    # artist 하나만 가져오는 url
    path('artists/<int:artist_pk>/', views.artist_update_delete_detail, name='artist_update_delete_detail'),
    path('artists/',views.artist_list, name='artist_list'),

    # MUSIC
    path('musics/<int:music_pk>/', views.music_update_delete_detail, name='music_update_delete_detail'),

    # api/v1/musics/
    # 모든 음악 가져오는 url
    path('musics/', views.music_list, name='music_list'),   
]
