function [r_color,r_label] = color_and_label_for_quadris(x)
  r_shape = ones(9,9);
    %
    %  How many free polyominoes are there?
    %
      p_num = 6;  
    %
    %  Create binary matrices for the polyominoes and pack them into p_shapes
    %
      for page = 1:p_num
          p_shapes(:,:,page) = zeros(9,9);
      end
    
      p_shapes(1,1,1) = 1;
      p_shapes(1:4,1,2) = [1; 1; 1; 1];
      p_shapes(1:3,1:2,3) = [1 1; 1 0; 1 0];
      p_shapes(1:2,1:2,4) = [1 1; 1 1];
      p_shapes(1:3,1:2,5) = [1 0; 1 1; 1 0];
      p_shapes(1:3,1:2,6) = [1 0; 1 1; 0 1];
    
    %
    %  How many copies of each pariomino do we use?
    %
      d = [1 2 5 5 4 4]; 
      [r_color,r_label] = get_color_and_label(r_shape,p_num,p_shapes,d,x);
      return
end

