from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

# artist와 1:N 구조
# artist.music_set 쓰는 대신, related_name 설정
class Music(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='musics')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


# Music과 1:N 구조 생성
class Comment(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()

    def __str__(self):
        return f'{self.music.pk}번 음악의 {self.pk}번 댓글'
    


