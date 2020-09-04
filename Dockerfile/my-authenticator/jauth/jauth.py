from jupyterhub.auth import Authenticator
import subprocess
import pwd
from subprocess import check_call
from ldap3 import Server,Connection
import os

class JimoAuth(Authenticator):

    def authenticate(self, handler, data):

        try:
          LDAP_IP = os.environ['LDAP_IP']
          if LDAP_IP != "":
            print("ldap enable!")
        except KeyError:
          LDAP_IP=""
          print("LDAP_IP Not fond disable LDAP mode")

        username = data['username']
        password = data['password']

        if LDAP_IP != "":
          LDAP_PORT = os.environ['LDAP_PORT']
          LDAP_PASSWORD = os.environ['LDAP_PASSWORD']        
          LDAP_BASE_DN = os.environ['LDAP_BASE_DN']

          ldap_user_dir=""
          ldap_user="cn={0}".format(username)
          ldap_user_dir+=ldap_user
          ldap_user_dir+=","
          ldap_user_dir+=LDAP_BASE_DN
          LDAP_SEARCH="(&(uid={0}))".format(username)
       
          print("LDAP_IP")
          print(LDAP_IP)
          print("LDAP_PORT")
          print(LDAP_PORT)
          print("LDAP_PASSWORD")
          print(LDAP_PASSWORD)
          print("LDAP_BASE_DN")
          print(LDAP_BASE_DN)
          print("LDAP_SEARCH")
          print(LDAP_SEARCH)
          print("ldap_user_dir")
          print(ldap_user_dir)

          try:
            conn = Connection(Server(LDAP_IP, port=int(LDAP_PORT)), user=ldap_user_dir, password=password)
            conn.bind()
          except KeyError:
            print("ldap login error")
          try:
            conn.search(ldap_user_dir,LDAP_SEARCH,attributes=['uid','mail','userPassword','gidNumber','uidNumber'])
            ens=conn.entries
            print("uid")
            print(ens[0]['uidNumber'])
            print("gid")
            print(ens[0]['gidNumber'])
          except KeyError:
            print("ldap search error")

        print("password")
        print(password)
        print("username")
        print(username)

        print(handler)
        print(data)
        try:
          pwd.getpwnam(username)
          return username
        except KeyError:
          if LDAP_IP != "":
            subprocess.check_call(['useradd','-u',str(ens[0]['uidNumber']),'-ms', '/bin/bash', username])
            if conn.bind() == True:
              return username
          else:
            subprocess.check_call(['useradd','-ms', '/bin/bash', username])
            subprocess.check_call(['echo',password,'|','passwd', username])
            return username
          

