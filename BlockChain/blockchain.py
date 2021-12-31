import datetime
import hashlib
import json
from flask import Flask, jsonify

class BlockChain:
  def __init__(self):
   self.chain = []
   self.createBlock(proof=1, previousHash='0') 