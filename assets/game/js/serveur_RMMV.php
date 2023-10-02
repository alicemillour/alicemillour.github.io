#!/usr/bin/env php
<?php

require_once('./websockets.php');

class rmmvServer extends WebSocketServer {

  function __construct($addr, $port, $bufferLength) {
    parent::__construct($addr, $port, $bufferLength);
    $this->userClass = 'MyUser';
  }

  //protected $maxBufferSize = 1048576; //1MB... overkill for an echo server, but potentially plausible for other applications.
  
   protected function process ($user, $message) {
	echo $user->socket ." : RMMV process : " . $message . "\n";
	    if($message == 'SEND_GOLD'){
	      foreach($this->users as $userId => $anotherUser)
	      {
		// si user différent
		if($anotherUser != $user)
		{
		  $this->send($anotherUser, 'GAIN_GOLD');
		}
	      }
	    }
 }
 
 protected function connected ($user) {
   echo $user->socket ." : RMMV connected\n";
 }
 
 protected function closed ($user) {
   echo $user->socket ." : RMMV closed\n";
 }
}

$echo = new rmmvServer("0.0.0.0","9000",1048576);

try {
  $echo->run();
}
catch (Exception $e) {
  $echo->stdout($e->getMessage());
}
