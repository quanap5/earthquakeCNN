#===================================================================================
#This file.m run on Matlab
#Editor: Nguyen Van Quan
#Declare window=20 and threshold=3 or 2 before run this algorithm
##====================================================================================
function out=ThresholdingAlgo(y,window,threshold)

% Get results
[signals,avg,std] = main(y,window,threshold);

figure; 
subplot(2,1,1); 
hold on;
x = 1:length(y); ix = window+1:length(y);
plot(1:length(y),y,'b');
subplot(2,1,2);
stairs(signals,'r','LineWidth',1.5); 
ylim([-1.2 1.2]);
end


function [signals,avgFilter,stdFilter] = main(y,window,threshold)
% Initialise signal results
signals = zeros(length(y),1);
% Initialise filtered series
filteredY = y(1:window+1);
% Initialise filters
avgFilter(window+1,1) = mean(y(1:window+1));
stdFilter(window+1,1) = std(y(1:window+1));
% Loop over all datapoints y(window+2),...,y(t)
window_adap=window
max_window=2000
T=[]
for i=window+2:length(y)
    % If new value is a specified number of deviations away
    count=0;
    
      if (y(i)-avgFilter(i-1) > threshold*stdFilter(i-1)) && (y(i+1)-avgFilter(i-1) > threshold*stdFilter(i-1))...
               && (y(i+2)-avgFilter(i-1) > threshold*stdFilter(i-1))&& (y(i+3)-avgFilter(i-1) > threshold*stdFilter(i-1))...
               &&  (y(i+4)-avgFilter(i-1) > threshold*stdFilter(i-1))&& (y(i+5)-avgFilter(i-1) > threshold*stdFilter(i-1))...
         %       &&  (y(i+6)-avgFilter(i-1) > threshold*stdFilter(i-1))&& (y(i+7)-avgFilter(i-1) > threshold*stdFilter(i-1))

        T=[T abs( (y(i)-avgFilter(i-1))/stdFilter(i-1))]
        signals(i) = 1;
        window_adap=window;

        filteredY(i) = y(i);
        avgFilter(i) = mean(filteredY(i-window:i));
        stdFilter(i) = std(filteredY(i-window:i));

    else
     
        count=0;
        filteredY(i) = y(i);
        if window_adap<max_window
        window_adap=window_adap+1;
        end
        avgFilter(i) = mean(filteredY(i-window_adap:i));
        stdFilter(i) = std(filteredY(i-window_adap:i));
    end
end
% Done, now return results
end

