import telegram
import asyncio
def send_telegram(photo_path = "alert.png"):
    try:
        my_token = "6572016248:AAE6j1pk2NklQuU_hARWEQ_G23KUZHOI5Io"
        bot = telegram.Bot(token = my_token)
        asyncio.run(bot.sendPhoto(chat_id = "5995079601", 
                      photo = open(photo_path,"rb"), 
                      caption = "Cảnh báo, có xâm nhập!"))
    except Exception as ex:
        print("Can not send messege telegram!", ex)
    
    print("Send sucess")