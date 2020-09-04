from jupyterhub.auth import Authenticator
import subprocess
import pwd
from subprocess import check_call
from ldap3 import Server,Connection


class JimoAuth(Authenticator):

    def authenticate(self, handler, data):
        print('login test')
        username = data['username']
        ldap_user_dir="cn={0},ou=users,dc=ai,dc=nchc,dc=org,dc=tw".format(username)
        ldap_search="(&(uid={0}))".format(username)
        conn = Connection(Server('10.113.99.1', port=30389), user=ldap_user_dir, password=data['password'])
        conn.bind()
        conn.search(ldap_user_dir,ldap_search,attributes=['uid','mail','userPassword','gidNumber','uidNumber'])
        
        print(ldap_user_dir)
        print("test")
        print(data['password'])       
        
        ens=conn.entries     
        print(ens[0]['uidNumber'])
        print(ens[0]['gidNumber'])


        print('test123')
        #if data['username'] == data['password']:
        #    return username


        print(handler)
        print(data)
        try:
          pwd.getpwnam(username)
        except KeyError:
           #print('creat group')
           #try:
           #  test=subprocess.check_call(['groupadd','-g',ens[0]['gidNumber'],username])
           #except KeyError:
           #  print(test)
           #  print("error")
          subprocess.check_call(['useradd','-u',str(ens[0]['uidNumber']),'-ms', '/bin/bash', username])
           #subprocess.check_call(['useradd','-ms', '/bin/bash', username])
        # check password:
	
        if conn.bind() == True:
          return username


#import subprocess
#import pwd
#from subprocess import check_call
#def my_hook(spawner):
#    username = spawner.user.name
#    try:
#      pwd.getpwnam(username)
#    except KeyError:
#      subprocess.check_call(['useradd', '-ms', '/bin/bash', username])
