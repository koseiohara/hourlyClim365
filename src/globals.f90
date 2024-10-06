module globals

    implicit none

    integer, parameter :: kp = 4

    integer :: nx
    integer :: ny
    integer :: nz

    integer :: time_ini
    integer :: year_num
    integer :: records_day
    integer :: vars
    integer :: var_number

    character(128) :: input_file
    character(128) :: output_file

end module globals

