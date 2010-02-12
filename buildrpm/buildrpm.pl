#!/usr/bin/perl

$svnurl = "http://svn.ids.surfnet.nl/surfids";
$package = "tunnel";
$version = "3.02";
$subtree = "tags";
$release = "stable-3.02";

##### DO NOT EDIT BELOW
$sourcedir = "./SOURCES/surfids-$package-$version";

# Downloading sources
`svn export $svnurl/$package/$subtree/$release/ $sourcedir/`;

# Deleting obsolete stuff
`rm -f $sourcedir/install_tn.pl`;
`rm -f $sourcedir/functions_tn.pl`;
`rm -f $sourcedir/tunnel_remove.txt`;
`mv -f $sourcedir/crontab.tn $sourcedir/tunnel-cron.d`;

# Creating .tar.gz
`tar -cvzf ./SOURCES/surfids-$package-$version.tar.gz $sourcedir/`;

# Building RPM
`rpmbuild -ba ./SPECS/surfids-tunnel.spec`;

