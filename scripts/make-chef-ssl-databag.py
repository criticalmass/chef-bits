#!/usr/bin/env python

import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--id", help="Item id", required=True)
parser.add_argument("--key", help="SSL key (PEM format)", required=True)
parser.add_argument("--cert", help="SSL cert (PEM format)", required=True)
parser.add_argument("--dhparam", help="dhparam file (PEM format)", required=False)
parser.add_argument("--ca", help="CA bundle file (PEM format)", required=False)
args = parser.parse_args()

def flatten_pem ( file ):
    out = ''
    f = open(file,'r')
    for line in f.readlines():
        out+=line.rstrip()
        out+='\n'
    f.close()
    return out

databag = {
    'id': args.id,
    'key': flatten_pem(args.key),
    'cert': flatten_pem(args.cert),
}

if args.dhparam:
    databag['dhparam'] = flatten_pem(args.dhparam)

if args.ca:
    databag['ca'] = flatten_pem(args.ca)

print databag
