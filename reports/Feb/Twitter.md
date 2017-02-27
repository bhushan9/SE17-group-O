In order to fulfil the social media distribution side of our news summary application, we decided to go with Twitter to publish news. We looked into Facebook, but the API for publishing text to pages was quite cumbersome and seemed quite taxing to actually implement.

We decided to write this part of the project in python. Since the server side framework all runs in python, it would be easier to integrate this code with that of the flask framework. The Twitter API has support for many python wrappers. We decided to go with twython since it had the most documentation available and a decent sized user base. It also supports features that may be useful in the future including the ability to upload images.

A Twitter account for our app was specifically created in order to publish news stories. We also used the account to access the Twitter developer page which allowed us to find the API keys. We then set up a small python script that allows us to publish text to our Twitter page by passing text to the python script.

We then tried integrating the news summarization API with the python script. The summarization API often times returns stories longer than 140 characters. Therefore, each post had to be split up into chunks and sent out in order. There were also problems about where to split the chunks. Often times words would get split in half between posts leading to text that was hard to read. This was solved by only allowing posts to split after a space character was found.

Currently, we are trying to find a way to run the twitter script in the background of our server at a certain time interval. Once news is pulled, summarized, and saved, we want the twitter script to be called and each summarized story to be published to our page.

Roadblocks include having to deal with timing of the news updates and the updates of the twitter page. Sometimes there are instances in which the news API updates but actually returns no data, which may be problematic for the Twitter script.

Also the formatting for multiple subsequent tweets about the same topic does not follow the normal twitter convention. This makes stories more difficult to read. It may or may not be possible to reply to your own tweet like we would like.
