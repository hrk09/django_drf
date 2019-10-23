from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Music, Artist, Comment
from .serializers import Musicserializer, Artistserializer, Commentserializer, ArtistDetailserializer


@api_view(['GET'])  # from rest_framework.decorators import api_view; get 요청으로 들어오면 music 리스트를 보여준다
def music_list(request):
    musics = Music.objects.all()
    # json 파일 형식으로 변환시켜서 보여주는 것(serializer)
    serializer = Musicserializer(musics, many=True)  # 여러개면 many=True
    # serializer 에서 데이터 꺼내서 Response(응답) 한다.
    return Response(serializer.data)


@api_view(['GET'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    # 한 개의 데이터만 보여주면 되므로 many=True가 필요 없음
    # id 값에 music 정보까지 보여주는 serializer
    serializer = ArtistDetailserializer(music)
    return Response(serializer.data)

@api_view(['GET'])
def artist_detail(requst, music_pk):
    artist = get_object_or_404(Artist, pk=music_pk)
    serializer = ArtistDetailserializer(artist)
    return Response(serializer.data)

@api_view(['GET'])
def comment_detail(request, music_pk):
    comment = get_object_or_404(Comment, pk=music_pk)
    # 한 개의 데이터만 보여주면 되므로 many=True가 필요 없음
    serializer = Commentserializer(comment)
    return Response(serializer.data)

@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = Artistserializer(artists, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = Commentserializer(comments, many=True)
    return Response(serializer.data)


