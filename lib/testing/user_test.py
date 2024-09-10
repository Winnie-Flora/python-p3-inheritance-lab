#!/usr/bin/env python3

from user import User

# lib/testing/user_test.py
import pytest
from lib.teacher import Teacher
from lib.student import Student
from lib.user import User

def test_user_initialization():
    user = User("Jordan", "Zippy")
    assert user.first_name == "Jordan"
    assert user.last_name == "Zippy"

def test_teacher_initialization():
    teacher = Teacher("Olivia", "Spencer")
    assert teacher.first_name == "Olivia"
    assert teacher.last_name == "Spencer"

def test_teacher_teach():
    teacher = Teacher("Olivia", "Spencer")
    knowledge_taught = teacher.teach()
    assert knowledge_taught in teacher.knowledge

def test_student_initialization():
    student = Student("Bruno", "Johnson")
    assert student.first_name == "Bruno"
    assert student.last_name == "Johnson"
    assert student.knowledge == []

def test_student_learn():
    student = Student("Bruno", "Johnson")
    student.learn("OOP in Python")
    assert "OOP in Python" in student.knowledge
