import random



data = ['A', 'B','C','D','E','F','G','H','I','J','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'1','2','3','4','5','6','7','8','9','10','!','@','#','$','_','^','&','*','(',')']

dump = ''

flag1 = True


ask_dump = str(input("Do you want to create a pattern or upload a pattern (For Secondary Use) ? [create = 'c', upload = 'u']\t"))


if ask_dump == 'c' :
    pass
    
else :
    flag1 = False
    dump = str(input("Please paste the dump here: \t"))




if flag1:
    dump_length=int(input("Please enter the length of dump: "))
    print ("Your dump is being created !! \n No 4 consecutive letters can be equal in the whole string which is being generated.\n So please wait time will be taken according to the length of the string you mentioned \n")
    time.sleep(2)
    input("Press enter after reading this to start the process!  ")
    check_list = []
    for i in range(0, dump_length) :
        dump = dump + data[random.randint(0,len(data)-1)]
        check_list.append(dump[i:i+3])
        for checker in check_list:
            if dump == checker:
                i = i-1
print(dump)




flag = True

while flag :


    pattern = input("Please enter the pattern u need to find: ")

    pattern_length = len(pattern)

    pattern_indexes = []

    for i in range(0, len(dump)):
        pattern_comp = dump[i:i+pattern_length]
        if pattern == pattern_comp :
            pattern_indexes.append(i)
            print('Inject after {}'.format(i-1))



    print("List of indexes found  "+str(pattern_indexes))

    decision = str(input("Do u want to check another string (y,n): "))

    if(decision == 'y'):
        pass
    else:
        flag = False
        print("Follow my discord server: https://discord.gg/gY25hNhXNy")
        print("Follow me on Instagram: https://instagram.com/_lexilominite_")
        print(" Bye...Bye...Catch you later ")
