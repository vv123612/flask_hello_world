import sys, os, platform
from flask import Flask
from flask import request


def info2():
    print('-----------------------------------------')
    print('os.name: ',os.name)
    print('platform.system(): '+platform.system())
    print('platform.release(): ', platform.release())
    print('executable: ', sys.executable)
    print('Packages:')
    print('\n'.join(sys.path))
    print('-----------------------------------------')
    [print(key,':',value) for key,value in dict(os.environ).items()]


def info():
    s='\n'

    return f'''
    Hello World! 
    -----------------------------------------')
    os.name: {os.name}
    platform.system(): {platform.system()}
    platform.release(): ', {platform.release()}
    executable: ', {sys.executable}

    Packages:
    {s.join(sys.path)}
    
    -----------------------------------------
    os.environ).items() 
    {s.join([(key+' = '+value) for key,value in dict(os.environ).items()])}
    '''

        # IP {request.remote_addr}

# def env():
#     [key+':'+value for key,value in dict(os.environ).items()]




print(info())
# info2()