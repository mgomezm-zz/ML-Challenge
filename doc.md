## Simulation

Let's assume we have a webpage with 5 links. Now out of 1000 impressions we can define certain events that might occur. Like for some reason most people are clicking on the first link but not the others. We can model this using a multinomial distribution, where n = # impressions and pi is the CTR for each link. We can use the Dirichlet conjugate prior on the CTR. What we get is Dir(alpha + c). Where alpha is the concentration parameter, and c is the link counts vector. 




We know that most people will not click on any of the links. So we can model

## Recommender

## Discussion
