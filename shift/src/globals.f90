module globals

    implicit none

    integer, parameter :: kp = 4

    integer :: nx
    integer :: ny
    integer :: nz

    integer :: yearend_record
    integer :: final_record
    integer :: output_initial_record

    character(128) :: input_file
    character(128) :: output_file

end module globals

