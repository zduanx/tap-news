var client = require('./rpc_client');

client.add(12, 34, (response) =>{
  console.assert(response.result == 46);
});

client.getNewsSummariesForUser('test_user', 1, (response) =>{
  console.assert(response.result != null);
});

client.logNewsClickForUser('test_user', 'test_news');
