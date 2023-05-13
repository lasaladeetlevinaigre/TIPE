rm data.csv
gcc engine.c -o engine -Wall -g -lm
./engine
rm engine
python3 plot.py
