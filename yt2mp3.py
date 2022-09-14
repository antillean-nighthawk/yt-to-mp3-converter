import youtube_dl
import sys, os

def main():
    urls = []
    names = []
    choice = intro()

    if choice == 'A' or choice == 'a':
        url = input("Enter youtube video url: ").strip()
        name = input("What do you wanna name the file? ")
        urls.append(url)
        names.append(name)
    elif choice == 'B' or choice == 'b':
        print("File format should be {url, filename} without the curly braces, seperated by newlines")
        file = open(input("Enter file name or path: ").strip())
        lines = file.readlines()
        for line in lines:
            l = line.split(', ')
            urls.append(l[0])
            names.append(l[1].replace(" ", "_").replace("\n", ""))
    else:
        sys.exit("Invalid choice")

    convert(urls, names)
                
def intro():
    print("Do you want to: ")
    print("A) Convert a single Youtube url")
    print("B) Convert a text file with multiple urls")
    return input().strip()

def hook(download):
    if download['status'] == 'finished':
        print('Finished downloading {}'.format(download['filename']))

def convert(urls, names):
    for i in range(len(urls)):
        ytdl_options = {
        'format':'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'noplaylist': False,
        'progress_hooks': [hook],
        'outtmpl': f"{names[i]}.mp3"
        }

        with youtube_dl.YoutubeDL(ytdl_options) as ydl:
            if urls[i]:
                ydl.download([urls[i]])

if __name__=='__main__':
    main()