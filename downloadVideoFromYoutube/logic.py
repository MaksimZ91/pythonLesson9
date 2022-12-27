from pytube import YouTube
import controller


def getVideo(link):
  try:
    yt = YouTube(link)
    resolution = [str(i.resolution) for i in yt.streams.filter(progressive=True) ]
    res = controller.userRequset(resolution)  
    yt.streams.filter(res=res, file_extension='mp4').desc().first().download()
    return True
  except:
    return False

def getAudio(link): 
  try:
    yt = YouTube(link)  
    yt.streams.filter(only_audio=True).desc().first().download()
    return True
  except:
    return False
   


