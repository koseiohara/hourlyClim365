program main

    use namelist, only : read_nml
    use clim    , only : hourly_clim_365

    implicit none


    call read_nml()

    call hourly_clim_365()

end program main

