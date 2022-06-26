weight = input("weight: ")
weight = int(weight)

type_of_weight = input("(L)bs or (K)g ")

if type_of_weight == 'L' or type_of_weight == 'l':
    print(f'you are {weight/2.2046} kilos')
elif type_of_weight == 'k' or type_of_weight == 'K':
    print(f'you are {weight*2.2046} kilos')
else:
    print("enter only letter L or K for conversion")
