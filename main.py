import pytube
from pytube import YouTube
# from pytube.exceptions import AgeRestrictedError, VideoUnavailable
import requests

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

    print(f"Baixando: {yt.title}")
    video.download(path_folder)
    print('Download Completo!\n') 

def verify_link(link):
    try:
        response = requests.head(link)
        return response.status_code == 200
    except requests.RequestException:
        print('Link Inválido!\n')
        return False

def verify_path(path):
    if os.path.exists(path):
        return True
    else:
        print('Caminho de pasta inválido!\n')
        return False

def download_helper():
    # path_folder = input('Insira o caminho da pasta: ')
    path_folder = r'C:\Users\larys\OneDrive\Área de Trabalho\videos'
    video_url = input('Insira o Link do vídeo: ')
    
    if verify_link(video_url) and verify_path(path_folder):
        try:
            # download_video(video_url, path_folder)   
            print('baixou confia')           
        except Exception:
            print('Erro ao baixar o vídeo!\n')
            print(traceback.format_exc())
    
    return True




def menu():
    print('[0] - Sair\n[1] - Baixar Vídeo\n[2] - Listar Vídeos')
    print('-------------------')

def show_action(user_action):
    print('-------------------')
    print(user_action)
    print('-------------------')

def main():
    while True:
        clear_terminal()
        show_action('VIDEO DOWNLOADER')
        menu()

        var = input('Digite sua opção: ')
        clear_terminal()

        if var == '0':
            print('Saindo...')
            break

        elif var == '1':
            show_action('BAIXAR VIDEO')
            download_helper()
            input('Pressione ENTER para continuar...')

        elif var == '2':
            # listar videos que já tinham e novos
            show_action('LISTAR VIDEOS')
            print('Listando...')
            input('Pressione ENTER para continuar...')

        else:
            print('Opção Inválida! Tente Novamente!\n')
            input('Pressione ENTER para continuar...')

main()

# download_helper(r'C:\Users\larys\OneDrive\Área de Trabalho\videos')