def addition(INPUT_X,INPUT_Y):
	
	if(len(INPUT_Y)>len(INPUT_X)):
		INPUT_X,INPUT_Y=INPUT_Y,INPUT_X
	while(len(INPUT_X)>len(INPUT_Y)):
		INPUT_Y.insert(0,0)
	n=len(INPUT_X)
	somme=[0 for i in range(0,n+1)]
	for i in range(n-1,-1,-1):
		if((INPUT_X[i]+INPUT_Y[i])>9 or (INPUT_X[i]+INPUT_Y[i])<0):
			somme[i+1]=(INPUT_X[i]+INPUT_Y[i])%10
			if(i==0):
				somme[i]+=((INPUT_X[i]+INPUT_Y[i])//10)
			else:
				INPUT_X[i-1]+=((INPUT_X[i]+INPUT_Y[i])//10)
			
		else:
			somme[i+1]+=INPUT_X[i]+INPUT_Y[i]
	i=0
	while(somme[i]==0):
		i+=1
	return(somme[i:])

def produit(INPUT_LIST,NUMBER):
	INPUT_LENGTH=len(INPUT_LIST)
	
	RESULT=[0 for i in range(0,INPUT_LENGTH+1)]
	for i in range(INPUT_LENGTH-1,-1,-1):
		if((RESULT[i+1]+INPUT_LIST[i]*NUMBER)>9):
			RESULT[i]+=((RESULT[i+1]+INPUT_LIST[i]*NUMBER)//10)
			RESULT[i+1]=(RESULT[i+1]+INPUT_LIST[i]*NUMBER)%10
			
			
		
		else:
			RESULT[i+1]+=INPUT_LIST[i]*NUMBER
	if(RESULT[0]==0):
		return RESULT[1:]
	else:
		return RESULT



def multiplication(INPUT_1,INPUT_2):
	RESULT=[]
	Z_NUMBER=0
	for i in range (len(INPUT_2)-1,-1,-1):

		PRODUCT=produit(INPUT_1,INPUT_2[i])
		for k in range (0,Z_NUMBER):
			PRODUCT.append(0)
		Z_NUMBER+=1
		RESULT=addition(RESULT,PRODUCT)
	return RESULT




def ToString(liste):
	chaine=""
	for e in liste:
		chaine+=str(e) 
	return chaine


def ToList(string):
	L=[int(i) for i in string]
	return L

FIRST="31112"
SECOND="271828"
LIST_X=ToList(FIRST)
LIST_Y=ToList(SECOND)
res=multiplication(LIST_Y,LIST_X)
print(ToString(res))


