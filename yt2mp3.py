import youtube_dl

def main():
    url = input("Enter youtube video url: ").strip()
    name = input("What do you wanna name the file? ")
    
    ytdl_options = {
        'format':'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'age_limit': 100,
        'noplaylist': False,
        'progress_hooks': [hook],
        'outtmpl': "{}.mp3".format(name.replace(" ", "_"))
    }

    with youtube_dl.YoutubeDL(ytdl_options) as ydl:
        ydl.download([url])

def hook(download):
    if download['status'] == 'downloading':
        print('     Downloading..........')
    if download['status'] == 'finished':
        print('Finished!')

if __name__=='__main__':
    main()