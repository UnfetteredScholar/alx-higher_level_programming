#!/usr/bin/python3
"""Adds all command line arguments to a json file"""
import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
save_to_json_file(sys.argv[1:], filename)
