animalSheltersDB
===================

AnimalSheltersDB is a database developed in Python with SQLAlchemy to adopt puppies.

The repository contains the virtual machine configuration to use with Vagrant and the code of the project in the /vagrant/animalSheltersDB/ directory.

## Files

The project is composed of three files:

- ``database_setup.py``: creates the database schema using SQLAlchemy
- ``puppypopulator.py``: populates the database
- ``queries.py``: contains the functions to use the database

## Installation and use

To run this project you need to have installed VirtualBox and Vagrant.

Once started and logged in the vagrant machine, go to ``/vagrant/animalSheltersDB/`` directory.

To create the database schema execute ``$ python database_setup.py``

To populate the database execute: ``$ python puppypopulator.py``

To use the function in ``queries.py`` add ``import queries`` in your Python program

## Functionality

These program provides the following functionalities:

1. ``getPuppiesOrderByName()``: queries all the puppies and return the results in ascending alphabetical order
2. ``getPuppiesYoungerThanSixMonths()``: queries all the puppies that are less than 6 months old organized by the youngest first
3. ``getPuppiesOrderByWeight()``: queries all the puppies by ascending weight
4. ``getPuppiesInShelters()``: queries all the puppies grouped by the shelter in which they are staying
