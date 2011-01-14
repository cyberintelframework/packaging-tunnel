#!/usr/bin/perl

# Checks the config and each config item for usage
# Config items with 0 usage should be checked and/or deleted

$config = "/opt/surfnetids/tunnel/trunk/surfnetids-tn.conf";
$dst = "/opt/surfnetids/tunnel/trunk/";

@confitems = `cat $config | grep c_ | grep -v \\\# | awk -F\\\$ '{print \$2}' | awk '{print \$1}'`;

foreach $item (@confitems) {
    chomp($item);
    $chk = `grep -R $item $dst | grep -v \\.svn | grep -v surfnetids-tn.conf | wc -l`;
    chomp($chk);
    print "$item - $chk\n";
}
