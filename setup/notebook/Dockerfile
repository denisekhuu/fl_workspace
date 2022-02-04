FROM jupyter/tensorflow-notebook

RUN set -ex \
   && conda install --quiet --yes \
   # choose the Python packages you need
   #'plotly==4.9.0' \
   #'folium==0.11.0' \
   'lux-api==0.4.0'\
   && conda clean --all -f -y \
   # install Jupyter Lab extensions you need
   #&& jupyter labextension install jupyterlab-plotly@4.9.0 --no-build \
   && jupyter labextension install @jupyter-widgets/jupyterlab-manager \
   && jupyter labextension install luxwidget \
   && jupyter lab build -y \
   && jupyter lab clean -y \