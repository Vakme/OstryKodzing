#!/usr/bin/env python

Zadania = {"Login"          :0,
           "ZlePolecenie"   :1,
           "exit"           :2,
           "Menu"           :3,
           "Help"           :4,
           "ls"             :5,
           "cd"             :6,
           "Register"       :7}


Error = {"brakBledow"   :0,
         "zlyNick"      :1, 
         "zleHaslo"     :2}


Type = {"txt"   :1,
        "exec"  :2}

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
