from ppadb.client import Client
import cv2
import keyboard
import numpy
from PIL import Image
import pytesseract
import time
import os
import threading
from save import save
import traceback
import time
#
# C:\Program Files\Tesseract-OCR\tesseract.exe
# X:\Tesseract-OCR\tesseract.exe
try:
    path = 'r\'X:\Tesseract-OCR\tesseract.exe\''
    pytesseract.pytesseract.tesseract_cmd = r'X:\Tesseract-OCR\tesseract.exe'
    adb = Client(host="127.0.0.1", port=5037)
    # print(adb.devices())
    devices = adb.devices()
    device = devices[0]
except Exception as e:
    print("錯誤代碼: "+ e)
    print("裝置連結錯誤，關閉腳本後確認是否成功執行")        
pause = False
db = save()
blacklist = ["BearJellyToy","BubblyBoba","RedberryJuice"]
def main():

    

    # id_img = screenshot()
    # idimg = id_img[720:765,385:605]
    # cv2.imshow('img',idimg)
    # cv2.waitKey(0)
    # print(resourceOcr(idimg,False))
    # print(difflib.SequenceMatcher(None,'IQNMS6843',resourceOcr(idimg,False)).quick_ratio())
    # os.system("pause")
    # # 0.8571428571428571

    t = threading.Thread(target=Mpause)
    t.daemon = True
    t.start()
    
    while True:
        try:
            print("若要暫停請按Scroll Lock")
            global pause
            while pause == False:
                # cls()
                time.sleep(0.5)
                img = screenshot()
                nametext = getImgName(img)
                cv2.imshow('img',img[790:840,1440:1800])
                cv2.waitKey(0)

                # imgname = img[790:870, 1440:1800]
            

                # print(db.limit(db, nametext))

                if db.is_metirial(nametext):
                    print("current: ",getImageDigit(img,db.is_metirial(nametext))," limit: ",db.limit(nametext))
                    if nametext == "BiscuitFlour" or nametext == "Jellyberry":
                        if getImageDigit(img,db.is_metirial(nametext)) < db.limit(nametext):
                            # device.shell('input touchscreen swipe 1700 670 1700 670 1000')
                            device.shell("input touchscreen tap 1700 670")
                            print("Execute")
                    elif getImageDigit(img,db.is_metirial(nametext)) < db.limit(nametext):
                        # device.shell('input touchscreen swipe 1700 350 1700 350 1000')
                        device.shell("input touchscreen tap 1700 350")
                        print("Execute")
                else:
                    for i in range(3):
                        if i == 0:
                            print(nametext)
                            print("current: ",getImageDigit(img,db.is_metirial(nametext),i=0)," limit: ",db.limit(nametext))
                            l = db.limit(nametext)
                            if getImageDigit(img,db.is_metirial(nametext),i=0) < l:
                                # print(getImageDigit(img,db.is_metirial(nametext),i=0))
                                # print(l)
                                # device.shell('input touchscreen swipe 1700 350 1700 350 1000')
                                device.shell("input touchscreen tap 1700 350")
                                print("Execute")
                        if i == 1:
                            nametext = getImgName(img,i=1)
                            print(nametext)
                            if len(nametext) == 0 :
                                break
                            if nametext in blacklist:
                                continue
                            print("current: ",getImageDigit(img,db.is_metirial(nametext),i=1)," limit: ",db.limit(nametext))
                            l = db.limit(nametext)
                            if getImageDigit(img,db.is_metirial(nametext),i=1) < l:
                                # print(getImageDigit(img,db.is_metirial(nametext),i=1))
                                # print(l)
                                # device.shell('input touchscreen swipe 1700 680 1700 680 1000')
                                device.shell("input touchscreen tap 1700 680")
                                print("Execute")
                        if i == 2:
                            nametext = getImgName(img,i=2)
                            print(nametext)
                            if len(nametext) == 0 :
                                break
                            if nametext in blacklist:
                                break
                            print("current: ",getImageDigit(img,db.is_metirial(nametext),i=2)," limit: ",db.limit(nametext))
                            l = db.limit(nametext)
                            if getImageDigit(img,db.is_metirial(nametext),i=2) < l:
                                # print(getImageDigit(img,db.is_metirial(nametext),i=2))
                                # print(l)
                                device.shell("input touchscreen tap 1700 1000")
                                # device.shell('input touchscreen swipe 1700 1000 1700 1000 1000')
                                print("Execute")
                time.sleep(3)
                device.shell("input touchscreen tap 1020 530")
            cls()
            print("已暫停")
            print("按 F12以重新開始，F11來查看或修改數量上限")
            keyboard.add_hotkey('F11',adjust)
            keyboard.wait("F12")
            cls()
            print("重新開始")
            print("若要暫停請按Scroll Lock")
            pause = False
        except Exception as e:
            print(e)
            traceback.print_exc()
            device.shell("input touchscreen tap 1020 530")
            # os.system("pause")

def spause():
    os.system("pause")


def getImgName(imgI,i = None)->str:
    imgname = imgI[150:200, 1440:1800]
    if i != None:
        if i == 1:
            imgname = imgI[470:520,1440:1800]
        if i == 2:
            imgname = imgI[790:840,1440:1800]

    
    cv2.imshow('img/getImgName',imgname)
    cv2.waitKey(0)
    nametext = resourceOcr(imgname, False)
    nametext = "".join(nametext.split())
    return nametext

def getImageDigit(imgI,ismetirial:bool,i=None)->int:
    #True 
    if ismetirial:
        imglimit = imgI[25:80, 1050:1180]
    #False
    if i == 0:
        imglimit = imgI[304:339, 1295:1350]
    if i == 1:
        imglimit = imgI[620:655, 1295:1350]
    if i == 2:
        imglimit = imgI[940:975, 1295:1350]

    cv2.imshow('img2/getImageDigit',imglimit)
    cv2.waitKey(0)
    limittext = resourceOcr(imglimit, True)
    limittext = "".join(limittext.split())
    try:
        limittext = int(limittext)
    except Exception as e:
        limittext = 1
    return limittext


def cls():
    os.system("cls" if os.name == "nt" else "clear")



def Mpause():
    global pause
    while True:
        keyboard.wait("scroll lock")
        pause = True


def resourceOcr(img, isdigit:bool):
    threshold = 180
    _, img_binarized = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    pil_img = Image.fromarray(img_binarized)
    if isdigit == True:
        text = pytesseract.image_to_string(
            pil_img, lang="eng", config="--psm 10 -c tessedit_char_whitelist=0123456789"
        )
    else:
        text = pytesseract.image_to_string(pil_img, lang="eng")
    return text


def screenshot():
    result = device.screencap()
    img = numpy.array(result)
    cv2.imshow('screen_shot',img)
    cv2.waitKey(0)
    imga = cv2.imdecode(img, cv2.COLOR_RGBA2BGR)
    img = cv2.cvtColor(imga, cv2.COLOR_BGR2GRAY)
    return img




def adjust():
    df = db.list_all()
    cls()
    keyboard.remove_hotkey('F11')   
    while True:
        try:
            cls()
            print(df)
            index = int(input("輸入想修改材料數量左方的數字(0-61): "))
        except:
            print("輸入錯誤 輸入內容限定為(0-61)的數字")
            ans = str(input('是否再輸入一次?(Y/N) :') or 'N')
            if ans.upper() != "Y":
                break
        if 0<= index <= 61:
            name =  df.iloc[index, df.columns.get_loc('名稱')]
            while True:
                print("要修改的素材為: "+name)
                new_limit = input("請輸入修改後的數量上限:")
                if new_limit.isdigit():
                    int(new_limit)
                    break
                else:
                    print("請輸入數字")
            db.update(name,new_limit)
            cls()
            print("修改完成，"+name+"數量調整為"+str(new_limit))
            os.system("pause")
            break
        else:
            print("輸入錯誤 輸入內容限定為(0-61)的數字")
            ans = str(input('是否再輸入一次?(Y/N) :') or 'N')
            if ans.upper() != "Y":
                break
            
    cls()       
    print("請按F12繼續使用腳本")       
    


if __name__ == "__main__":
    main()
    
