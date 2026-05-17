from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
import shutil
from pathlib import Path
class mainHandler(FileSystemEventHandler):
 
    def on_created(self,event):
        
        with open("logarchives.txt","a") as arquivo:
            arquivo.write(f"{event.src_path}\n")
        print("arquivo criado")
        
        if event.src_path.endswith(".txt"):
         
               if event.src_path.endswith(".txt"):
                   
                   
                   
                   
                   os.makedirs("textos",exist_ok = True
                    )
                   filename = Path(event.src_path)
                  
                   filename2 = Path(event.src_path).name
                   print(filename)
                   if os.path.exists(f"/storage/emulated/0/Python tests/textos/{filename2}"):
                        txtnumber =0
                        txtarchivename =f"{filename.stem}({txtnumber}).txt"    
                        os.rename(event.src_path,f"{txtarchivename}")
                        
                        print(event.src_path)
                        txtarchivename =f"{filename.stem}({txtnumber}).txt"
                        print(txtarchivename)
                        for arquivos in os.listdir("/storage/emulated/0/Python tests/textos"):
                            
                            if arquivos ==  txtarchivename:
                                txtnumber+=1
                                print("loop")
                                os.rename(f"{txtarchivename}",f"{filename.stem}({txtnumber}).txt")
                                txtarchivename =f"{filename.stem}({txtnumber}).txt" 
                                
                        os.makedirs("textos",exist_ok = True
                    )
                        print("move")
                        
                        shutil.move(f"{filename.stem}({txtnumber}).txt","textos")
#provávelmente usar for:
                   else:
                       os.makedirs("textos",exist_ok = True
                    )
                       shutil.move(event.src_path,"textos")
                       
                   
        if event.src_path.endswith(".jpg") or event.src_path.endswith(".png") or event.src_path.endswith(".jpeg"):
            
            
            imgname = Path(event.src_path)
                  
            imgname2= Path(event.src_path).name
            os.makedirs("imagens",exist_ok = True)
            if os.path.exists(f"/storage/emulated/0/Python tests/imagens/{imgname2}"):
               imgsnumber =0
               imgsarchive= f"{imgname.stem}({imgsnumber}).{imgname.suffix}"    
               os.rename(event.src_path,f"{imgsarchive}")
               
               shutil.move(event.src_path,"imagens")
               for arquivos in os.listdir("/storage/emulated/0/Python tests/imagens"):
                            
                            if arquivos ==  imgsarchivename:
                                imgsnumber+=1
                                print("loop")
                                os.rename(f"{imgsarchive}",f"{imgname.stem}({imgsnumber}).{imgsarchive.suffix}")
                                imgsarchive =f"{imgname.stem}({imgsnumber}).{imgname.suffix}" 
                                
               shutil.move(f"{imgname.stem}({imgsnumber}).{imgsname.suffix}","imagens")
            else:
                  shutil.move(event.src_path,"imagens")
                 
        if event.src_path.endswith(".mp4"):
            mp4name= Path(event.src_path)
                  
            mp4name2= Path(event.src_path).name
            os.makedirs("videos",exist_ok = True)
            if os.path.exists(f"/storage/emulated/0/Python tests/videos/{mp4name2}"):
               videosnumber =0
               videosarchive= f"{mp4name.stem}({videosnumber}).mp4"    
               os.rename(event.src_path,f"{videosarchive}")
               shutil.move(event.src_path,"videos")
            
               for arquivos in os.listdir("/storage/emulated/0/Python tests/videos"):
                            
                            if arquivos ==  videosarchivename:
                                videosnumber+=1
                                print("loop")
                                os.rename(f"{videosarchive}",f"{mp4name.stem}({videosnumber}).mp4")
                                videosarchive =f"{mp4name.stem}({videosnumber}).mp4" 
                                
               shutil.move(f"{mp4name.stem}({videosnumber}).mp4","videos")
            else:
                  shutil.move(event.src_path,"videos")
                 
             
        if event.src_path.endswith(".pdf"):
            pdfname= Path(event.src_path)
                  
            pdfname2= Path(event.src_path).name
            os.makedirs("pdfs",exist_ok = True)
            if os.path.exists(f"/storage/emulated/0/Python tests/pdfs/{pdfname2}"):
               pdfsnumber =0
               pdfsarchive= f"{pdfname.stem}({pdfsnumber}).pdf"    
               os.rename(event.src_path,f"{pdfsarchive}")
               
               for arquivos in os.listdir("/storage/emulated/0/Python tests/pdfs"):
                            
                            if arquivos ==  pdfsarchive:
                                pdfsnumber+=1
                                print("loop")
                                os.rename(f"{pdfsarchive}",f"{pdfname.stem}({videosnumber}).pdf")
                                videosarchive =f"{pdfname.stem}({pdfsnumber}).pdf" 
                                
               shutil.move(f"{pdfname.stem}({pdfsnumber}).pdf","pdfs")
            else:
                  shutil.move(event.src_path,"pdfs")
       
            
            def on_moved(self,event):
                
                with open("logarchives.txt","a") as arquivo:
                    
                    arquivo.write(f"{event.src_path}\n")
                    print("arquivo criado")
        
                    if event.src_path.endswith(".txt"):
                        
                        os.makedirs("textos",exist_ok = True
                    )
                        filename = Path(event.src_path)
                  
                        filename2 = Path(event.src_path).name
                        print(filename)
                        if os.path.exists(f"/storage/emulated/0/Python tests/textos/{filename2}"):
                            
                            txtnumber =0
                            txtarchivename =f"{filename.stem}({txtnumber}).txt"    
                            os.rename(event.src_path,f"{txtarchivename}")
                        
                            print(event.src_path)
                            txtarchivename =f"{filename.stem}({txtnumber}).txt"
                            print(txtarchivename)
                            for arquivos in os.listdir("/storage/emulated/0/Python tests/textos"):
                                
                                
                                if arquivos ==  txtarchivename:
                                    
                                  
                                 txtnumber+=1
                                 print("loop")
                                 os.rename(f"{txtarchivename}",f"{filename.stem}({txtnumber}).txt")
                                 txtarchivename =f"{filename.stem}({txtnumber}).txt" 
                                
                                 os.makedirs("textos",exist_ok = True
                    )
                                 print("move")
                        
                                 shutil.move(f"{filename.stem}({txtnumber}).txt","textos")
#provávelmente usar for:
                    else:
                        
                        os.makedirs("textos",exist_ok = True
                    )
                        shutil.move(event.src_path,"textos")
                       
                   
        if event.src_path.endswith(".jpg") or event.src_path.endswith(".png") or event.src_path.endswith(".jpeg"):
            
            
            imgname = Path(event.src_path)
                  
            imgname2= Path(event.src_path).name
            os.makedirs("imagens",exist_ok = True)
            if os.path.exists(f"/storage/emulated/0/Python tests/imagens/{imgname2}"):
               imgsnumber =0
               imgsarchive= f"{imgname.stem}({imgsnumber}).{imgname.suffix}"    
               os.rename(event.src_path,f"{imgsarchive}")
               
               shutil.move(event.src_path,"imagens")
               for arquivos in os.listdir("/storage/emulated/0/Python tests/imagens"):
                            
                            if arquivos ==  imgsarchivename:
                                imgsnumber+=1
                                print("loop")
                                os.rename(f"{imgsarchive}",f"{imgname.stem}({imgsnumber}).{imgsarchive.suffix}")
                                imgsarchive =f"{imgname.stem}({imgsnumber}).{imgname.suffix}" 
                                
               shutil.move(f"{imgname.stem}({imgsnumber}).{imgsname.suffix}","imagens")
            else:
                  shutil.move(event.src_path,"imagens")
                 
        if event.src_path.endswith(".mp4"):
            mp4name= Path(event.src_path)
                  
            mp4name2= Path(event.src_path).name
            os.makedirs("videos",exist_ok = True)
            if os.path.exists(f"/storage/emulated/0/Python tests/videos/{mp4name2}"):
               videosnumber =0
               videosarchive= f"{mp4name.stem}({videosnumber}).mp4"    
               os.rename(event.src_path,f"{videosarchive}")
               shutil.move(event.src_path,"videos")
            
               for arquivos in os.listdir("/storage/emulated/0/Python tests/videos"):
                            
                            if arquivos ==  videosarchivename:
                                videosnumber+=1
                                print("loop")
                                os.rename(f"{videosarchive}",f"{mp4name.stem}({videosnumber}).mp4")
                                videosarchive =f"{mp4name.stem}({videosnumber}).mp4" 
                                
               shutil.move(f"{mp4name.stem}({videosnumber}).mp4","videos")
            else:
                  shutil.move(event.src_path,"videos")
                 
             
        if event.src_path.endswith(".pdf"):
            pdfname= Path(event.src_path)
                  
            pdfname2= Path(event.src_path).name
            os.makedirs("pdfs",exist_ok = True)
            if os.path.exists(f"/storage/emulated/0/Python tests/pdfs/{pdfname2}"):
               pdfsnumber =0
               pdfsarchive= f"{pdfname.stem}({pdfsnumber}).pdf"    
               os.rename(event.src_path,f"{pdfsarchive}")
               
               for arquivos in os.listdir("/storage/emulated/0/Python tests/pdfs"):
                            
                            if arquivos ==  pdfsarchive:
                                pdfsnumber+=1
                                print("loop")
                                os.rename(f"{pdfsarchive}",f"{pdfname.stem}({videosnumber}).pdf")
                                videosarchive =f"{pdfname.stem}({pdfsnumber}).pdf" 
                                
               shutil.move(f"{pdfname.stem}({pdfsnumber}).pdf","pdfs")
            else:
                  shutil.move(event.src_path,"pdfs")
       
            
handler = mainHandler()
observer = Observer()
observer.schedule(handler,"/storage/emulated/0/Python tests",recursive = False)
observer.start()
try:
    while True:
        
        
        time.sleep(1)
        
except KeyboardInterrupt:
    
        observer.join()
        observer.stop()
    
    

    
    
    
    