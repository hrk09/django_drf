from rest_framework import serializers
from .models import Music, Artist, Comment

class Musicserializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist_id',)


class Artistserializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name', )


class ArtistDetailserializer(Artistserializer):
# class ArtistDetailserializer(serializers.ModelSerializer): 도 가능
    musics = Musicserializer(many=True)
    # 음악을 총 몇 개 가지고 있는 지
    musics_count = serializers.IntegerField(source='musics.count') 

    class Meta(Artistserializer.Meta):
        # id, name 뒤에 musics 추가하는 방식
        fields = Artistserializer.Meta.fields + ('musics', 'musics_count', )


class Commentserializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'music_id', )
