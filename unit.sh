cd src
./testing.sh
cd ../tests
python3.6 -m unittest test_functions.pyx
cd ../
