import pytube
from pytube import YouTube
from pytube.exceptions import AgeRestrictedError

import os
import traceback

def clear_terminal():
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # Linux ou macOS
        os.system("clear")

def download_video(video_url, path_folder):
    yt = YouTube(video_url)
    video = yt.streams.get_highest_resolution()
    print('Baixando...')
    video.download(path_folder)
    print('Download Completo!') 

def verify_link(url):
    try:
        yt = pytube.YouTube(url)
        return True
    except pytube.exceptions.VideoUnavailable:
        print('Link Inválido!')
        return False

def verify_path(path):
    if os.path.exists(path):
        return True
    else:
        print('Caminho de pasta inválido!')
        return False

def download_helper():
    # path = input('Insira o caminho da pasta: ')
    path_folder = r'C:\Users\larys\OneDrive\Área de Trabalho\videos'
    video_url = input('Insira o Link do vídeo: ')
    
    if verify_link(video_url) and verify_path(path_folder):
        try:
            download_video(video_url, path_folder)              
        except Exception:
            print(traceback.format_exc())
    
    else:
        clear_terminal()

    var = input('Baixar mais vídeos? [0] - Não [1] - Sim')
    return var




def menu():
    print('-------------------')
    print('[0] - Sair\n[1] - Baixar Vídeo\n[2] - Listar Vídeos')
    print('-------------------')

def show_action(user_action):
    print('-------------------')
    print(user_action)
    print('-------------------')

def main():
    while True:
        menu()

        var = input('Digite sua opção: ')
        clear_terminal()

        if var == '0':
            print('Saindo...')
            break
        elif var == '1':
            show_action('BAIXAR VIDEO')
            var = download_helper()
        elif var == '2':
            # listar videos que já tinham e novos
            show_action('LISTAR VIDEOS')
            print('2-listar')
        else:
            print('Opção Inválida! Tente Novamente!')

main()

# download_helper(r'C:\Users\larys\OneDrive\Área de Trabalho\videos')