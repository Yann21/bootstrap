DIR=$(mktemp -d)
cd $DIR

curl -LO https://thoughtbot.github.io/rcm/dist/rcm-1.3.4.tar.gz
tar -xvf rcm-1.3.4.tar.gz
cd rcm-1.3.4

./configure --prefix=$HOME/.local
make
make install
