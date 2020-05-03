import string
alphabet=" "+string.ascii_lowercase
def encode():
	seq=input("enter message to be encrypted:  ").lower()
	key=int(input("enter choice of key:  "))
	position={" ":0, "a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
	rev={list((position.values()))[i]: list((position.keys()))[i] for i in range(len(position))}
	empty=""
	for i in seq:
		if (position[i]+key)%26 != position[i]+key:
			empty+=rev[((position[i]+key)%26)-1]
		else:
			empty+=rev[position[i]+key]
	print(empty)
encode()
	
def decode():
	word=input("enter word to be decoded:  ")
	key=int(input("enter number of keys:  "))
	position={" ":0, "a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
	rev={list((position.values()))[i]: list((position.keys()))[i] for i in range(len(position))}
	empty=""
	for i in word:
			if (position[i]-key)%26 != position[i]-key:
				empty+=rev[((position[i]-key)%26)+1]
			else:
				empty+=rev[position[i]-key]
	print(empty)
	
decode()