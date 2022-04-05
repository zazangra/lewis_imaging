#Lewis Imaging on a Causal Model


This is a Python script to perform Lewis Imaging as presented in the following article:
Pearl, Judea (2017), "Physical and Metaphysical Counterfactuals: Evaluating Disjunctive Actions", Journal of Causal Inference, 5 (2):1--10 ()

This method is used in statistics, causal inference, probability theory and formal philosophy 
in order to compute the probability that an event "A" occurs under the assumption that another event "B" happened.
Performing this procedure is different from calculating the conditional probability of A given B. 

The script takes as input the information describing a causal model 
(for an overview on causal models see  Pearl, Judea (2000), "Causality", Cambridge University Press);
in particular it needs:

1) the number and name of the variables in the model;
2) the conditional probabilities among the variables;
3) a relation of smilarity over all the possible realizations of the variables.

After having specified 1, 2 and 3, the script computes the probability of a given counterfactual B -> A,
i.e. the probability that B occurs under the assumption that A happened.

For example, given a set of three variables X, Y and Z, given the conditional dependencies among those, and
given a relation of similararity among all the possible configurations of X; Y and Z, the script can compute
the probability of X=1 -> Z=1, i.e. the probability that Z takes value 1 under the assumption that X assumed value 1.

