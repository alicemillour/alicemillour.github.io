var http = require('http');
var server = http.createServer();
// Ajout Alice
var io = require('/usr/local/lib/node_modules/socket.io/').listen(server);

io.sockets.on('connect', function (socket) {
  console.log('Un client se connecte, socket.id = ' + socket.id);
  // code à lancer quant un client se connecte

  // Quand le serveur reçoit un signal de type "message" du client    
  socket.on('message', function (message) {
    console.log('Un client me parle ! Il me dit : ' + message);
    var tabMsg = message.split('|');
    if(tabMsg[0]){
      switch(tabMsg[0]) {   // Ce switch/case doit être modifié selon les commandes de votre netcode
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

  });
  socket.on('disconnect', function () {
    console.log('Un client se déconnecte, socket.id = ' + socket.id);
    // code à lancer quant un client se déconnecte

  });
});

console.log('Lancement du serveur sur port 9000');
server.listen(9000);
