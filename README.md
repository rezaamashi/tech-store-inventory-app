- [Overview](#orgeb20f01)
- [Principle of Object Oriented Programming](#orgdd84109)
  - [Encapsulation](#org3fa087e)
    - [Type Accessing Method](#org26d7651)
    - [Static and Class Methods](#orgb438ba8)
    - [Read Only Attribute](#org38d6f7c)
  - [Abstraction](#org69933ac)
    - [Workflow](#orgf8c61ec)
  - [Inheritance](#orga4fdf34)
    - [Access Modifiers](#orgb52aa57)
  - [Polymorphism](#org3bb0d31)
- [Attributes](#org63afbc8)
  - [Class](#org78e86da)
  - [Instances](#org35d4025)
- [Constructor](#orgb01c9cf)

<a id="orgeb20f01"></a>

# Overview

This is my personal repo on doing [Object Oriented Programming with Python - Full Course for Beginners - YouTube](https://www.youtube.com/watch?v=Ej_02ICOIgs).

<a id="orgdd84109"></a>

# Principle of Object Oriented Programming

<a id="org3fa087e"></a>

## Encapsulation

[ce4727](https://github.com/rezaamashi/tech-store-inventory-app/commit/ce4727f812260e203deb2a57e199a4e56819ddb6)

<a id="org26d7651"></a>

### Type Accessing Method

1.  Getting Method => Retrieving Information
2.  Setting Method => Changing Information

Programmer also able to set certain attribute to be read only, only allowing to get certain methods and not allowing to setting methods.

<a id="orgb438ba8"></a>

### Static and Class Methods

1.  Static Methods

    [a52017](https://github.com/rezaamashi/tech-store-inventory-app/commit/a520177be372de4974d4c2dab8d268a58682bab6)
    This should do something that has relationship with the class, When we need to use method that are not necesarily need to be unique per instance. Set up using decorator `@staticmethod`

2.  Class Methods

    [3af0a1](https://github.com/rezaamashi/tech-store-inventory-app/commit/3af0a1c73ed45cffdac149107deff0555b2b1d5a)
    This should also do something that has a relationship with the class, but usually, those are used to manipulate different structures of data to instantiate objects, like from CSV. Set up using decorator `@classmethod`

<a id="org38d6f7c"></a>

### Read Only Attribute

[761243](https://github.com/rezaamashi/tech-store-inventory-app/commit/761243cc3966bd1e7959fcf5e78058e8328a592c)
To set an immutable attribute on class. Set up using decorator `@property`

<a id="org69933ac"></a>

## Abstraction

[836e8d](https://github.com/rezaamashi/tech-store-inventory-app/commit/836e8d71406db7435034f781dd0814bbcc515988)
Ability to only include certain methods or attributes that are important and hiding deemed unnecessary to be known methods and attributes.

<a id="orgf8c61ec"></a>

### Workflow

The way this principle applied is through setting up a point of access to the classes, for more ease of use.

1.  Interface

    Point of access for user to use the implementation without going deep into understanding the implementation ([Blackboxing at DuckDuckGo](https://duckduckgo.com/?q=blackboxing&ia=web))

2.  Implementation

    The coded methods and attribute that not necessarily to be known for the intended purpose of the program to be used.

<a id="orga4fdf34"></a>

## Inheritance

[eb0116](https://github.com/rezaamashi/tech-store-inventory-app/commit/eb01161af8a246eb4bc31ed4938347e3f13b2fcd)
Ability to use methods and attributes from superclass or parent class. While also able to override and adding subclass or child classes specific methods and attributes.

<a id="orgb52aa57"></a>

### Access Modifiers

A set of rules on which classes have access to other classes, methods, or attributes

1.  Public

    Accessible from anywhere in the program

2.  Private

    [e1960a](https://github.com/rezaamashi/tech-store-inventory-app/commit/e1960afdad4bac639c67c2d639baad5bc9f39450)
    Accessible only from within the same class that the member is defined. This allow programmer to create member with the same name in the program without conflicting with each other [although it is not ideal]

3.  Protected

    Accessible within the class it is defined, as well as any subclasses of that class.

<a id="org3bb0d31"></a>

## Polymorphism

[a0cf1b](https://github.com/rezaamashi/tech-store-inventory-app/commit/a0cf1b451adeac270d8f6a3b70994986288cff5f) Ability to take on many forms. In this principle objects could take different type of input and keep functioning and producing the intended output.

Note: Make sure to be selecting the exact intended morph as it would not return error directly.

<a id="org63afbc8"></a>

# Attributes

[4bcf6b](https://github.com/rezaamashi/tech-store-inventory-app/commit/4bcf6b88fc49bdc2a2429434fa95b41356344f47)

<a id="org78e86da"></a>

## Class

<a id="org35d4025"></a>

## Instances

<a id="orgb01c9cf"></a>

# Constructor

[939476](https://github.com/rezaamashi/tech-store-inventory-app/commit/9394763bd7a4af41029260d7e866c9c74ff93128)
