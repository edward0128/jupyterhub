# jupyterhub


PARAMETER     | example                               |
--------------|---------------------------------------|
LDAP_IP       |10.113.99.1                            |
LDAP_PORT     |30389                                  |
LDAP_PASSWORD |password                               |
LDAP_BASE_DN  |ou=users,dc=ai,dc=nchc,dc=org,dc=tw    | 




使用 ldap 查詢系統
```
ldapsearch -xD cn=admin,dc=ai,dc=nchc,dc=org,dc=tw -wpassword -b ou=users,dc=ai,dc=nchc,dc=org,dc=tw -H ldap://10.113.99.1:30389
```



```
docker run -it -p 8000:8000 -e LDAP_IP="10.113.99.1" -e LDAP_PORT="30389" -e LDAP_PASSWORD="password" -e LDAP_BASE_DN="ou=users,dc=ai,dc=nchc,dc=org,dc=tw" yusongwang1991/jupyterhub
```

build dockerhub image
```
docker build -t yusongwang1991/jupyterhub:latest .
```
