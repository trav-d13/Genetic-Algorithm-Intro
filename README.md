# Genetic-Algorithm-Intro
An outline and example Genetic Algorithm to help understand the core principles underlying the meta-heuristic optimization algorithm


## Task
Target: `with enough probability anything is possible`


The overall task is to use a genetic algorithm to produce an individual that matches the above target.

### Create an Individual
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

### Create a Random Initial Population 
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
