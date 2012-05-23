! project euler (projecteuler.net) problem 31
! solution by Kevin Retzke (retzkek@gmail.com), May 2012

module combinations
    implicit none
contains
    recursive function countCombinations(vals, ival, total) result(cnt)
        integer :: cnt
        integer, dimension(:), intent(in) :: vals
        integer, intent(in) :: ival, total

        cnt = 0
        if (ival .gt. size(vals)) then
            if (total .eq. 0) then
                cnt = 1
            end if
        else
            if (vals(ival) .le. total) then
                cnt = cnt + countCombinations(vals, ival, total-vals(ival))
            end if
            cnt = cnt + countCombinations(vals, ival+1, total)
        end if
    end function countCombinations
end module

program eu031
    use combinations
    implicit none
    integer, dimension(8) :: coins
    data coins /200,100,50,20,10,5,2,1/

    write(*,*) countCombinations(coins, 1, 500)
end program eu031
