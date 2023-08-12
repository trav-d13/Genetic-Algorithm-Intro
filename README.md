# Genetic-Algorithm-Intro
An outline and example Genetic Algorithm to help understand the core principles underlying the meta-heuristic optimization algorithm


## Task
Target: `with enough probability anything is possible`

The overall task is to use a genetic algorithm to produce an individual that matches the above target.

### 1. Create an Individual
This task asks you to make an individual using an Object-Oriented Programming (OOP) approach. 
This means that each individual should contain a genome of letters (44 characters) including the space.
As well as a numerical value representing the fitness of the individual. 
In summary, the Individual class should contain two fields: 
- Genetics: The string containing the genetic information of the individual
- Fitness: Initialize to zero to start. This will be continued in task 3.

#### What is an Individual 
An individual is a single entity within a population. 
An individual contains a genotype (genetic material) and based on this genotype, 
a phenotype (individual characteristics) is created.

There exist two ways in which an individual is created: 
1. Randomly created within the initial population
2. The result of reproduction between two parent individuals


### 2. Create a Random Initial Population 
In this case, we focus on the random initialization of an individual.
The target string is 44 characters long, therefore each individual when randomly initialized should 
contain a random combination of 44 characters including the " " space. 
This random assortment then form the individual's genome, where the phenotype is if the assortment begins to make words
and have meaning.

I suggest, creating a population class that is capable of holding all individuals within a list. 
This will allow you to create a `random_population()` method to generate an initial population. 
Additionally, this structure will allow you to calculate the fitness per generation as well as other useful functions.

#### What is a Population
A population is the sum of all individuals in a generation. 
In this case, the first generation will be made up of individuals that have been randomly created. 

#### Random Individual Initialization Example

Individual 1: `assjftiuasn rtionsw sdf wefgenrbertb deuvieu` \
Individual 2: `ebefvwoev wevew  wevkmvns ievo eoivrnwwwver ` \
Individual 3: `iubgwe rypdldvnms webrvbuwyerv edvnweiiwrevd` \

#### Random Population Example
![img.png](resources/rand_pop.png)

### 3. Evaluate each Individual using a fitness function
Create a fitness function that can numerically evaluate the fitness of an individual based on their genetic 
composition (their phenotype). The fitness values for each individual informs reproduction and survival probabilities,
and it an essential element of a Genetic Algorithm. 

I would suggest placing the fitness function within the `Individual` class. 
Additionally, I would suggest calling it to calculate the fitness after each time a new individual is created. 

As a last additional task, I would suggest providing a method in you `Population` to capture the average fitness,
to serve as a measure of fitness per generation. This should gradually show an increase through the generations 
as individuals get closer to the `target`.

#### What is a fitness function
A fitness function is a numerical method of determining how close an individual is to reaching the optimal target.
The fitness function provides a way od determining which individuals are the fittest. The saying "Survival of the fittest" 
implies that fitter individuals have a higher probability of reproducing and passing their genetics to the next population. 

Please note, that the construction of the fitness function is one of the most difficult elements of a Genetic Algorithm, as 
its rules and structure determine the individuals fitness and influence reproduction. 
There can exists penalties and bonuses to ensure certain traits carry forth or to halt certain traits. 

Please feel free to modify the fitness score if you have an idea or want to test something out.


#### How to construct a simple fitness function
The `target` string consists of 44 characters. A simple fitness function will evaluate each individual's genetics against the
`target` string, and count the number of character matches in the correct position. This means that the perfect individual
matching the `target` will have a maximum score of 44. 

#### Example

Target: **with enough probability anything is possible**
![img.png](resources/fitness_example.png)

The first match exists at `index=1` matching the `i` characters.

### Implement a Selection Function
Within the GA selection exists to determine the selection of the parents that will reproduce. 
The traditional survival of the fittest method may lead to stagnation of the population genetics due to the same parents being selected. 
Multiple methods have been created to maintain genetic diversity while still maintaining a selection of good quality/ higher fitness parents. 
The `Selection.py` file contains a few of the possible selection methods. 
There will be variable results based on the selection method, so careful consideration of the correct method or experimentation is
crucial to determine what works for your genetic algorithm. 

Please note, the graphs below are sourced from my studies at Maastricht University, specifically the Intelligent Systems course
run by Kurt Driessens. 
Full accreditation goes to the original author.

Three possible selection methods are provided below. The selection methods have varying levels of implementation difficulty arranged in the
following order (easiest to hardest).
1. Tournament Selection
2. Roulette Wheel Selection
3. Boltzman Selection

I would suggest following the Minimal viable Product (MVP) method and completing the easiest selection method first. 
Once the GA is working, feel free to implement the more difficult methods and determine how they change the algorithm. 

#### Tournament Selection
Tournament selection randomly selects a subset of individuals from the population and holds a tournament
tp determine which Individual is the fittest within this sub-population. 
The fittest individual is then selected to act as a parent. 

In summary the following steps are performed: 
1. Randomly select a subpopulation of k size from the population
2. Determine the fittest individual from the tournament. 
3. This individual acts as a parent. 

Please note, the size of the subpopulation (k) can be used to tune the selection process. 


#### Roulette Wheel Selection
![rouletteWheel.png](resources/rouletteWheel.png)
The roulette wheel selection can be summarized as follows: 
The larger an individuals fitness the larger their probability of selection. The opposite also applies, such that the smaller
an individuals fitness the less probability of them being selected. 
This structure creates a selection behaviour where individuals of higher probability are more likely to be selected and pass good genetics
to the next generation, however random occurrences and suboptimal selections maintains the population diversity and will potentially
improve the genetic algorithm


#### Boltzman or Gibbs Distribution
The Boltzamn/ Gibbs selection is based on the Boltzman/ Gibbs distribution. 
It extends the capability of the Roulette wheel (see similarities in equations), however it includes Temperature (T). 
Temperature is a fine-tuning parameter that allows the selection to be more random (high values of T) or more deterministic (low values of T)
based on the values of T. 
**Note:** Determinsitc behaviour is such that the highest fitness individual is always selected. (Always selects the fittest individual).

![Pasted image 20230227111848.png](..%2F..%2Fobsidian%2Fimages_and_docs%2FPasted%20image%2020230227111848.png)

A common usage of this methodology is to begin with a more random (high T value) in order to introduce diversity into the population, 
and decrease Temperature (T) gradually as the generations continue in order to move from random behaviour to a more deterministic selection. 


