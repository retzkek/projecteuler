#!/usr/bin/env escript
%% project euler (projecteuler.net) problem 31
%% solution by Kevin Retzke (retzkek@gmail.com), May 2012
-mode(compile).

main(_) ->
    io:format("~w\n",[count([200,100,50,20,10,5,2,1],200)]).

count([],0) -> 1;
count([],_) -> 0;
count([X|XS],T) ->
    if X =< T -> count([X|XS],T-X)+count(XS,T);
        true  -> count(XS,T)
    end.
