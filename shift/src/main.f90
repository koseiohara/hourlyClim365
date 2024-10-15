program main

    use namelist, only : read_nml
    use shifter , only : time_shift

    implicit none

    call read_nml()

    call time_shift()

end program main

