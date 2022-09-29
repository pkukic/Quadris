function save_plots(a,b)
set(0, 'DefaultFigureVisible', 'off');
for i = a:b
    fname_color = append(append('../unique/colors/r_color_', num2str(i)), '.mat');
    fname_label = append(append('../unique/labels/r_label_', num2str(i)), '.mat');
    fname_plot = append(append('../unique/plots/plot_', num2str(i)), '.png');
    plot_from_color_and_label(load(fname_color).r_color, load(fname_label).r_label, fname_plot);
end
set(0, 'DefaultFigureVisible', 'on');
end

