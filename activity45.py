import os
import time

def shutdown():
    print('--------SYSTEM SHUTDOWN PROGRAM -----------')
    user_choice = input('do you want to shutdown the compter? yes/no:')
    user_choice = user_choice.lower()
    if user_choice == 'yes' :
        print('\n system will shutdown in 10 seconds...')

        for i in range(10,0,-1):
            print('shutting down in',i,'seconds..')
            time.sleep(1)

        print('Executind shutdown command..')

        os.system('shutdown /s /t 1')

    elif  user_choice == "no":
        print('/nShutdown process cancelled by the user.')

    else:
        print('\ninvalid input , please enter yes or no')
        shutdown()

shutdown()




