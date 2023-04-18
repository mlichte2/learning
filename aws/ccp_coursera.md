# AWS Certified Cloud Practicioner

[TOC]

---

## Domain 1: cloud concepts

### Benefits of the AWS Cloud

#### Define the AWS Cloud and its value proposition

AWS Cloud
: Amazon Web Services (AWS) is the world’s most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services from data centers globally. Millions of customers—including the fastest-growing startups, largest enterprises, and leading government agencies—are using AWS to lower costs, become more agile, and innovate faster.

AWS Cloud Value Proposition
: **Security** -- AWS offers multiple Security and Compliance services for various applications. Apart from the Shared Responsibility Model, there are options for configuring extra security measures.
: **Agility** -- Applications can be developed and deployed globally across multiple geolocations within minutes. The speed of experimentation, development and deployment is exponentially higher compared to applications developed on-premises.
: **Flexibility** -- AWS offers multiple services for various applications. There are over 200 products that support services to run all kinds of workloads.
: **Elasticity** -- Applications can scale the resources required for smooth operability based on the demand — the application capacity is sufficient to deal with the incoming requests while paying for only what they use.
: **Cost** -- AWS makes it easy to scale up and down based on demand and removes the need for an on-premise data centre to reduce costs. By using the pay as you go model, costs incurred can be monitored and reduced.

Question walkthrough

- Q: The ability to horizontally scale Amazon EC2 instances based on demaind is an example of which concept of the AWS Cloud value proposition?
- A: Elasticity

#### Identify aspects of AWS Cloud economics

AWS Cloud economics
: How operating in AWS can affect your orgs ownership and operational costs

Total Cost of Ownership (TCO) concepts

1.  Operational expenses (opex)
    : day-to-day costs to your org such as services and items that get used up. examples: printer toner, website hosting, etc
2.  Capital expenses (capex)
    : costs associated with creating the longer-term benefits. purchasing a building, servers, power back-ups
3.  Labor costs associated with on premises operations
    : costs incured to handle on premecise infra
4.  Impact of software licensing laws
    : can your software licenses be moved to the cloud, or are there ones with AWS that you can use instead

Cost reduction operations:

1. Right size infrastructure
2. Automation
3. Reduce Compliance Scope
4. Managed services

Question walkthrough

- Q: Which on premises expense will be reduced if the company migrates their app to amazon ec2?
- A: Server hardware costs

Tip: even when the stem does not state it; always look for the most correct response.

#### Explain the cloud architecture design principles

1. Design for failure
   : what and how components fail -- building an app that could run on a single server but runs on two instead (backup).
2. Decouple components vs monolithic architecture
   : monolothic arch -- all processes are tightly coupled or connected and run as a single service. SO if there is a demand spike the entire app must be scaled
   : decoupled arch -- decoupling the database from the app so in case there is an issue with scaling the app there isnt downtime for the db
3. Implementing elasticity in the cloud vs on-premises
   : AWS allows dynamically changing capacity based on demand (2, 200, 2000 servers depending on demand), many other things can be scalled too.
4. Think parallel
   : serial and sequencial dependencies can cause issues, if there is an issue with one -- it will affect other processes. Example would be using a load balancer to distribute requests.

Question Walkthrough

- Q: Which of the following is an AWS Cloud architecture design principle
  : implement single points of failure, implement loose coupling, implement monolithic design, implement vertical scaling?
- A: implement loose coupling -- kind of a trick question A + B are anti-patterns and D would be right if it was horizontal

---
