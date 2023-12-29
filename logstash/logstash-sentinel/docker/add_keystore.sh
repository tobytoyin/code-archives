#! /bin/bash

# args
keymapfile="$1"

# create keystore
echo "yes\n" | /usr/share/logstash/bin/logstash-keystore create

# adding .env key mapping to logstash keystore
# Loop through each line of the file
while IFS= read line; do
    key=$(echo "$line" | cut -d'=' -f1)
    value=$(echo "$line" | cut -d'=' -f2)

    # add secret to keystore
    value="${value%%[[:space:]]}"
    value="${value%\"}"
    value="${value#\"}"
    echo $value | /usr/share/logstash/bin/logstash-keystore add $key

done < "$keymapfile"
