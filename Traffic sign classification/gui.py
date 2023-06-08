import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

import numpy 
from keras.models import load_model
model = load_model('D:\\Tran Quyen\\Code\\Xu Ly Anh\\Nhan dien bien bao giao thong\\Code\\Traffic sign classification\\traffic_classifier.h5')

classes = { 1:'Giới hạn tốc độ (20km/h)',
            2:'Giới hạn tốc độ (30km/h)',      
            3:'Giới hạn tốc độ (50km/h)',       
            4:'Giới hạn tốc độ (40km/h)',      
            5:'Giới hạn tốc độ (70km/h)',    
            6:'Giới hạn tốc độ (80km/h)',      
            7:'Giới hạn tốc độ (10km/h)',     
            8:'Giới hạn tốc độ (100km/h)',    
            9:'Giới hạn tốc độ (120km/h)',     
           10:'Đường dành cho người đi bộ',   
           11:'Không có phương tiện đi qua hơn 3,5 tấn',     
           12:'Bên phải tại giao lộ',     
           13:'Dừng lại',    
           14:'Năng suất',     
           15:'Stop',       
           16:'No vehicles',       
           17:'Veh > 3.5 tons prohibited',       
           18:'No entry',       
           19:'General caution',     
           20:'Dangerous curve left',      
           21:'Dangerous curve right',   
           22:'Double curve',      
           23:'Bumpy road',     
           24:'Slippery road',       
           25:'Road narrows on the right',  
           26:'Giới hạn trọng tải 30 tấn',    
           27:'Traffic signals',      
           28:'Pedestrians',     
           29:'Children crossing',     
           30:'Bicycles crossing',       
           31:'Beware of ice/snow',
           32:'Wild animals crossing',      
           33:'End speed + passing limits',      
           34:'Rẽ phải về phía trước',     
           35:'Rẽ trái về phía trước',       
           36:'Giới hạn tốc độ (10km/h)',      
           37:'Go straight or right',      
           38:'Go straight or left',      
           39:'Keep right',     
           40:'Keep left',      
           41:'Cho phép quay đầu',     
           42:'End of no passing',      
           43:'End no passing veh > 3.5 tons' }
                 
top=tk.Tk()
top.geometry('800x600')
top.title('Nhận Diện Biển Báo GT')
top.configure(background='#CDCDCD')

label=Label(top,background='#CDCDCD', font=('arial',15,'bold'))
sign_image = Label(top)

def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30,30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)  
    print(image.shape)


    predictions = model.predict(image)
    pred = numpy.argmax(predictions[0])
    sign = classes[pred+1]
    print(sign)
    label.configure(foreground='#011638', text=sign) 
   
def show_classify_button(file_path):
    classify_b=Button(top,text="Nhận Diện",command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)
    classify_b=Button(top, text='abc' )

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

upload=Button(top,text="Tải Ảnh Lên",command=upload_image,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('arial',10,'bold'))

upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Hệ Thống Nhận Diện Biển Báo Giao Thông",pady=20, font=('arial',20,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()
top.mainloop()
