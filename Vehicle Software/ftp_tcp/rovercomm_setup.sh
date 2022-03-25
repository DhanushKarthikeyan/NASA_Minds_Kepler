#!/usr/bin/env bash
if [[ $(id -u) -ne 0 ]] ; then echo "Please run as root" ; exit 1 ; fi
apt install -y vsftpd
printf 'listen=NO\nlisten_ipv6=YES\nanonymous_enable=NO\nlocal_enable=YES\nwrite_enable=YES\nlocal_umask=022\ndirmessage_enable=YES\nuse_localtime=YES\nxferlog_enable=YES\nconnect_from_port_20=YES\nchroot_local_user=YES\nsecure_chroot_dir=/var/run/vsftpd/empty\npam_service_name=ftp\nrsa_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem\nrsa_private_key_file=/etc/ssl/private/ssl-cert-snakeoil.key\nssl_enable=NO\n' > /etc/vsftpd.conf
service vsftpd restart
useradd -m -d /srv/rovercomm rovercomm -s /usr/sbin/nologin
echo rovercomm:rovercomm | chpasswd
chmod a-w /srv/rovercomm
mkdir /srv/rovercomm/incoming
chown rovercomm:rovercomm /srv/rovercomm/incoming
chmod u+w /srv/rovercomm/incoming
