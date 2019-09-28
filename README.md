# PYGHACK

## **HOME @ PYGHACK.** focuses on real problems within the community.


We want to explore various factors that may impact poverty levels in Champaign county. In doing so, we identify areas in which more resources need to be allocated to help alleviate the issue.

While researching, we also discovered a disturbing truth:
the Champaign area has one of the highest poverty rates in all of Illinois.

We trained a random forest classifier on data provided by [Champaign County Regional Planning Comission](https://ccrpc.org/data/?category_name=planning), using cities, towns, and municipalities as data points, and key features such as:
- Average Household Size
- Language Most Often Spoken at Home
- Mean Travel Time to Work
- Assessed population

to generate a model that would identify the most important features that influence the poverty rate. We found that, (after median household income), the most influential features were average household size and language most often spoken at home.

In Progress
- [x] Aggregate all data in one location
- [x] train the model on the data
- [x] Create a website
- [ ] Host the website off a service such as Azure or AWS
