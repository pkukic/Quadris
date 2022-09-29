function [ro1, ro2, ro3, ro4, mu1, mu2, delta1, delta2] = reflections_and_symmetries(A)
%REFLECTIONS_AND_SYMMETRIES Summary of this function goes here
%   Detailed explanation goes here

ro1 = rot90(A, 1);
ro2 = rot90(A, 2);
ro3 = rot90(A, 3);
ro4 = rot90(A, 4);

mu1 = fliplr(A);
mu2 = flipud(A);

delta1 = rot90(fliplr(A), 3);
delta2 = rot90(fliplr(A), 1);
end