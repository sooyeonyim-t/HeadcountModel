import sys
import cv2
import tensorflow
import numpy

def print_awesome():
    print('''
             ____                                  __                       
/\  _`\      __                       /\ \                      
\ \,\L\_\   /\_\     ___       __     \ \ \____   _ __    ___   
 \/_\__ \   \/\ \  /' _ `\   /'__`\    \ \ '__`\ /\`'__\ / __`\ 
   /\ \L\ \  \ \ \ /\ \/\ \ /\ \L\.\_   \ \ \L\ \\ \ \/ /\ \L\ \
   \ `\____\  \ \_\\ \_\ \_\\ \__/.\_\   \ \_,__/ \ \_\ \ \____/
    \/_____/   \/_/ \/_/\/_/ \/__/\/_/    \/___/   \/_/  \/___/ 
                                                                
                                                           
    '''     

    )
    print('\n')

    print('python ', sys.version)
    print('openCV ', cv2.__version__)
    print('tensorflow ', tensorflow.__version__)
    print('numpy ', numpy.__version__)
    # print('             ')
    # print('\n\n\n')