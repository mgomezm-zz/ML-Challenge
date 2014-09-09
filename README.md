ML-Challenge
============

##Usage

    python simulation.py 
    python recommmender.py


> * The first command will simulate pageviews/share events, item attributes, test attributes, and write the datafiles to "./../data/". 
> 
> * The second command will take the contents  of the data folder and recommend the test item that will produce the highest shares. 

---------------------------------------------------------------------------------------------
## Simulation

#### Item Attributes

Assuming a finite vocabulary of size 50.  Attributes for a link are chosen by randomly picking 10 items uniformly without replacement.

#### Pageviews 

Let's assume we have a webpage with 5 links. Out of 1000 impressions we can define certain events that might occur. For example, the click counts could be [1, 10, 5, 50, 100] and the number of user leaving would be just 1000 minus the sum of all click counts. That is, c = [1, 10, 5, 50, 100, 834]. 

We can model this using a multinomial distribution, where n = #impressions and theta_i is the Click Through Rate (CTR) for each link plus the probability of a user leaving.

We will use the conjugate prior of the multinomial distribute, the Dirichlet, on the thetas. After doing some math we get that the posterior ~ Dir(alpha + c), where alpha is the concentration parameter, and c is the link counts vector. We can use this posterior to control share counts.

#### Shares

Simulating share counts is more interesting. We need to consider pageviews and how similar a link is to to other links (similarity matrix on attributes). 

For each link we can simulate the share counts using the binomial distributeion where n = #impression and the thetas can be computed as follows:
> * We can obtain a probabilistic measure for pageviews using the poserior, Dir(alpha + c). => pi_clicks
> * Using the similarity matrix, we count the number of really similar items (based on some threshold). From this we can obtain a measure of how informative a link is.  => pi_entropy
> * The probability a user leaving the webpage. => gamma

We obtain the following: theta = (1-gamma) * pi_clicks + gamma * pi_entropy

The idea being that if more users are staying on the webpage, then page views should be more important. Whereas if users leave the webpage more often, then we should emphasize the imformative links more. 

## Recommender

We can say that an item that is similar to a website with high shares and high page views will get many shares. 

Some possibilites, a link may have:
> 
> * large page views and large shares. >>>>
> * small page views and large shares. >>>
> * large page views and small shares. >>
> * small page views and small shares. >

For our recommender we use a weighted cosine similarity. The weighting takes into consideration both the click and share counts. 

Alternatives include clustering algoritms and UV decomposition. Clustering would have the advantage of doing most of the work offline. Using the historic data you train and obtain the clusters. Then, when you have a new data point classifcation involves a simpe dot product. 

## Discussion

A Cool and fun problem. I spent around 80 percent of the time on the simulation. It was interesting thinking about how to simulate pageviews and share counts. I skimmed over some papers to make sure my intution was correct. 

My recommender solution is simple but works effectively. It would be interesting to compare performance with other algorithms. 


## References

M. Regelson, D. Fain, [Predicting Click-Through Rate Using Keyword Clusters](http://diyhpl.us/~bryan/papers2/marketing/Predicting%20click-through%20rate%20using%20keyword%20clusters.pdf)

X. Wang, W. Li, Y. Cui, [Click-Through Rate Estimation for Rare Events in Online Advertising](http://www.cs.cmu.edu/~xuerui/papers/ctr.pdf)

D. Asanov, [Algorithms and Methods in Recommender Systems](https://www.snet.tu-berlin.de/fileadmin/fg220/courses/SS11/snet-project/recommender-systems_asanov.pdf)
