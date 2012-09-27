> object alert python
	from autopy import alert
	
	alert.alert(' '.join(args))
	
	return ""
< object

> object mouse python
	from autopy import mouse	
	
	x = int(args[0])
	y = int(args[1])
	mouse.move(x,y)
	
	return ""
< object

> object typekeys python
	from autopy import key
	from array import array
	
	s = ' '.join(args)
	sa = array('c',str(s))
	spchar = set(str('!@#$%^&*()_+{}|:"<>?'))
	
	for c in sa:
		if c in spchar:
			key.tap(c,key.MOD_SHIFT)
		else:
			key.tap(c)
		
	return ""
< object