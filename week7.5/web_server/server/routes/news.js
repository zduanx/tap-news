var express = require('express');
var router = express.Router();
var rpc_client = require('../rpc_client/rpc_client')

/* GET news list. */
router.get('/userId/:userId/pageNum/:pageNum', function(req, res, next) {
  user_id = req.params['userId'];
  page_num = req.params['pageNum'];

  console.log(`Fetching news ... for user "${user_id}" page "${page_num}"`);
  rpc_client.getNewsSummariesForUser(user_id, page_num, function(response){
    res.json(response.result);
  })
});

// const fakeNews =  [
//     {'title': 'Zero Motorcycles CTO Abe Askenazi on the future of two-wheeled EVs',
//      'description': "Electric cars and buses have already begun to take over the world, but the motorcycle industry has been much slower to put out all-electric and hybrid models...",
//      'url': "https://techcrunch.com/2017/03/23/zero-motorcycles-cto-abe-askenazi-on-the-future-of-two-wheeled-evs/",
//      'urlToImage': "https://tctechcrunch2011.files.wordpress.com/2017/03/screen-shot-2017-03-23-at-14-04-01.png?w=764&h=400&crop=1",
//      'source': 'techcrunch',
//      'digest':"3RjuEomJo26O1syZbUdOHA==\n",
//      'time':"Today",
//      'reason':"Hot"
//    },
//    {'title': "Facebook security chief rants about misguided “algorithm” backlash",
//     'description': "\"I am seeing a ton of coverage of our recent issues driven by stereotypes of our employees and attacks against fantasy, strawman tech cos\" wrote Facebook..",
//     'url': "https://techcrunch.com/2017/10/07/alex-stamos/",
//     'urlToImage': "https://tctechcrunch2011.files.wordpress.com/2017/10/facebook-alex-stamos.png",
//     'source': 'techcrunch',
//     'digest':"3RjuEomJo26O1ZbUdOHA==\n",
//     'reason': 'Today'
//    },
//    {"title": "Benchmarks contradict ‘Apple slowed down my iPhone’ claims",
//     "description": "It's a refrain we all hear every year around September: \"I swear, whenever they release a new iPhone, Apple makes all the old ones run worse to make you..",
//     "url": "https://techcrunch.com/2017/10/06/benchmarks-contradict-apple-slowed-down-my-iphone-claims/",
//     "urlToImage": "https://tctechcrunch2011.files.wordpress.com/2017/06/2014-iphone-6-gettyimages-455672728.jpg",
//     'source': 'techcrunch',
//     'digest':"3RjuJo26O1ZbUdOHA==\n",
//     'reason':"Hot"
//    },
//    {"title": "Square Enix Brings Manga to VR - IGN Access - IGN Video",
//     "description": "Reading isn't something we're used to doing in virtual reality, but it might be soon.",
//     "url": "http://ca.ign.com/videos/2017/10/07/square-enix-brings-manga-to-vr-ign-access",
//     "urlToImage": "https://assets1.ignimgs.com/thumbs/userUploaded/2017/10/7/maxresdefault-1507410780676_1280w.jpg",
//     'source': 'ign',
//     'digest':"3RjuJo26O1ZA==\n",
//     'reason':'Recommend'
//    }
//  ];
//
//
// /* GET news list. */
// router.get('/', function(req, res, next) {
//     const news = fakeNews;
//     res.json(news);
//
// });

module.exports = router;
