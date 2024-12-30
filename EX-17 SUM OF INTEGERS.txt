% Base Case: The sum of integers from 1 to 0 is 0.
sum_of_integers(0, 0).
% Recursive rule to calculate the sum of integers from 1 to N.
sum_of_integers(N, Sum) :-
    N > 0,                 % Ensure N is positive.
    N1 is N - 1,           % Decrement N by 1.
    sum_of_integers(N1, Sum1),  % Recursively find the sum for N-1.
    Sum is Sum1 + N.       % Calculate the sum by adding N to the sum of N-1.
% Example usage:
% To find the sum of integers from 1 to 5, you can use:
% ?- sum_of_integers(5, X).
% X will contain the result, which is 15 in this case.
