from pytube import YouTube
from pytube.cli import on_progress
import os, pyinputplus as pyip


def createdir(path):
    os.makedirs(path, exist_ok = True)
    print(f'{path} is Available\n')

def getDetails(link):
    try:
        ytlink = YouTube(link)
        yt360p = ytlink.streams.filter(progressive=True, file_extension='mp4', res='360p').first()
        yt720p = ytlink.streams.filter(progressive=True, file_extension='mp4', res='720p').first()
        print(f'Video Title: {ytlink.title}')
        print(f'Creator: {ytlink.vid_info["videoDetails"]["author"]}')
        print(f'Number of views: {ytlink.views}')
        print(f'File size: {yt360p.filesize_mb}MB - 360p')
        print(f'File size: {yt720p.filesize_mb}MB - 720p')
    except Exception as err:
        print(f'An Error occured: {err}')
        exit()

    

def ytdownload(link, ext='mp4', res='720p'):

    path = f'{os.path.expanduser("~")}/Downloads/Pytubes/'
    createdir(path)

    ytlink = YouTube(link, on_progress_callback=on_progress)
    ytinfo = ytlink.streams.filter(progressive=True, file_extension=ext, res=res).first()
    print(f'\nVideo File Size: {ytinfo.filesize_mb}MB\n')

    print(f'Downloading {ytlink.title} to {path}\n')
    if os.path.exists(f'{path}/{ytlink.title}.mp4'):
        print('Video Already exists')
    else:
        ytinfo.download(path)
        print('Download Complete ')

def userPrompt():
    prompt = pyip.inputYesNo('\nDo you wish to download this file (Y/n): ', blank=True)
    if prompt == '':
        prompt = 'yes'

    if prompt == 'yes':
        res = pyip.inputMenu(['360p', '720p'], prompt='\nChoose your preferred resolution (Default is 720p):\n', numbered=True, blank=True)
        if res == '':
            res = '720p'
        ytdownload(link, res=res)
    else:
        exit()

if __name__ == '__main__':
    try:
        link = pyip.inputURL('\nPaste your Youtube Link: ')
        getDetails(link)
        userPrompt()
    except KeyboardInterrupt:
        print('\n\nExiting...')
