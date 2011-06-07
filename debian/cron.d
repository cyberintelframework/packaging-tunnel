*/5 * * * * root /opt/surfnetids/scripts/rrd_traffic.pl >/dev/null
*/5 * * * * root /opt/surfnetids/scripts/rrd_serverinfo.pl >/dev/null
*/10 * * * * root /opt/surfnetids/scripts/tun-janitor.pl >/dev/null
59 23 * * * root /opt/surfnetids/scripts/scanbinaries.pl >/dev/null
#* 5 * * * root /opt/surfnetids/scripts/redirect_argos.pl >/dev/null
