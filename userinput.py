import MessageType

def getchloop(message_queue):
    try:
        import msvcrt
        while True:
            if msvcrt.kbhit():
                ch = msvcrt.getch()
                message_queue.put([MessageType.USERESCAPE,ch])
    except ImportError:
        message_queue.put([MessageType.TEXT,'Direct user input only accepted on Windows'])