pip3 install ldap3
pip install jupyterhub-dummyauthenticator
pip3 install jupyterlab
pip3 install jupyterhub-ldapauthenticator

cd /tmp/my-authenticator/&& python3 setup.py install
#useradd admin
#echo "admin:password" | chpasswd
#jupyterhub 0.0.0.0 -f /tmp/jupyterhub_config.py
