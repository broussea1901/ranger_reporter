#!/usr/bin/env python3
import sys
import json
from json2table import convert
from collections import OrderedDict

jsonfile = sys.argv[1]
if len(sys.argv) < 1:
    print("Syntax error : ranger2table.py <rangerexport>.json")

json_object = json.load(open(jsonfile, 'r'),object_pairs_hook=OrderedDict)

json_meta = json_object['metaDataInfo']
meta = '{ "Ranger Export context" :' + json.dumps(json_meta) + '}'
json_meta = json.loads(meta,object_pairs_hook=OrderedDict)

sorted_json_policies = sorted(json_object['policies'], key=lambda x : x['service'], reverse=False)
#sorted_json_policies=json_object['policies']
policies = '{ "Ranger policies" :' + json.dumps(sorted_json_policies) + '}'
json_policies = json.loads(policies,object_pairs_hook=OrderedDict)

#build_direction = "LEFT_TO_RIGHT"
build_direction = "TOP_TO_BOTTOM"
table_attributes_meta = {}
table_attributes_policies = {"style":"width:100%"}
html_meta = convert(json_meta, build_direction=build_direction, table_attributes=table_attributes_meta)
html_policies = convert(json_policies, build_direction=build_direction, table_attributes=table_attributes_policies)

print(
'''
<html>
<head>
<title>Ranger policies report</title>
<style type="text/css"> 
* {border: 0; margin: 0; padding: 0; font-family: Tahoma; font-size: 8px;}
table {border-collapse: collapse; border: 0.05px solid #24943A; text-align: center;}
td, th {border: .1px solid #24943A; padding: .2em .2em .2em .2em;}
tr:nth-child(even), td:nth-child(even), th:nth-child(even) {background: #FFFFFF;}
tr:nth-child(odd), td:nth-child(odd), th:nth-child(odd) {background: #D4EED1;}
table table table tr:nth-child(even),table table table td:nth-child(even), table table table th:nth-child(even) {background: #D4EED1;}
table table table tr:nth-child(odd), table table table td:nth-child(odd), table table table th:nth-child(odd) {background: #FFFFFF;}
table table td:nth-child(1), table table table table td:nth-child(1) {background: #24943A; font-weight: bold; color: #FFFFFF; border: .1px solid #D4EED1;}
table table th:nth-child(1), table table table table th:nth-child(1) {background: #FFFFFF; font-weight: bold; color: #000000;}
table table table td:nth-child(1) {background: #FFFFFF; border: .1px solid #24943A;}
ul {list-style-type: none;}
</style></head><body>
'''
)
print(html_meta)
print("</br>")
print(html_policies)
print("</body></html>")

