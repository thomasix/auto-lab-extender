#!/bin/bash
input=~/credentials

while IFS= read -r line
do
	if [[ $line == aws_* ]] ; then
		val=$(echo "$line" | cut -d'=' -f 2)
		if [[ $line == aws_access_key_id=* ]] ; then
			echo "KeyID: $val"
			echo "$val" | gh secret set AWS_ACCESS_KEY_ID --repo thomasix/cloud-native-software-development
		elif [[ $line == aws_secret_access_key=* ]] ; then
			echo "AccessKey: $val"
			echo "$val" | gh secret set AWS_SECRET_ACCESS_KEY --repo thomasix/cloud-native-software-development
		elif [[ $line == aws_session_token=* ]] ; then
			echo "SessionToken: $val"
			echo "$val" | gh secret set AWS_SESSION_TOKEN --repo thomasix/cloud-native-software-development
		fi
	fi
done < "$input"
