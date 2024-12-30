wet_grass :- raining.

working_hard :- studying(john), studying(mary).

% Define initial facts
raining.
studying(john).
studying(mary).

% Forward chaining
conclude(X) :- wet_grass, X = 'The grass is wet.'.
conclude(X) :- working_hard, X = 'John and Mary are working hard.'.
