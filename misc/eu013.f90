program eu013
! eulerproject.net problem 13
! generalized to handle any number of integers up to length 100 digits each
! input file should have each number on a new line
implicit none

integer, parameter :: iin=10
integer, parameter :: maxLength = 100
character(len=100) :: cin
character(len=maxLength), allocatable :: nums(:)
! we make the result string twice the size as the largest number to support the
! extra digits that can result from the summation
character(len=maxLength*2) :: res
integer :: nNums
integer :: err
integer :: i, j, n
integer :: carry, sum, rem

! get data file name
if (iargc() < 1) then
    write(*,*) "Usage: eu013 [file]"
    return
end if
call getarg(1, cin)
! open file
open(unit=iin, file=cin)

! count numbers (lines)
nNums = 0
do
    read(iin,*, iostat=err)
    if (err /= 0) exit
    nNums = nNums + 1
end do
allocate(nums(nNums))
rewind(iin)

! read numbers
do i=1,nNums
    read(iin,'(A)',iostat=err) nums(i)
    ! right-justify each number
    nums(i) = adjustr(nums(i))
end do

! initialize result string
write(res,'(200("0"))')

! sum the numbers, starting with the right-most digit and working left
carry = 0
do j=maxLength,1,-1
    sum = carry
    do i=1,nNums
        read(nums(i)(j:j),'(I1)') n
        sum = sum + n
    end do
    ! calulate the remainder (last digit)
    rem = modulo(sum,10)
    ! calculate the carry
    carry = (sum - rem)/10
    ! write the carry to the result string; remember that the result string is
    ! twice the length of the number strings
    write(res(maxLength+j:maxLength+j),'(I1)') rem
end do
! write the final carry to the result string, padded with zeros
write(res(1:100),'(I100.100)') carry

! find the start of the number in the result string
do j=1,maxLength*2
    if (res(j:j) /= '0') exit
end do

write(*,'(A)') res(j:maxLength*2)

end program eu013


