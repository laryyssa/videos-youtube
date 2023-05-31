import pytube
import os

def limpar_terminal():
    if os.name == "nt":  # Windows
        os.system("cls")
    # else:  # Linux ou macOS
    #     os.system("clear")

def verifyLink(url):
    try:
        yt = pytube.YouTube(url)
        return True
    except pytube.exceptions.VideoUnavailable:
        return False

def dowloadVideo(path_folder):
    var = 1

    while var !=0:
        video_url = input('Insira o Link do vídeo: ')
        
        if verifyLink(video_url):
            yt = pytube.YouTube(video_url)
            video = yt.streams.get_highest_resolution()
            # video.download(output_path='/videos')
            print('Baixando...')
            # path = r'C:\Users\larys\OneDrive\Documentos\Projetos\Videos Youtube\downloaded_videos'
            path = path_folder
            video.download(output_path=path)
            print('Download realizado!')
            break

        else:
            print('Link inválido!')
            var = input('[0] - Sair [1] - Continuar')
            limpar_terminal()

def main():
    var = 1
    while var != 0:
        print('-------------------')
        print('[0] - Sair\n[1] - Baixar Vídeo')
        print('-------------------')
        var = input('Digite sua opção: ')
        limpar_terminal()

        if var == '0':
            print('Saindo...')
            break
        elif var == '1':
            limpar_terminal()
            # path = input('Insira o caminho da pasta: ')
            path = r'C:\Users\larys\OneDrive\Documentos\Projetos\Videos Youtube\downloaded_videos'
            dowloadVideo(path)
        elif var == '2':
            # listar videos que já tinham e novos
            print('2-listar')
        else:
            print('Opção Inválida!')

main()