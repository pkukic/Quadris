function [flag] = check_if_in_unique(mat, fnames)
%CHECK_IF_IN_UNIQUE Summary of this function goes here
%   Detailed explanation goes here
data = load_unique(fnames);
% disp(data);
flag = check_transformation_intersection(mat,data);
% disp(flag);
end

