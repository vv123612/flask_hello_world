import sys, os, platform

print('-----------------------------------------')
print('os.name: ',os.name)
print('platform.system(): '+platform.system())
print('platform.release(): ', platform.release())
print('executable: ', sys.executable)
print('Packages:')
print('\n'.join(sys.path))
print('-----------------------------------------')
[print(key,':',value) for key,value in dict(os.environ).items()]
