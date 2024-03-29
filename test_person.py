from beings import Person
import pytest


@pytest.fixture()
def person():
    return Person("Dodji Akakpo",40,jobs=["Data Engineer"])

def test_init(person: Person):
    assert person.name == "Dodji Akakpo"
    assert person.age == 40
    assert person.jobs ==["Data Engineer"]

def test_forename(person: Person):
    assert person.forename =="Dodji"

def test_surname(person: Person):
    assert person.surname =="Akakpo"  

def test_no_surname(person: Person):
    person.name = "Dodji"
    assert not person.surname


def test_celebrate_birthday(person: Person):
    person.celebrate_birthday()
    assert person.age == 41

def test_add_job(person: Person):
    person.add_job("Zookeeper")
    assert person.jobs == ["Data Engineer","Zookeeper"]