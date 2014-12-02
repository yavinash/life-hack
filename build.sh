#!/bin/bash

# $Id: Avinash Yenikapati$

git clone git@github.com:zeomega/jiva_buildout.git
cd jiva_buildout
git checkout $1
./installpy27.sh -s
./usr/bin/buildout -c linux_dev.cfg
