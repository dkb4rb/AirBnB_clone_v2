# Nginx configuration file

package { 'nginx':
  ensure   => 'present',
  provider => 'apt'
} ->

$nginx_conf = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=EgBJmlPo8Xw;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"

file { '/data':
  ensure  => 'directory'
} ->

file { '/data/web_static':
	ensure => 'directory'
} ->

file { '/data/web_static/releases':
	ensure => 'directory'
} ->

file { '/data/web_static/releases/test':
	ensure => 'directory'
} ->

file { '/data/web_static/releases/test/index.html':
	ensure => 'present',
	content => 'Holberton School\n'
} ->

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test'
} ->

exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}

file { '/var/www':
  ensure => 'directory'
} ->

exec { 'nginx restart':
	path => '/usr/sbin/'
} ->
