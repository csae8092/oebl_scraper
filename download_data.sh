#!/bin/bash
rm -rf orig_data.zip
rm -rf ./data
gdown --id 1f8ni9qfgDQIdX-WEZzI4puZYmRuDfCgm --output orig_data.zip
unzip orig_data.zip -d .
rm -rf orig_data.zip