{\rtf1\ansi\ansicpg1250\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import socket\
from flask import Flask, request\
\
app = Flask(__name__)\
\
@app.route('/')\
def get_client_ip():\
	ip_address = request.remote_addr\
	return f"Your IP address is: \{ip_address\}"\
if __name__ == '__main__\'92:\
	app.run()}