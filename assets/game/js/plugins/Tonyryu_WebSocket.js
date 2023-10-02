﻿//=============================================================================
// Tonyryu_WebSocket.js
//=============================================================================

/*:
 * @plugindesc Plugin de connexion WebSocket (1.00)
 * @author Tonyryu
 *
 * @param Host
 * @desc Adresse du serveur WebSocket
 * @default localhost:9000
 *
 * @help http://www.tonyryudev.com/
 * 
 */


var parameters = PluginManager.parameters('Tonyryu_WebSocket');
var tonyryuws_param_host = String(parameters['Host'] || 'tonyryu.hd.free.fr:9000');

/**********************************************************************
*----------------------------------------------------------------------
* Création d'une nouvelle "classe" Window_Gui
*  hérite de la classe Window_Base
*----------------------------------------------------------------------
**********************************************************************/
function WsManager() {
  throw new Error('This is a static class');
}

var $wsConnexion = null;

WsManager.start = function(){

  if( $wsConnexion !== null){
    if($wsConnexion.readyState === 3){
      delete $wsConnexion;
      $wsConnexion = null;
    }
  }

  if($wsConnexion === null){
    $wsConnexion = new WebSocket('ws://'+tonyryuws_param_host);
    $wsConnexion.onopen = function()
    {
      $gameSwitches.setValue(1, true);
      $wsConnexion.send('RMMV_WS');
      console.log("Connection is open");
    };

    $wsConnexion.onmessage = function (evt) 
    { 
      var received_msg = evt.data;
      console.log("Message is received..." + received_msg);
      var tabMsg = received_msg.split('|');
      if(tabMsg[0]){
        switch(tabMsg[0]) {   // Ce switch/case doit être modifié selon les commandes de votre netcode
          case 'GAIN_GOLD':
            $gameParty.gainGold(1000);
            break;
	  case 'CMD_1':
            // Code de la commande CMD_1
            break;
          case 'CMD_2':
            // Code de la commande CMD_2
            break;
          default:
            // Code lorsque commande inconnu

        }

      }
    };

    $wsConnexion.onclose = function()
    { 
      $gameSwitches.setValue(1, false);
      console.log("Connection is closed..."); 

    };
  }
};

WsManager.send = function(pMessage){
  if($wsConnexion.readyState === 1){
    $wsConnexion.send(pMessage);
  }
};

WsManager.stop = function(){
  if($wsConnexion){
    if($wsConnexion.readyState === 1)
      $wsConnexion.close();
  }
  delete $wsConnexion;
  $wsConnexion = null;
};

WsManager.isConnected = function(){
  if($wsConnexion)
    return $wsConnexion.readyState === 1;
  return false;
};

var _tonyryuws_Game_Interpreter_pluginCommand = Game_Interpreter.prototype.pluginCommand;
Game_Interpreter.prototype.pluginCommand = function(command, args) {
  _tonyryuws_Game_Interpreter_pluginCommand.call(this, command, args);
  if(command === 'WS_START')
    WsManager.start();
  if(command === 'WS_STOP')
    WsManager.stop();
  if(command === 'WS_SEND')
    WsManager.send(args[0]);
  if(command === 'WS_SEND_TEXT_FLOWER')
    var splitted_command=args[0].split("?");
    if (splitted_command != undefined){
	if ($gameVariables.value(splitted_command[1]) == "crann" || $gameVariables.value(splitted_command[1]) == "Crann"){
	// changing value for global variable dependind on answer : \v[2] == true
	$gameVariables.setValue(2, 1)
	WsManager.send(splitted_command[0]+"?"+$gameVariables.value(splitted_command[1]));
	} else {
	// changing value for global variable dependind on answer : \v[2] == false
	$gameVariables.setValue(2, 0)	
	}
    }else{
	WsManager.send(args[0]);}

};



