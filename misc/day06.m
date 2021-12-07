1;

function retval = fish(d, inp)
   # build matrix
   M = zeros(9,9);
   for i = 1:8
     M(i,i+1) = 1;
   endfor
   M(7,1) = 1;
   M(9,1) = 1;
   M
   # build counter
   cnt = zeros(1,9);
   for i = 0:8
     cnt(1,i+1) = sum(inp == i);
   endfor
   
   retval = sum(M^d*transpose(cnt));
 endfunction
 
 sampleinput = [3,4,3,1,2]
 
 part1 = fish(80,sampleinput);
 part2 = fish(256,sampleinput);
 
 format('long')
 disp("Part 1:"), disp(part1)
 disp("Part 2:"), disp(part2)
 