#!/bin/bash
for i in *.html; do
    cp header ../$i;
    cat $i >> ../$i;
    cat footer >> ../$i;
done
