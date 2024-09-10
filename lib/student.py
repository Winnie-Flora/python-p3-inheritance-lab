#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.knowledge = []
    
    def learn(self, knowledge_str: str):
        self.knowledge.append(knowledge_str)
