#Tasks 
"""1.
Given the following data from an e-commerce app: out of 500 users, 120 bought phone accessories, 80 bought a phone, and
50 bought both, calculate the probability that a user bought a phone given they already bought accessories (P(Phone|Accessories))

solution:
bougth phone accessories P(A) = 120
bougth a phone P(B) = 80
bought both P(A and B) = 50

P(B/A) = P(A and B) / P(A)
           
       = 50/120
       = 0.167

persentage = 167%

interpretation :The probability that a user bought a phone given that they already bought phone accessories is 0.4167 or 41.67%. This means
that approximately 41.67% of users who purchased phone accessories also purchased a phone"""

"""2.
Imagine you are analyzing Flipkart's user data: 30% of users buy headphones, and among those, 40% later buy a smartphone.
Calculate the conditional probability that a randomly selected user buys a smartphone, given they have already bought headphones.
<br><br><em><strong>Hint:</strong> Use the formula for conditional probability: P(A|B) = P(A and B) / P(B).</em>

solution:

Probability of buying headphones = 30% = 0.30
Probability of buying a smartphone among headphone buyers = 40% = 0.40

so  formula: P(A/B) = P(A and B)/ P(B)

P(A/B) = 0.40  = 40%

interpretation:
The conditional probability of a user buying a smartphone, given that they have already bought headphones, is 0.40 or 40%.
This means that 40% of users who purchased headphones later also purchased a smartphone."""
            

"""3.
Write a Python function bayes_churn_probability(prior_churn, prob_email_given_churn, prob_email) that uses Bayes’ Theorem to
compute the probability a user will churn given they received a 'we miss you' email. Test your function with prior_churn=0.15,
 prob_email_given_churn=0.6, prob_email=0.25."""

def bayes_churn_probability(prior_churn,
                            prob_email_given_churn,
                            prob_email):

    probability = (prior_churn * prob_email_given_churn) / prob_email

    return probability


# Test the function
result = bayes_churn_probability( 0.15,0.6,0.25)

print("Probability of Churn:", result)
print("Percentage:", result * 100, "%")

"""4.
A digital wallet app detects fraud based on spending patterns. If 2% of all transactions are fraudulent, and the app’s alert 
system correctly flags 90% of fraudulent transactions but also falsely flags 5% of normal transactions, use Bayes’ Theorem to
calculate the probability that a transaction is actually fraudulent when flagged by the alert system.<br><br><em><strong>Hint:
</strong> Define events: F = fraud, A = alert. Use Bayes’ formula: P(F|A) = [P(A|F) * P(F)] / P(A).</em>"""

"""solution:

Transactions of fraudulent = 0.02
transactions of normal = 0.98
Alert flags of fraudulent transactions = 0.90
flags on normal transactions = 0.05

Formula:

P(A)=P(A/F)P(F)+P(A/bar F)P(bar F)

P(A)=(0.90)(0.02)+(0.05)(0.98)

=0.018+0.049

{P(A)=0.067}

 Bayes' Thearm:

P(F|A)=P(A|F)*P(F)/P(A)

P(F|A)=(0.90)(0.02)/(0.067)

=(0.018)(0.067)

=0.2687

Percentage :
0.2687*100=26.87%

interpretaion: The probability that a transaction is actually fraudulent when flagged by the alert system is approximately 26.87%. This means
that not every transaction flagged by the system is fraudulent. Some alerts may be false positives because the system can also
flag normal transactions. The digital wallet company should verify flagged transactions before taking further action."""

"""5.
Use ChatGPT or another AI tool to generate a real-world scenario where conditional probability is used in a food delivery app
(like Zomato or Swiggy), and explain how Bayes’ Theorem could help improve their recommendation system. Paste the AI’s output
and add one sentence of your own analysis"""

""" Real-World Scenario_Zomato**

AI-Generated Scenario:

A Zomato customer frequently searches for Pizza and clicks on Pizza restaurant recommendations. Zomato can use Conditional
   Probability to understand the customer's food preferences.

Suppose the probability of ordering Pizza is 20%, the probability of clicking a Pizza recommendation when the customer orders
Pizza is 80%, and the probability of clicking a Pizza recommendation when the customer does not order Pizza is 30%.

Using Bayes' Theorem:

P(Pizza Order | Click) = (0.80 * 0.20) / 0.40

= 0.40 or 40%.

This means that after clicking on a Pizza recommendation, the probability of the customer ordering Pizza is 40%.

Zomato can use this information to recommend Pizza restaurants, special offers, and related food items to customers. This helps
improve the recommendation system and customer experience.

My Own Analysis: I think Bayes' Theorem helps Zomato understand customer choices and recommend food according to their interests."""





