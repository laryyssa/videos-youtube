import pytube

# Insira o link do vídeo que deseja baixar
video_url = "https://www.youtube.com/watch?v=yxW5yuzVi8w"

# https://www.youtube.com/watch?v=XQ45gynAUPg

# Cria uma instância do objeto YouTube
yt = pytube.YouTube(video_url)

# Obtém a melhor resolução disponível
video = yt.streams.get_highest_resolution()

# Baixa o vídeo
video.download()
