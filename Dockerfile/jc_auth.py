from jupyter_client.localinterfaces import public_ips
c.JupyterHub.hub_ip = public_ips()[0]
#c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

from jauth import JimoAuth
c.JupyterHub.authenticator_class = JimoAuth



c.Spawner.default_url = '/lab'
#c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'
#c.DummyAuthenticator.password = "password"



#import subprocess
#import pwd
#from subprocess import check_call
#def my_hook(spawner):
#    username = spawner.user.name
#    try:
#      pwd.getpwnam(username)
#    except KeyError:
#      subprocess.check_call(['useradd', '-ms', '/bin/bash', username])
#c.Spawner.pre_spawn_hook = my_hook
