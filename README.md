# Genetic-Algorithm-Intro
An outline and example Genetic Algorithm to help understand the core principles underlying the meta-heuristic optimization algorithm


## Task
Target: `with enough probability anything is possible`


The overall task is to use a genetic algorithm to produce an individual that matches the above target.

### 1. Create an Individual
This task asks you to make an individual using an Object Oriented Programming (OOP) approach. 
This means that each individual should contain a genome of letters (44 characters) including the space. 
This individual attribute should be easily accessible and modifiable, so make a `getter` and a `setter` method to access it and set it.

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