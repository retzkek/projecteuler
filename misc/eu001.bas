"Project Euler Problem 1"
"TI-BASIC"
0->TOT
For(x,1,999)
If mod(x,3)==0 or mod(x,5)==0
(TOT+x)->TOT
End
Disp TOT
