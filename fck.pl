#!/usr/bin/perl 

 
use HTTP::Request;
use LWP::Simple;
use LWP::UserAgent;
use Term::ANSIColor;
 
 
if ($^O =~ /MSWin32/) {system("cls"); system("color a");
}else { system("clear"); }
print color("bold blue"), "\n\t                          FCKeditor Grabber\n";
print color("bold blue"), "\t                        Results In", color("bold green"), " Live.txt";
print color("bold blue"), "\n\t                   Usage : ", color("bold yellow"), "perl $0 list.txt\n\n";
 
open(tarrget,"<$ARGV[0]") or die "$!";
while(<tarrget>){
chomp($_); 
$target = $_;
$target = "$target";
$websss = $target."/FCKeditor/editor/filemanager/connectors/asp/";
$website = $target."/FCKeditor/editor/filemanager/connectors/asp/connector.asp";
$nigga = "$target/FCKeditor/editor/filemanager/browser/default/browser.html?connector=$website";
$req=HTTP::Request->new(GET=>$websss);
$ua=LWP::UserAgent->new();
$ua->timeout(30);
$response=$ua->request($req);
if($response->status_line=~ /403/ )
 
 {
print color("bold green"), "\n[+] $target => FCK & Connector Detected \n";
open (TEXT, '>>Live.txt');
print TEXT "=================\n$nigga\n";
close (TEXT);
}
else{
print color("bold red"), "\n[+] $target => Try Other Path of FCK...\n";
$wbs1 = $target."FCKeditor/editor/filemanager/browser/default/connectors/asp/";
$fuckaa = "$target/FCKeditor/editor/filemanager/browser/default/browser.html?connector=connectors/asp/connector.asp";
$reqq=HTTP::Request->new(GET=>$wbs1);
$uaa=LWP::UserAgent->new();
$uaa->timeout(30);
$responsee=$uaa->request($reqq);
if($responsee->status_line=~ /403/  ) {  
 
print color("bold green"), "\n[+] $target => Path 2: FCK & Connector Detected \n";
open (TEXTt, '>>Live.txt');
print TEXTt "=================\n$fuckaa\n";
close (TEXTt);
 
 
    }else { print color("bold red"), "\n[+] $target => 404 Not Found\n";}
 
 
}
}
