% Estimate sensitvity and bias given a single hit rate and false-positive rate based on area under the ROC
% See Zhang, J. & Mueller, S.T. Psychometrika (2005) 70: 203. https://doi.org/10.1007/s11336-003-1119-8
% 
% INPUTS:
% 	h = hit rate
% 	f = false alarm rate
% OUTPUTS:
% 	A = sensitivity (min = 0, chance = 0.5, max = 1)
% 	lb = log response bias (lb>0 means liberal so more towards yes, lb<0 means conservative so more towards no)
% 
% ----------------------------------------------------------------------------
%  Created by Vincent Ka Ming Cheung on 2018 03 06 
%  at the Max Planck Institute for Human Cognitive and Brain Sciences,
%  Leipzig, Germany
% 
%  This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 Internaional License
% 
%  --- Use at your own risk! While I tried my best, I am not responsible for any errors in the code... ---

function [A,lb] = calcA(h,f)
	% check if values or vectors entered
	if length(h) || length(f) ~=1
		error('enter hit rate and false alarm rate as values')
	end
	
	% check if h and f in [0,1]
	if h > 1 || h < 0
		error('hit rate must be in [0,1]')
	end
	if f > 1 || f < 0
		error('false alarm rate must be in [0,1]')
	end
	
	% calculate sensitivity first
	if f>h
		error('more false positives than true positives')
	elseif f <= 0.5 && 0.5 <= h
		A = .75 + (h-f)/4 - f*(1-h);
	elseif f <= h &&  h < 0.5
		A = .75 + (h-f)/4 - f/(4*h);
	elseif 0.5 < f && f <= h
		A = .75 + (h-f)/4 - (1-h)/(4*(1-f));
	else
		error('something is wrong with f and h for A')
	end
	
	% calculate log bias (for symmetry)
	if f>h
		error('more false positives than true positives')
	elseif f <= 0.5 && 0.5 <= h
		b = (5-4*h)/(1+4*f);
	elseif f < h &&  h < 0.5
		b = (h^2 + h)/(h^2 + f);
	elseif 0.5 < f && f < h
		b = ((1-f)^2 + (1-h))/((1-f)^2 + (1-f));
	else
		error('something is wrong with f and h for b')
	end
	lb = log(b);
end
