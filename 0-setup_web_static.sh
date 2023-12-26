#!/usr/bin/env bash
# Configure web servers for deployment of web static
#sudo apt-get -y update
#sudo apt-get -y upgrade
#sudo apt-get install -y nginx

sudo mkdir -p /data/web_static/releases/test /data/web_static/shared/

echo "Hamilton is Awesome" | sudo tee /data/web_static/releases/test/index.html > /dev/null

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -hR ubuntu:ubuntu /data/

sudo sed -i '/^    listen 80;$/c\    listen 80;\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

sudo service nginx restart

