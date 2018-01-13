var client = require('./rpc_client');

client.add(12, 34, (response) =>{
  console.assert(response.result == 46);
});
