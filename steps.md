1. make rebuild-apache
2. make exec-apache
If server not running then 
ln -s /home/boincadm/project/boincserver.httpd.conf /etc/apache2/conf-enabled/boincserver.httpd.conf
/etc/init.d/apache2 reload
4. cd html/ops
5. echo "admin" | htpasswd -i -c .htpasswd admin
Go to http://127.0.0.1/boincserver_ops
Sign up
go to Manage applications
add an application
uppercase uppercase
6. cd ~/projects/
Add
        <daemon>
            <cmd>sample_trivial_validator --app uppercase</cmd>
        </daemon>
        <daemon>
            <cmd>sample_assimilator --app uppercase</cmd>
        </daemon>
to the config.xml

7. sed -i 's/define("PROJECT", "boincserver");/define("PROJECT", "Williams Ukpere Project");/' html/project/project.inc

8. 
cp tmp_apps/uppercase_out templates
cp tmp_apps/uppercase_in templates
cp templates/uppercase_in templates/uppercase_in.xml
cp templates/uppercase_out templates/uppercase_out.xml

9. 
cd apps/
mkdir -p uppercase/1.0/x86_64-pc-linux-gnu
cd uppercase/1.0/x86_64-pc-linux-gnu
cp ~/project/tmp_apps/uppercase .
cp ~/project/tmp_apps/version.xml .
cd ~/project
bin/sign_executable app
s/uppercase/1.0/x86_64-pc-linux-gnu/uppercase keys/code_sign_private >> apps/uppercase/1.0/x86_64-pc-linux-gnu/uppercase.sig
bin/update_versions

bin/stop
bin/start

echo "Hello worldls!" >> in

Then you need to connect from you client app to the server
And register/login
http://127.0.0.1/boincserver

bin/create_work --appname uppercase in

resuls in upload/ folder
