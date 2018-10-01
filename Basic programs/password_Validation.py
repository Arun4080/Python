import re
a='Arunverma@1.'
x=True
while x:
	if (len(a)<6 or len(a)>16) or not re.search(r'[A-Z]', a) or not re.search(r'[a-z]',a) or not re.search(r'[$#@]',a) and re.search(r'/s',a):
		break
	else: 
		print('its a good password')
		x=False
if x:print('not good password')