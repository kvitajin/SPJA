# ﻿# -*- coding: utf-8 -*-


class Subject:

    def __init__(self, name, shortcut, points):
        self._name = name
        self._shortcut = shortcut
        self._points = points
        self._students = {}

    def add_student(self, instance_of_student):
        if type(instance_of_student)==Student:
            self._students[instance_of_student.get_login()] = instance_of_student

    def get_student(self, login):
        if login in self._students:
            return self._students[login]
        else:
            return False

    def remove_student(self, login):
        if login in self._students:
            del self._students[login]
            return
        return False

    def get_best_student(self):
        best = 0
        bestLog = None
        for login, student in self._students.items():
            if student.get_points() > best:
                best = student.get_points()
                bestLog = login
        return self._students[bestLog]

    def list_of_passed_students(self):
        list = []
        for login, student in self._students.items():
            if student.get_points() > self._points:
                list.append(student)
        return list

class Student:

    def __init__(self, name, login):
        self._name = name
        self._login = login
        self._points = 0

    def add_points(self, points):
        if ((type(points)==float or type(points)==int) and points>0):
            self._points+=points

    def get_name(self):
        return self._name

    def get_login(self):
        return self._login

    def get_points(self):
        return self._points

    def __str__(self):
        return "My name is {} (with login {}) and I have {} points.".format(self._name, self._login, self._points)

    def __repr__(self):
        return self.__str__()


def main():
    s1 = Student("Praotec Čech", "cec001")
    s2 = Student("Praotec Slovak", "slo001")
    s3 = Student("Praotec Čechomoravak", "cec002")
    s4 = Student("Petr Novák", "Nov001")

    print(s1)
    print(s2)
    print(s3)
    print(s4)

    spja = Subject("Skriptovací programovací jazyky a jejich aplikace", "SPJA", 6)

    spja.add_student(s1)
    spja.add_student(s2)
    spja.add_student(s3)
    spja.add_student(s4)

    s1.add_points(5)
    s1.add_points(5)
    s2.add_points(6)
    s2.add_points("5")
    s3.add_points(3)

    print()
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    print()

    best = spja.get_best_student()
    if best is not None:
        print("Nejlepší student: {1} {0} [{2}] b".format(best.get_name(), best.get_login(), best.get_points()))

    passed = spja.list_of_passed_students()
    print("List of passed students:")
    for student in passed:
        print ("\t[{} b]\t{}: {}".format(student.get_points(), student.get_login(), student.get_name()))

if __name__ == "__main__":
    main()
