FROM jupyterhub/jupyterhub

# install the library by pip 
#RUN pip install --upgrade pip
RUN pip3 install ldap3
RUN pip3 install jupyterlab
COPY my-authenticator my-authenticator	
RUN cd my-authenticator && python3 setup.py install
## expose port 8888,22
EXPOSE 8000

#COPY jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py
COPY jc_auth.py jc_auth.py
CMD  jupyterhub -f jc_auth.py 
