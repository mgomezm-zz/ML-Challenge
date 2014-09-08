ML Challenge

The following actions are logged from a web site, in the form of a logfile that looks like this:

pageview    http://foo.com/1001
pageview    http://foo.com/1002
pageview    http://foo.com/1002
pageview    http://foo.com/1003
share       http://foo.com/1002
share       http://foo.com/1003

...


A separate file exists with attributes of each url.  Attributes are in list form:

http://foo.com/1001  [foo, bar, slimy]
http://foo.com/1002  [foo, slimy]
http://foo.com/1003  [slimy, gobbledy, gook]

….


The above file contains 10 new items that have never been viewed before.  An email blast is being sent which will contain one of these 10 new items.  The goal of the email blast is to get as many shares as possible, as these are seen as highly valuable to the web site’s ability to grow.

Your job is to figure out which of the 10 new items will result in the greatest number of share events.  Note that a share cannot exist without a prior pageview.


Deliverables:

1. A simulated dataset for the two files above, using whatever method you want.  It should be as realistic as possible in that some items will have high click rates but low share rates, while others have high share rates but low click rates.  It should also reflect a dependency between attributes and click/share rates, the complexity of which is up to you.

2. Python code implementing an machine learning algorithm to predict the share rate.  Please provide a repo on github with the code along with clear documentation for how to run it.

3. A written explanation of your approach and discussion of why it is better or worse than other approaches.

The expected time to complete the task with a minimal solution is 4 hours, with more complex solutions taking longer.  If you feel limited by time, please describe options you considered that would have taken too long to implement.

------------------------------------------------------------------------------

We can say that an item that is similar to a website with high shares and high page views will get many shares. 

Some possibilites, a link may have:

* large page views and large shares. >>>>
* small page views and large shares. >>>
* large page views and small shares. >>
* small page views and small shares. >

We rank them base on importance in determining whether an item will get shared.




#############################################################################





Several (let's say up to three) large CSV files (up to two million rows and up to 255 columns each) all have a shared key.  

Write a program that zips them together.

Inputs are filenames and column indexes of the shared key.  

Output is a single file containing the merged result of all the input files.  

Your program should take into account all CSV conventions; please provide test file(s) as part of the exercise.  

Your program should be a single runtime (i.e. don't use Hadoop, etc.).














