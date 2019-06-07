# 2048 bot
# only works on windows
from pynput.keyboard import Key, Controller, Listener
import time


keyboard = Controller()

keyboard.press(Key.cmd) # open the windows search bar
keyboard.release(Key.cmd)

time.sleep(0.75)

keyboard.type("google") # type "google" and...
time.sleep(0.5) 
keyboard.press(Key.enter)
keyboard.release(Key.enter) # press enter

time.sleep(2) # wait to open

keyboard.press(Key.cmd)
keyboard.press(Key.up)
time.sleep(0.01) # this shit was anoying me so i fixed ti c;
keyboard.release(Key.cmd)
keyboard.release(Key.up)

keyboard.press(Key.ctrl_l)
keyboard.press('t')
# make a new tab
keyboard.release(Key.ctrl_l)
keyboard.release('t')

time.sleep(0.4) # wait

keyboard.type("https://hczhcz.github.io/2048/20ez/") # type in the link to the game
keyboard.press(Key.enter) # press enter
keyboard.release(Key.enter)

time.sleep(1) # let it load

keyboard.press(Key.enter) # press enter
keyboard.release(Key.enter)

time.sleep(2.5)

while(True): 

	keyboard.press(Key.right)
	keyboard.release(Key.right)
	#time.sleep(0.0001) 
	time.sleep(0.015)
	keyboard.press(Key.left)
	keyboard.release(Key.left)
	#time.sleep(0.0001) 
	time.sleep(0.015)
	keyboard.press('d')
	keyboard.release('d')
	#time.sleep(0.0001) 
	time.sleep(0.015)
	keyboard.press('s')
	keyboard.release('s')

	if Key == Key.esc:
		# Stop listener
		print("--------Program-Terminated-------")
		break
	
	else:
		continue
 
