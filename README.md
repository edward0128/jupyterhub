# jupyterhub
docker run -it -p 8000:8000 -e LDAP_IP="10.113.99.1" -e LDAP_PORT="30389" -e LDAP_PASSWORD="password" -e LDAP_BASE_DN="ou=users,dc=ai,dc=nchc,dc=org,dc=tw" yusongwang1991/jupyterhub

docker build -t yusongwang1991/jupyterhub:latest .
