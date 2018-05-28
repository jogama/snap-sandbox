# source this before snapping. You probably have to source again if you clean. 

# the dir is $SNAPCRAFT_PART_INSTALL
PYTHONPATH=$PYTHONPATH:$(../src/culebra/prepend_sitepackages.py /home/jgarciamallen/sandbox/cmake_py/snap/parts/everything/install mkdir);

mkdir -p /home/jgarciamallen/sandbox/cmake_py/snap/parts/everything/src/bin

# then you can snap
