#opeming file form cmd line
import sys
f_name = sys.argv[1]
input_file= open(f_name,'r')
line = input_file.readlines();

#extracting input
for str in line:
    in_arr = str.split()
    first_string = in_arr[0] # --> first input
    second_string = in_arr[1]   # --> Second input

    # print(first_string ," " ,second_string)

  
    #var declartion
    linear = int(0)
    fcircular = int(0)
    circular = int(0)
    length = len(first_string)

    for i in range(0,length):  

        # finding ascii code
        ascii_1 =  ord(first_string[i])        
        ascii_2 =  ord(second_string[i]) 
        
        if ascii_1 != ascii_2 :  
            if ascii_1 > ascii_2 :              
                linear = linear + (ascii_1 - ascii_2)
                x = ord('z')  -  ascii_1               
                y = ascii_2 - ord('a')                
                fcircular =  x+y+1
                circular = circular +  min(fcircular , ascii_1 - ascii_2)           
            else:
               
                linear = linear + (ascii_2 - ascii_1)
                x = ord('z')  - ascii_2               
                y = ascii_1 - ord('a')
                fcircular =  x+y+1
                circular = circular +  min(fcircular , ascii_2 - ascii_1)
        
    print(linear,circular )