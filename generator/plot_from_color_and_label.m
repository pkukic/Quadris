function plot_from_color_and_label(r_color,r_label,filename)
    color_choice = 4;
    p_num = 6;

    [r_m, r_n] = size(r_color);

    clf ( );
    hold ( 'on' );

%  Make the figure nicely centered
    set(gcf, 'PaperUnits', 'centimeters');
    set(gcf, 'PaperPosition', [0 0 10 10]);
%
%  Before working with imagesc, we want to flip each column.
%
    r_color = flip ( r_color );
    r_label = flip ( r_label );

    disp(r_color);
    disp(r_label);
%
%  Display the solution as a matrix.
%
    imagesc ( r_color );

    lw = 0.04;

    for i = 1 : r_m
      for j = 1 : r_n

        if ( r_label(i,j) ~= 0 ) 
%
%  Horizontal separator above.
%
          if ( i == 1 )
            xl = [ j - 0.5 - lw, j + 0.5 + lw, j + 0.5 + lw, j - 0.5 - lw ];
            yl = [ i - 0.5 - lw, i - 0.5 - lw, i - 0.5 + lw, i - 0.5 + lw ];
            fill ( xl, yl, 'k' );
          elseif ( r_label(i-1,j) == 0 )
            xl = [ j - 0.5,      j + 0.5,      j + 0.5,      j - 0.5      ];
            yl = [ i - 0.5 - lw, i - 0.5 - lw, i - 0.5 + lw, i - 0.5 + lw ];
            fill ( xl, yl, 'k' );
          elseif ( r_label(i-1,j) ~= r_label(i,j) )
            xl = [ j - 0.5, j + 0.5, j + 0.5,      j - 0.5      ];
            yl = [ i - 0.5, i - 0.5, i - 0.5 + lw, i - 0.5 + lw ];
            fill ( xl, yl, 'k' );
          end
%
%  Horizontal separator below.
%
          if ( i == r_m )
            xl = [ j - 0.5,      j + 0.5,      j + 0.5,      j - 0.5      ];
            yl = [ i + 0.5 + lw, i + 0.5 + lw, i + 0.5 - lw, i + 0.5 - lw ];
            fill ( xl, yl, 'k' );
          elseif ( r_label(i+1,j) == 0 )
            xl = [ j - 0.5,      j + 0.5,      j + 0.5,      j - 0.5      ];
            yl = [ i + 0.5 + lw, i + 0.5 + lw, i + 0.5 - lw, i + 0.5 - lw ];
            fill ( xl, yl, 'k' );
          elseif ( r_label(i+1,j) ~= r_label(i,j) )
            xl = [j - 0.5, j + 0.5, j + 0.5,      j - 0.5      ];
            yl = [ i + 0.5, i + 0.5, i + 0.5 - lw, i + 0.5 - lw ];
            fill ( xl, yl, 'k' );
          end
%
%  Vertical separator to left.
%
          if ( j == 1 )
            xl = [ j - 0.5 - lw, j - 0.5 + lw, j - 0.5 + lw, j - 0.5 - lw ];
            yl = [ i - 0.5 - lw, i - 0.5 - lw, i + 0.5 + lw, i + 0.5 + lw ];
            fill ( xl, yl, 'k' );
          elseif ( r_label(i,j-1) == 0 )
            xl = [ j - 0.5 - lw, j - 0.5 + lw, j - 0.5 + lw, j - 0.5 - lw ];
            yl = [ i - 0.5 - lw, i - 0.5 - lw, i + 0.5 + lw, i + 0.5 + lw ];
            fill ( xl, yl, 'k' );
          elseif ( r_label(i,j-1) ~= r_label(i,j) )
            xl = [ j - 0.5,      j - 0.5 + lw, j - 0.5 + lw, j - 0.5      ];
            yl = [ i - 0.5 - lw, i - 0.5 - lw, i + 0.5 + lw, i + 0.5 + lw ];
            fill ( xl, yl, 'k' );
          end
%
%  Vertical separator to right.
%
          if ( j == r_n )
            xl = [ j + 0.5 - lw, j + 0.5 + lw, j + 0.5 + lw, j + 0.5 - lw ];
            yl = [ i - 0.5 - lw, i - 0.5 - lw, i + 0.5 + lw, i + 0.5 + lw ];
            fill ( xl, yl, 'k' );
          elseif ( r_label(i,j+1) == 0 )
            xl = [ j + 0.5 - lw, j + 0.5 + lw, j + 0.5 + lw, j + 0.5 - lw ];
            yl = [ i - 0.5 - lw, i - 0.5 - lw, i + 0.5 + lw, i + 0.5 + lw ];
            fill ( xl, yl, 'k' );
          elseif ( r_label(i,j+1) ~= r_label(i,j) )
            xl = [ j + 0.5 - lw, j + 0.5,      j + 0.5,      j + 0.5 - lw ];
            yl = [ i - 0.5 - lw, i - 0.5 - lw, i + 0.5 + lw, i + 0.5 + lw ];
            fill ( xl, yl, 'k' );
          end

        end
      end
    end

    hold ( 'off' );
%
%  Coloring option 1:
%  0 = white for blank space.
%  1 = light blue for all polyominoes.
%
    if ( color_choice == 1 )

      color_num = 2;
%
%  Coloring option 2:
%  Allow a color for each nonzero variable, plus 0=white.
%
    elseif ( color_choice == 2 )
      color_num = nz + 1;
%
%  Coloring option 3:
%  Allow a color for each variable, plus 0=white.
%
    elseif ( color_choice == 3 )
      var_num = x_m;
      color_num = var_num + 1;
%
%  Coloring option 4:
%  Allow a color for each "parent", plus 0=white.
%
    elseif ( color_choice == 4 )
      color_num = p_num + 1;
    end

    caxis ( [ 0, color_num - 1 ] );
%
%  For gray scale plots, change "false" to "true".
%
    if ( false )
      colormap ( gray ( color_num ) );
      cmap = colormap ( );
      newmap = contrast ( cmap );
      newmap(1,1:3) = [ 1, 1, 1 ];
      colormap ( newmap );
      brighten ( 0.4 );
%
%  You can change "jet" to another built-in MATLAB color map.
%
    else
      colormap ( jet ( color_num ) );
      cmap = colormap ( );
      cmap(1,1:3) = [ 1, 1, 1 ];
      colormap ( cmap );
    end
%
%  Title the plot.
%
%     title ( { label; filename2 } )
%
%  Use the same scale for X and Y directions.
%
    axis ( 'equal' )
%
%  Don't display the graph axes.
%
    axis ( 'off' )

%     shg();

    saveas(gcf, filename);
    fprintf ( 1, '  Saved plot as "%s"\n', filename);
end

