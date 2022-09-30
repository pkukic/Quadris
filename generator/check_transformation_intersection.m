function [flag] = check_transformation_intersection(mat,data)
[ro1, ro2, ro3, ro4, mu1, mu2, delta1, delta2] = reflections_and_symmetries(mat);
% Concatenate along the third axis
s = cat(3, ro1, ro2, ro3, ro4, mu1, mu2, delta1, delta2);
if isempty(data)
    flag = 0;
    return
else
    [m, n, p] = size(data);
    [m, n, q] = size(s);
    % Get intersection
    result = intersect(reshape(s, [], q).', reshape(data, [], p).', 'rows');
    result = reshape(result.', m, n, []);
    flag = ~isempty(result);
end
end

