#!/bin/bash

# clone 
git clone https://github.com/named-data-ndnSIM/ns-3-dev.git ns-3
git clone git@github.com:cesarghali/ndnSIM-PITless.git ns-3/src/ndnSIM
git clone git@github.com:cesarghali/ndn-cxx-PITless.git ns-3/src/ndnSIM/ndn-cxx
git clone git@github.com:cesarghali/NFD-PITless.git ns-3/src/ndnSIM/NFD

# build it
cd ns-3
./waf configure --enable-examples

# good to go
