from tkinter import*
import requests

class IRCTC:
                def __init__(self):
                                self.root=Tk()
                                
                                self.root.title("IRCTC")                                                                                  #name assign
                                self.root.minsize(400,600)                                                                                #size restrictions
                                self.root.maxsize(400,600)
                                self.root.configure(background="#3498db")                                                                 #colour scheme

                                label1=Label(self.root,text="Train Route", bg="#3498db", fg="#ffffff")                                    #configuring label class
                                label1.configure(font=("Times Roman", 22, "bold"))                                                        #configuring text
                                label1.pack(pady=(30,10))

                                self.train_no=Entry(self.root)
                                self.train_no.pack(ipadx=40, ipady=10)

                                click=Button(self.root,text="Fetch",bg="#ffffff", width=28, height=2,command=lambda:self.fetch())
                                click.pack(pady=(10,20))

                                self.result=Label(self.root, bg="#3498db", fg="#ffffff")                                                  #configuring label class
                                self.result.configure(font=("Times Roman", 14))                                                           #configuring text
                                self.result.pack(pady=(5,10))


                                self.root.mainloop()

                def fetch(self):
                                train_no=self.train_no.get()
                                url="https://api.railwayapi.com/v2/route/train/{}/apikey/kis6g64yjx/".format(train_no)
                                response=requests.get(url)
                                data=response.json()

                                stations=""
                                for i in data['route']:
                                                stations=stations+i['stations']['name']+" | "+ i['scharr']+ " | "+ str(i['distance']) + "KM"+"\n"
                                                self.result.configure(text=i['station']['name'])



obj=IRCTC()
