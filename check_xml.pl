#!/usr/bin/perl
#
# This script requires the package `perl-OBS-XML`

use strict;
use warnings;

use lib "/usr/lib/obs/server";

use XML::Structured;
use Data::Dumper;
use OBS::XML;

my $dtd     = $OBS::XML::servicetype;
my $hashref = XMLinfile($dtd, $ARGV[0]);

exit 0;
