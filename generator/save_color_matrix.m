function save_color_matrix(r_color, i)
%SAVE_COLOR Summary of this function goes here
%   Detailed explanation goes here
disp(r_color);
save(append(append('../unique/colors/r_color_', num2str(i)), '.mat'), 'r_color');
end

