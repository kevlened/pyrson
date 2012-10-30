import MessageType
import time

def easygui_input(message_queue):
    import easygui
    while True:
        response = easygui.enterbox(msg='Type something you want to communicate:', title='Communicate via text',strip=True)
        if response:
            message_queue.put([MessageType.TEXT,response])
        else:
            message_queue.put([MessageType.USERESCAPE,'q'])

def windows_getch_loop(message_queue):
    try:
        import msvcrt
        while True:
            if msvcrt.kbhit():
                ch = msvcrt.getch()
                message_queue.put([MessageType.USERESCAPE,ch])
            time.sleep(.01)
    except Exception, e:
        message_queue.put([MessageType.TEXT,e])