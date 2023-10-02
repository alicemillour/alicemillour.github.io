<?php
//print_r($_GET)

switch($_GET['action'])
{
  case 'store_text': 
     //number1 = (int)$_GET['number1'];
     //number2 = (int)$_GET['number2'];
     //result = number1 + number2;
     
     echo "\nPHP : In store_text (php)\n";
     echo $_GET['text'];
     echo "sending file_put_contents";
     echo file_put_contents("flower-text.txt",$_GET['text'],FILE_APPEND); 
     file_put_contents("flower-text.txt","\n",FILE_APPEND);
     break;    
  case 'store_rhyme': 
     //number1 = (int)$_GET['number1'];
     //number2 = (int)$_GET['number2'];
     //result = number1 + number2;
     
     echo "\nPHP : In store_text (php)\n";
     echo $_GET['text'];
     echo "sending file_put_contents";
     echo file_put_contents("nuage-text.txt",$_GET['text'],FILE_APPEND); 
     file_put_contents("nuage-text.txt","\n",FILE_APPEND);
     break;   
   case 'store_bibs': 
     //number1 = (int)$_GET['number1'];
     //number2 = (int)$_GET['number2'];
     //result = number1 + number2;
     
     echo "\nPHP : In store_text (php)\n";
     echo $_GET['text'];
     echo "sending file_put_contents";
     echo file_put_contents("bibs-text.txt",$_GET['text'],FILE_APPEND); 
     file_put_contents("bibs-text.txt","\n",FILE_APPEND);
     break;  
  case 'store_song': 
     //number1 = (int)$_GET['number1'];
     //number2 = (int)$_GET['number2'];
     //result = number1 + number2;
     
     echo "\nPHP : In store_text (php)\n";
     echo $_GET['text'];
     echo "sending file_put_contents";
     echo file_put_contents("song-text.txt",$_GET['text'],FILE_APPEND); 
     file_put_contents("song-text.txt","\n",FILE_APPEND);
     break;  

} 
?>

