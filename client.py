import sys
from threading import Thread
import time
def threaded_function():
    #botsocket.run(app ,host=HOST, port=int(os.environ.get('PORT', 5000)))
    time.sleep(1)
    def send_message(chat_id, text = 'Unknown command'):
        #https://api.telegram.org/bot7875995471:AAFYcnSDTwKB-A7OffWoSeMquN6Y-1i32fc/deleteWebhook?https://1555-141-138-108-110.ngrok-free.app
        url = 'https://api.telegram.org/bot7875995471:AAFYcnSDTwKB-A7OffWoSeMquN6Y-1i32fc/' + 'sendmessage'
        answer = {'chat_id' : chat_id, 'text':text}
        r = requests.post(url, json=answer)

        return r.json()
    from socketio import Client
    send_message(500397666, "dssconnected")
     
    sio = Client(logger=True, engineio_logger=True)
    sio.connect("https://1555-141-138-108-110.ngrok-free.app");
    
    sio.sleep(0)

    sio.emit("message", {'from':'to'});

    @sio.event
    def connect_error(data):
        send_message(500397666, "The connection failed!" + str(data))
    @sio.event
    def connect():
        send_message(500397666, "connected")
    
    
    @sio.event
    def disconnect(reason):
        send_message(500397666," I'm disconnected! reason:"+ str(reason))

if __name__ == "__main__":
    time.sleep(5)
    thread = Thread(target = threaded_function)
    thread.start()
    thread.join()

 

    #and client
