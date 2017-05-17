def mysqrt(a):
	epsilon = 0.0001
	x = 10.00000
	while True:
		y = (x + a/x) / 2
		if abs(y - x) < epsilon:
			return y
			break
		x = y
		
import math

def test_square_root():
	print ("a     mysqrt(a)     math.sqrt(a)     delta")
	print ("-     ---------     ------------     -----")
	for a in range(1, 10):
		print ('{:.1f}    {:.5f}        {:.5f}       {:f}'.format(a,mysqrt(a), math.sqrt(a), mysqrt(a)-math.sqrt(a)))
		
test_square_root()
