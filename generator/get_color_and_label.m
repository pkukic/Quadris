function [r_color,r_label] = get_color_and_label(r_shape, p_num, p_shapes, d, x)

  color_choice = 4;

%  Get the linear system satisfied by A*x=b.
%
  [ a, b, parent ] = polyomino_multihedral_matrix ( r_shape, p_num, p_shapes, d );
%
%  Get the size of the linear system.
%
  [ a_m, a_n ] = size ( a );
%
%  Get the size of R.
%
  [ r_m, r_n ] = size ( r_shape );
%
%  Get tne number of cells in R.
%
  r_num = polyomino_area ( r_shape );
%
%  Index the nonzero cells in R.
%
  r_index = polyomino_index ( r_shape );
%
%  Get the size of X.
%

   x = cell2mat(x.');
  
%   disp(x);

  [ x_m, x_n ] = size ( x );

%   disp(x_m);
%   disp(x_n);
     
    x_index = 1;

    xc = zeros ( x_m, 1 );
    xi = zeros ( x_m, 1 );

    nz = 0;

    for i = 1 : x_m

      if ( x(i,x_index) == 0 )
        color = 0;
      else
        nz = nz + 1;

        if ( color_choice == 1 )
          color = 1;
        elseif ( color_choice == 2 )
          color = nz;
        elseif ( color_choice == 3 )
          color = i;
        elseif ( color_choice == 4 )
          color = parent(i);
        end

        xc(i) = color;
        xi(i) = nz;

      end

    end
%
%  The first R_NUM rows of A are equations about covering each cell of R.
%
%  Multiplying this matrix times XC gives us:
%
    axc = a(1:r_num,1:a_n) * xc;
    axi = a(1:r_num,1:a_n) * xi;
%
%  R_SHAPE is binary (0 or 1).
%  R_TILING replaces each 1 by the index of the polyomino variant which
%  covers it.
%
    r_color = zeros ( r_m, r_n );
    for i = 1 : r_m
      for j = 1 : r_n
        if ( r_index(i,j) == 0 )
          r_color(i,j) = 0;
        else
          r_color(i,j) = axc(r_index(i,j));
        end
      end
    
    end

    r_label = zeros ( r_m, r_n );
    for i = 1 : r_m
      for j = 1 : r_n
        if ( r_index(i,j) == 0 )
          r_label(i,j) = 0;
        else
          r_label(i,j) = axi(r_index(i,j));
        end
      end
    
    end
end