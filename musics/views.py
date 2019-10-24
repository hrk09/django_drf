from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Music, Artist, Comment
from .serializers import Musicserializer, Artistserializer, Commentserializer, ArtistDetailserializer


# from rest_framework.decorators import api_view; get 요청으로 들어오면 music 리스트를 보여준다
@api_view(['GET'])
def music_list(request):

    # (번외)만약 artist_pk 가 Query params 로 넘어온다면 artist_pk 로 필터링 한 값만 응답한다
    # 그렇지 않으면 전체 음악을 응답함(json placeholder)
    params = {}
    artist_pk = request.GET.get('artist_pk')

    if artist_pk is not None:
        params['artist_id'] = artist_pk
    musics = Music.objects.filter(**params)

    # musics = Music.objects.all()
    # json 파일 형식으로 변환시켜서 보여주는 것(serializer)
    serializer = Musicserializer(musics, many=True)  # 여러개면 many=True
    # serializer 에서 데이터 꺼내서 Response(응답) 한다.
    return Response(serializer.data)

# /api/v1/musics/3/ ==> 한 줄로 method별로 detail/update/delete 중 하나 실행하도록 하는 함수!
@api_view(['GET', 'PUT', 'DELETE'])
def music_update_delete_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)

    # method 별로 분기하는 작업
    if request.method == 'GET':
        serializer = Musicserializer(music)
        # 한 개의 데이터만 보여주면 되므로 many=True가 필요 없음
        # id 값에 music 정보까지 보여주는 serializer
        return Response(serializer.data)        
    elif request.method == 'PUT':
        # 수정
        serializer = Musicserializer(data=request.data, instance=music)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:  # 삭제
        music.delete()
        return Response({'message': 'Music has been deleted!'})

# @api_view(['GET'])
# def artist_detail(requst, artist_pk):
#     artist = get_object_or_404(Artist, pk=artist_pk)
#     serializer = ArtistDetailserializer(artist)
#     return Response(serializer.data)

@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = Artistserializer(artists, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def artist_update_delete_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)

    # method 별로 분기하는 작업
    if request.method == 'GET':
        serializer = ArtistDetailserializer(artist)
        # 한 개의 데이터만 보여주면 되므로 many=True가 필요 없음
        # id 값에 artist 정보까지 보여주는 serializer
        return Response(serializer.data)        
    elif request.method == 'PUT':
        # 수정
        serializer = ArtistDetailserializer(data=request.data, instance=artist)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:  # 삭제
        artist.delete()
        return Response({'message': 'Artist has been deleted!'})


@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = Commentserializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_update_delete_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.method == 'GET':
        serializer = Commentserializer(comment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = Commentserializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:  # 삭제
        comment.delete()
        return Response({'message': 'Comment has been deleted!'})


@api_view(['POST'])
def comments_create(request, music_pk):
    # request.data == 사용자가 보냈던 데이터
    # print(request.data)
    serializer = Commentserializer(data=request.data)
    if serializer.is_valid(raise_exception=True):  # 사용자가 넘겨준 값이 유효하다면,
        # raise_exception ; 검증 실패하면 400 Bad Request 오류 발생함
        serializer.save(music_id=music_pk)  # commit=False 안 넣어줘도 됨(다름)
    return Response(serializer.data)  # 사용자가 방금 작성한 데이터를 보여주겠다.

        