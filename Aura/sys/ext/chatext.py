import time

def chat():
    found = True
    while found == True:
            
        ask = input("\n - ").lower()
        fi = open("C:/Aura/sys/text/chat.txt", "r") 
        data = fi.readlines() 
        fi.close()
            
        stop = 0                        
        for li in data:
            if(li.split(":")[0].lower() == ask):
                time.sleep(1)
                print(li.split(":")[1])
                stop = 1
                found = True
            elif 'bye'in ask:
                stop = 1
                found = False
            elif 'quit' in ask:
                stop = 1
                found = False
        if stop == 0:
            time.sleep(1)
            print("I don't know how to reply to that.")
            appen = input("Help my understanding grow by typing what I should have said.\n - ")
            nex = (str(ask) + ':' + str(appen))
            appendfile = open('C:/Aura/sys/text/chat.txt', 'a')
            appendfile.write('\n')
            appendfile.write(nex)
            appendfile.close()
    time.sleep(1)
    quit()

chat()
