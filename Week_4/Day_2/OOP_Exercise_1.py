"""Part 1: OOP Quiz.
 
Answers are stored in the ANSWERS dictionary below, and each concept is
demonstrated with a small runnable example further down the file.
Run this file to print every answer:  python3 quiz.py
"""
 
ANSWERS = {
    "What is a class?":
        "A class is a blueprint for creating objects. It defines the "
        "attributes (data) and methods (behaviour) that every object made "
        "from it will have. Defining a class does not create any object by "
        "itself, in the same way that a house plan is not a house.",
 
    "What is an instance?":
        "An instance is one concrete object built from a class. Calling the "
        "class, like dog = Dog('Rex'), creates an instance. Each instance "
        "has its own copy of the instance attributes, so changing one dog's "
        "name does not affect another's. 'Object' and 'instance' are used "
        "interchangeably.",
 
    "What is encapsulation?":
        "Encapsulation means bundling data and the methods that operate on "
        "that data inside one class, and controlling access to the internal "
        "state instead of letting outside code modify it freely. Python has "
        "no truly private attributes; it uses conventions: a single leading "
        "underscore (_balance) signals 'internal, please don't touch', and a "
        "double leading underscore (__balance) triggers name mangling, which "
        "renames the attribute to _ClassName__balance to avoid accidental "
        "clashes in subclasses. Properties let you expose a controlled "
        "read/write interface.",
 
    "What is abstraction?":
        "Abstraction means exposing only what a user of the class needs to "
        "know and hiding the implementation details behind a simple "
        "interface. You call list.sort() without knowing which sorting "
        "algorithm runs underneath. In Python, abstract base classes (the "
        "abc module) let you define an interface with methods that "
        "subclasses are required to implement. Encapsulation is about "
        "hiding data; abstraction is about hiding complexity.",
 
    "What is inheritance?":
        "Inheritance lets a class (the child or subclass) reuse and extend "
        "the attributes and methods of another class (the parent or "
        "superclass). It models an 'is a' relationship: a Dog is an Animal. "
        "The child can add new methods, or override inherited ones, and can "
        "call the parent's version with super().",
 
    "What is multiple inheritance?":
        "Multiple inheritance is when a class inherits from more than one "
        "parent at the same time: class C(A, B). The child gets the "
        "attributes and methods of every parent. It is powerful but can get "
        "confusing when two parents define the same method, especially in "
        "the 'diamond problem' where two parents share a common ancestor. "
        "Python resolves this with the MRO. It is most often used for "
        "mixins: small classes that add one focused piece of behaviour.",
 
    "What is polymorphism?":
        "Polymorphism means 'many forms': the same method call behaves "
        "differently depending on the object it is called on. Two common "
        "forms in Python are method overriding (subclasses redefine a parent "
        "method, so animal.speak() gives a different result per class) and "
        "duck typing (any object with the right method works, regardless of "
        "its class, because Python does not check types). Dunder methods "
        "like __repr__, __len__ and __add__ are polymorphism too: len() and "
        "+ work on many unrelated types.",
 
    "What is method resolution order or MRO?":
        "The MRO is the ordered list of classes Python searches when looking "
        "up an attribute or method on an object: the class itself first, "
        "then its parents, and so on up to object. It matters most with "
        "multiple inheritance, where it decides which parent's version wins. "
        "Python builds it with the C3 linearization algorithm, which "
        "guarantees a child always comes before its parents and that the "
        "order parents are listed is respected. You can inspect it with "
        "ClassName.__mro__ or ClassName.mro().",
}
