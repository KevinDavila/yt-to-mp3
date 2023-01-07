from pytube import YouTube


def Download(link):
    ytObject = YouTube(link)
    ytObject = ytObject.streams.filter(progressive=True, file_extension='mp4').first()
    print(ytObject)
    try:
        ytObject.download()
    except:
        print("ocurrio un error")
    print("La descarga se ah Completado")


link = input("ingresa link de YT: ")
Download(link)