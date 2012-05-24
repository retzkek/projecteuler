-- project euler (projecteuler.net) problem 31
-- solution by Kevin Retzke (retzkek@gmail.com), May 2012

main = do
    putStrLn (show (count [200,100,50,20,10,5,2,1] 200))

count :: [Int] -> Int -> Int

count [] 0 = 1
count [] _ = 0
count (x:xs) total 
    | x <= total = a+b
    | otherwise  = b
    where a = count (x:xs) (total-x)
          b = count xs total
