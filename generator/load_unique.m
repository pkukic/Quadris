function [data] = load_unique(fnames)
data_cell = {};
for i=1:length(fnames)
    data_cell{i} = load(fnames{i}).r_color; 
end
data = cat(3,data_cell{:});
end

