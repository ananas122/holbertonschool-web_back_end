#!/usr/bin/env python3
"""function that lists all documents in a collection"""
import pymongo

def list_all(mongo_collection):
    return list(mongo_collection.find())