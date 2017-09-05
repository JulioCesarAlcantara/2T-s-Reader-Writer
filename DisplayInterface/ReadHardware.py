#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import Library.MFRC522
import signal

continue_reading = True

# Capture SIGINT para limpeza quando o script for interrompido
def end_read(signal,frame):
    global continue_reading
    print ("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

# Gancho no SIGINT
signal.signal(signal.SIGINT, end_read)

# Cria um objeto da classe MFRC522
MIFAREReader = Library.MFRC522.MFRC522()

# Welcome message
print ("Welcome to the MFRC522 data read example")
print ("Press Ctrl-C to stop.")

# Este loop continua procurando por chips. Se estiver próximo, obterá o UID e autenticará
while continue_reading:
    
    # Procurar cartões
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print ("Card detected")
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
        print ("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
    
        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)

        #Sector
        sectorBlock = 9
        
        # Authenticate
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, sectorBlock, key, uid)

        # Check if authenticated
        if status == MIFAREReader.MI_OK:
            MIFAREReader.MFRC522_Read(sectorBlock)
            MIFAREReader.MFRC522_StopCrypto1()
        else:
            print ("Authentication error")

