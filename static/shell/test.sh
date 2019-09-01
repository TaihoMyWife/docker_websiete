#!/bin/expect
#set timeout 30
#we need two arg, one is username, two is password
#we can use this shell just like: expect test.sh cliA 19308119
set name [lindex $argv 0]
set password [lindex $argv 1]
cd /home/chen/keys
spawn openssl genrsa -des3 -out $name.pem 1024
expect "Enter pass phrase for $name.pem:"
send "$password\n"
expect "Verifying - Enter pass phrase for $name.pem:"
send "$password\n"
sleep 0.3
spawn openssl req -new -sha256 -key $name.pem -out $name.csr
send "$password\n"
expect "Country Name (2 letter code)"
send "CN\n"
expect "State or Province Name (full name)"
send "Shaanxi\n"
expect "Locality Name (eg, city)"
send "Xian\n"
expect "Organization Name (eg, company)"
send "NeoCom\n"
expect "Organizational Unit Name (eg, section)"
send "NeoComClient\n"
expect "Common Name (e.g. server FQDN or YOUR name)"
send "$name\n"
expect "Email Address"
send "$name@chenu.com\n"
expect "A challenge password"
send "\n"
expect "An optional company name"
send "\n"
sleep 0.3
spawn openssl ca -policy policy_anything -days 7200 -cert ca.crt -keyfile cakey.pem -in $name.csr -out $name.crt
send "19308119\n"
expect "Sign the certificate?"
send "y\n"
expect "1 out of 1 certificate requests certified, commit?"
send "y\n"
sleep 0.3
spawn openssl pkcs12 -export -in $name.crt -inkey $name.pem -out $name.p12 -name $name
expect "Enter pass phrase for $name.pem:"
send "$password\n"
expect "Enter Export Password:"
send "$password\n"
expect "Verifying - Enter Export Password:"
send "$password\n"
sleep 1
spawn cp $name.p12 /home/chen/Documents/wsgi/static/text/auth
interact
exit
