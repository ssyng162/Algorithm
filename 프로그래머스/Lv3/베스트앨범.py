# 프로그래머스: 베스트앨범

def solution(genres, plays):
    genre_total = {}
    genre_songs = {}
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_total[genre] = genre_total.get(genre, 0) + play
        genre_songs.setdefault(genre, []).append((i, play))
            
    for music_list in genre_songs.values():
        music_list.sort(key=lambda x: (-x[1], x[0]))
        
    sorted_genres = sorted(genre_total.items(), key=lambda x: -x[1])
    
    result = []
    for genre, _ in sorted_genres:
        music_list = genre_songs[genre]
        result.extend([idx for idx, _ in music_list[:2]])
        
    return result
