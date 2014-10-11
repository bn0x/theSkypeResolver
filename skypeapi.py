#! -*- coding: utf-8 -*-
#
# ---------------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 43.5):
# @__akiaki wrote this file. As long as you retain this notice you can do whatever
# you want with this stuff. If we meet some day, and you think this stuff is worth
# it, you can buy me a beer (or caffeinated beverage) in return. --aki
# ---------------------------------------------------------------------------------

import Skype4Py


skype = ""

def init():
    global skype
    if skype == "":
        skype = Skype4Py.Skype()
        skype.Attach()
         
def activateSkype(skypeName):
    global skype
    if skype != "":
        skype.Client.Focus()
        skype.Client.OpenUserInfoDialog(skypeName)
        skype.Client.Minimize()
        skype.Client.Focus()

