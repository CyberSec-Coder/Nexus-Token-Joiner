import sys
import os
import keyboard
import time

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..",)
    )
)

from Helper import (
    NexusColor,
    pink_gradient,
    Utils
)

class UtilMenu():
    def __init__(self):
        self.utils = Utils()
    
    def menu(self):
        self.utils.clear()
        self.utils.new_title(
            "Nexus Util Menu discord.gg/nexus-tools ┃ Press the key that matches your choice."
        )
        
        sys.stdout.write(fr'''
        {pink_gradient[0]}                      _   __                        ______            __            
        {pink_gradient[1]}                     / | / /__  _  ____  _______   /_  __/___  ____  / /____    
        {pink_gradient[2]}                    /  |/ / _ \| |/_/ / / / ___/    / / / __ \/ __ \/ / ___/    __
        {pink_gradient[3]}                   / /|  /  __/>  </ /_/ (__  )    / / / /_/ / /_/ / (__  )     .-'--`-._
        {pink_gradient[0]}                  /_/ |_/\___/_/|_|\__,_/____/    /_/  \____/\____/_/____/      '-O---O--'
        ''')

        print(f"\n\n\n                                ",
              f"{NexusColor.LIGHTBLACK}[{NexusColor.RESET}1{NexusColor.LIGHTBLACK}] Vc Joiner",
              f"[{NexusColor.RESET}2{NexusColor.LIGHTBLACK}] Token Leaver",
              f"[{NexusColor.RESET}3{NexusColor.LIGHTBLACK}] PFP Changer"
              )

        start_time = time.time()
        message_shown = False
        while True:
            if keyboard.is_pressed("1"):
                print(f"                                        {NexusColor.GREEN} Starting VC Joiner..")
                os.system(fr"py External\scripts\vcjoiner.py")
                break
            
            if keyboard.is_pressed("2"):
                print(f"                                        {NexusColor.GREEN} Starting Server Leaver..")
                os.system(fr"py External\scripts\server_leaver.py")
                break
            
            if keyboard.is_pressed("3"):
                print(f"                                        {NexusColor.GREEN}Starting PFP adder..")
                os.system(fr"py External\scripts\pfp_adder.py")
                break

            if not message_shown and time.time() - start_time >= 10:
                print(f"                                   {NexusColor.GREEN} Press the key that matches your choice.")
                message_shown = True
        
UtilMenu().menu()