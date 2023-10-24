#!/usr/bin/env python3

def extractRules(rules):
    result = {}
    for rule in rules:
        rule = rule.strip('#').strip()
        key, value = rule.split('=')
        key = key.strip()
        value = value.strip()
        result[key] = value
    return result

def filter_text(text):
    # Your solution
    lines = text.splitlines()
    rules = [s for s in lines if "#" in s]
    extractedRules = extractRules(rules)
    for key in extractedRules:
        for value in extractedRules.values():
            if key in value:
                return False
    return True
