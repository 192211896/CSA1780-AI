% Facts: Name(Name, DOB)
name(john, date(1990, 5, 15)).
name(susan, date(1985, 10, 20)).
name(mike, date(1995, 2, 8)).
name(lisa, date(1982, 7, 3)).
% Queries
% Find the DOB of a person
dob_of_person(Name, DOB) :-
    name(Name, DOB).
