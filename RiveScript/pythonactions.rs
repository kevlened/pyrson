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

> object type_string python
	from autopy import key	
	key.type_string(' '.join(args))
	return ""
< object

> object toggle python
	from autopy import toggle	
	alert.alert(args[0])
	return ""
< object