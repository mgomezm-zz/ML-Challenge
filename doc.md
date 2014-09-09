
# Simulation

### Item Attributes

Assumed a finite vocabulary of size 50.  Attributes for a link where chossen by randomly picking 10 items without replacement.

### Pageviews 

Let's assume we have a webpage with 5 links. Now out of 1000 impressions we can define certain events that might occur. For example, most people are clicking on the first link but not the others. We can model this using a multinomial distribution, where n = # impressions and theta_i is the Click Through Rate (CTR) for each link plus the probability of a user leaving. 

For example, the click counts could be [1, 10, 5, 50, 100] and the number of user leaving would be just 1000 minus the sum of all click counts.  

We can use the Dirichlet conjugate prior on the CTR. After some math we get a posterior ~ Dir(alpha + c), where alpha is the concentration parameter, and c is the link counts vector. We can use this posterior to control share counts.  

### Shares

Simulating share counts is more interesting. We need to consider pageviews and the similarity of a link's attributes to the rest. 

For each link we can simulate the share counts with binomial distributeion where n = #impression and the thetas can be computed as follows:
> * To tackle pageviews we can use the posterior Dirichlet probabilities. 
> * We can compute the similarity matrix on the attributes. We put preference on the link's with attriubtes that are more informative.
> * Then we use the probability a user leaving the webpage as a smoothing paramter on the probabilities specified above. 

# Recommender

We can say that an item that is similar to a website with high shares and high page views will get many shares. 

Some possibilites, a link may have:
> 
> * large page views and large shares. >>>>
> * small page views and large shares. >>>
> * large page views and small shares. >>
> * small page views and small shares. >

For our recommender we use a weighted cosine similarity. The weighting takes into consideration both the click and share counts. 

Alternatives include clustering algoritms, UV decomposition. Using clustering would have the advantage of doing most of the work offline. Using your historic data you train and obtain the clusters. Then, when you have a new data point classifcation involves a simpe dot product. 


# Discussion

A Cool and fun problem. I spent around 80 percent of the time on the simulation. It was interesting thinking about how to simulate pageviews and share counts. I skimmed over some papers to make sure my intution was correct. 

My recommender solution is simple but works effectively. It would be interesting to compare performance with other algorithms. 


## References

M. Regelson, D. Fain, [Predicting Click-Through Rate Using Keyword Clusters](http://diyhpl.us/~bryan/papers2/marketing/Predicting%20click-through%20rate%20using%20keyword%20clusters.pdf)

X. Wang, W. Li, Y. Cui, [Click-Through Rate Estimation for Rare Events in Online Advertising](http://www.cs.cmu.edu/~xuerui/papers/ctr.pdf)

D. Asanov, [Algorithms and Methods in Recommender Systems](https://www.snet.tu-berlin.de/fileadmin/fg220/courses/SS11/snet-project/recommender-systems_asanov.pdf)
