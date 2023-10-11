0x00. AirBnB clone
- The console

Creation of a command interpreter to manage the hbnb projects

AirBnB clone Project done by
Elijah Omeruah &
Uchenna Oko


Description of the project
This is the first step towards building our first full web application: the AirBnB clone.The goal of the project is to deploy on our server a simple copy of the AirBnB website.The final version of this project will have:

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)


Aims & Objectives of this project
This will help to be able to manage the objects of our project:

- Creation of a new object (ex: a new "User" or a new "Place")
- Retrieval of an object from a file storage, a database etc… 
- Perform operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object


The created objects
The list of the objects (instances) that can be created are as follows:

- BaseModel
- User
- City
- Amenity
- State
- Review
- Place

Files and Directories
- models directory contains all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
- tests directory contains all unit tests.
console.py file is the entry point of our command interpreter.
- models/base_model.py file is the base class of all our models. It contains common elements:
	- attributes: id, created_at and updated_at
	- methods: save() and to_json()
- models/engine directory contains all storage classes (using the same prototype). For the moment I will have only one: file_storage.py.

The project's implementation will happen in the following phases:

Phase One
The first phase is to manipulate a powerful storage system to give an abstraction between objects and how they are stored and persisted. To achieve this, I will:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of my future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine
- Create a data model
- Manage (create, update, destroy, etc) objects via a console/command interpreter
- Store and persist objects to files (JSON files)

