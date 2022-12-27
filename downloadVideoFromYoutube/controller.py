import ui
import logic

def start():
  answer = ui.audioOrVideo()  
   
  match answer:
    case 1:
      link = ui.linkReques()
      ui.downoladStatusCheck(logic.getVideo(link))
    case 2:   
      link = ui.linkReques()
      ui.downoladStatusCheck(logic.getAudio(link))
    case 0:
     return 
  
def userRequset(res):  
 resolution = ui.RequestResolution(res) 
 return resolution


  
