function save_label_matrix(r_label, i)
%SAVE_COLOR Summary of this function goes here
%   Detailed explanation goes here
disp(r_label);
save(append(append('../unique/labels/r_label_', num2str(i)), '.mat'), 'r_label');
end

