#!/usr/bin/env python3

def filter_text(text):
    # Your solution
    lines = text.splitlines()
    rules = [s for s in lines if "#" in s]
    counter = 0
    for rule in rules:
        words = rule.split(" ")
        key = words[1]
        if len(key) > 1:
            counter = counter + 1
    if counter == len(rules):
        return True
    else:
        return False
    
