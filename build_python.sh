export PYTHONPATH=$PYTHONPATH:"$PWD/build/python"
pip3 install -e src/culebra/ --install-option="--script-dir=../../bin" --install-option="--install-dir=../../build/python"
