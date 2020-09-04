import os
from ldap3 import Server,Connection

App = os.environ['test']

try:
    App2 = os.environ['test2']
except KeyError:
    print("1234")

print(App)


conn = Connection(Server('10.113.99.1', port=30389), user="cn=alang886,ou=users,dc=ai,dc=nchc,dc=org,dc=tw", password='password')
conn.bind()
conn.search("cn=alang886,ou=users,dc=ai,dc=nchc,dc=org,dc=tw",'(&(uid=alang886))',attributes=['uid','mail','userPassword','gidNumber','uidNumber'])
ens=conn.entries
print(ens)
print(ens[0]['uidNumber'])
print(ens[0]['gidNumber'])


#docker run -it -p 8000:8000 -e LDAP_IP="10.113.99.1" -e LDAP_PORT="30389" -e LDAP_PASSWORD="password" -e LDAP_BASE_DN="ou=users,dc=ai,dc=nchc,dc=org,dc=tw" yusongwang1991/jupyterhub

#for e in ens:
#    print(e['uidNumber'])